# 11_flySwat.py
# A game to swat flies
#
# Name: Benjamin Goldstone
# Date: 11/03/2020

import pygame
from random import randint

# Initialize all that Pygame provides
pygame.init()
pygame.mixer.init() # Enables sound effects

# Global constants:
WIDTH     = 1000
HEIGHT    = 600
FLY_COUNT = 10
DELTA     = 20
BG_COLOR  = (255,255,255)
FONT_COLOR = (0,0,0)
RANDOMIZER = 3
SCORE_POS = (WIDTH//2, 20)

## CLASS DEFINITIONS ##

class Fly(pygame.sprite.Sprite):
    # A member of the Fly class is a sprite that moves around the screen making
    #   random speed changes and bouncing off the edges of the screen.  If it
    #   collides with a swatter, the swat() method is used to change the image
    #   and freeze the location.
        
    def __init__(self, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("11_liveFly.png")
        self.image = self.image.convert()
        self.image.set_colorkey( self.image.get_at((1,1)) ) 
        self.rect = self.image.get_rect()
        self.rect.center = position  # position is an (x, y) pair
        (self.dx, self.dy) = speed   # speed is a (speedX, speedY) pair
        self.alive = True

    def update(self, screen):
        # This method controls movement of the fly object

        if self.alive :     # Only move if it's a living fly
            # Change .dx and .dy to randomize speed each clock tick
            #   so that it looks like a fly buzzing around aimlessly
            self.dx += randint(-RANDOMIZER, RANDOMIZER)
            self.dy += randint(-RANDOMIZER, RANDOMIZER)
            self.rect.centerx += self.dx
            self.rect.centery += self.dy

            if self.rect.left <= 0:
                #self.rect.left = 0
                self.dx = abs(self.dx)
            if self.rect.right >= screen.get_width():
                #self.rect.right = screen.get_width()
                self.dx = -abs(self.dx)
            if self.rect.top <= 0:
                #self.rect.top = 0
                self.dy = abs(self.dy)
            if self.rect.bottom >= screen.get_height():
                #self.rect.bottom = screen.get_height()
                self.dy = -abs(self.dy)

        
        
    def swat(self):
        self.image = pygame.image.load("11_deadFly.png")
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((1, 1)))
        self.dx = 0
        self.dy = 0
        self.alive = not self.alive
class Swatter(pygame.sprite.Sprite):
    # A swatter is a sprite that moves around the screen following mouse 
    #   movements.  If it has a collision with a Fly object, the fly is swatted.     
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("11_swatter.png")
        self.image = self.image.convert()
        self.image.set_colorkey( self.image.get_at((1, 1)) ) 
        self.rect = self.image.get_rect()
        
    def update(self, screen):
        self.rect.center = pygame.mouse.get_pos()
    

        
class Label(pygame.sprite.Sprite):
    # This class puts a message on the screen
    
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)
        fontList = []
        #for font in pygame.font.get_fonts():
            #fontList.append(font)
        #self.font = pygame.font.SysFont(fontList[randint(0, len(fontList))], size)
        self.font = pygame.font.Font("11_SyneMono-Regular.ttf", size)
        self.text = " " # Space (" " not "") This avoids visual artifact on some HW
        self.position = position
        
    def update(self, screen):
        self.image = self.font.render(self.text, 1, FONT_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

## MAIN ##
def main():

    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption("Ben Goldstone")
    
    # Create the background Surface object
    background = pygame.Surface(screen.get_size())
    background.fill( BG_COLOR )
    screen.blit(background, (0, 0))
    
    # Create Sound objects
    yay = pygame.mixer.Sound("11_yay.wav")
    slap = pygame.mixer.Sound("11_slap.wav")
    aww = pygame.mixer.Sound("11_aww.mp3")
    # Create a Label object (used when the game ends)
    message = Label( (screen.get_width()//2, screen.get_height()//2), 60 )
    
    # Create a scoreboard
    scoreboard = Label( SCORE_POS, 30 )
    
    # Create a Swatter object
    swatter = Swatter()
    
    # Create a list of Fly objects
    flies = []
    for  fly in range(FLY_COUNT):
        fly = Fly(( randint(0,screen.get_width()), randint(0, screen.get_height()) ),(randint(-DELTA,DELTA), randint(-DELTA,DELTA)))
        flies.append(fly)
            
    # Create sprite groups.
    #  Every sprite must be in a group, but there can be more than one group.
    flyGroup = pygame.sprite.Group(flies)  # All the flies are initially alive
    deadGroup = pygame.sprite.Group()  # Initially empty.  As flies are swatted, they
                                       # are removed from flyGroup and added to deadGroup.
    otherSprites = pygame.sprite.Group(swatter, scoreboard)
    flyNum = len(flies)
    keepGoing = True
    win = False
    clock = pygame.time.Clock()
    while keepGoing:
        clock.tick(30)
        swatList = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                message.text = "You lost :("
                otherSprites.add(message)
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    message.text = "You lost :("
                    otherSprites.add(message)
                    keepGoing = False
        if(pygame.mouse.get_pressed()[0] == True):
            pygame.mouse.set_visible(False)
            swatList = pygame.sprite.spritecollide(swatter, flyGroup, True)
        else:
            pygame.mouse.set_visible(True)
        # In spriteCollide(), if the third parameter is "True", then each 
        #   colliding sprite is removed from the flyGroup.

        for fly in swatList:   # swatList is all the flies that are currently being swatted
            fly.swat()
            slap = pygame.mixer.Sound("11_slap.wav")
            slap.play()
            deadGroup.add(fly) # add the fly to the deadGroup
            flyNum -= 1
                
                
        scoreboard.text = "Flies remaining: " + str(flyNum)
        if (flyNum <= 0) :
            message.text = "YOU WIN!"
            otherSprites.add(message)
            win = True
            keepGoing = False
            
        # All sprite groups must have .clear(), .update(), and .draw() at the end
        #   of the game loop, just before the .flip().  This is true for the group
        #   of live flies, the group of dead flies, and the group of other sprites.
        flyGroup.clear(screen, background)
        deadGroup.clear(screen, background)
        otherSprites.clear(screen, background)
        
        flyGroup.update(screen)
        deadGroup.update(screen)
        otherSprites.update(screen)
        
        flyGroup.draw(screen)
        deadGroup.draw(screen)
        otherSprites.draw(screen)
    
        pygame.display.flip()
        
    # After the game loop is finished
    if win:
        yay.play()
        pygame.time.wait(int(yay.get_length() * 1000)) # pause (in milliseconds)
    else:
        aww.play()
        pygame.time.wait(int(aww.get_length() * 1000))
            
# Start the program running
main()

# Clean up
pygame.quit()

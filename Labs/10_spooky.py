# 10_spooky.py
#
# Name: Benjamin Goldstone
# Date: 10/27/20200

# Import and initialize
import pygame
pygame.init()

from random import randint

WIDTH = 800
HEIGHT = 600

SPRITE_COUNT = 3  # How many sprites of each type?
SPEED_X = 10         #uses int to generate randint between negative and postive number
SPEED_Y = SPEED_X   #uses int to generate randint between negative and postive number


RVBUTTON_X = 20
RVBUTTON_Y = 20
RVBUTTON_W = 100
RVBUTTON_H = 30
RVBUTTON_LABELXY = (12, 10)
# Display configuration
screen = pygame.display.set_mode( (WIDTH,HEIGHT) ) 
pygame.display.set_caption("Ben Goldstone")

class Pumpkin(pygame.sprite.Sprite):

    # The constructor method for a Pumpkin object.
    # Accepts four input arguments for location and motion of the object.
    def __init__(self, xPos, yPos, speedX, speedY):
        pygame.sprite.Sprite.__init__(self)         # Initialize the sprite.
        self.dx = speedX
        self.dy = speedY
        self.image = pygame.image.load("10_pumpkin.png").convert()
        self.image.set_colorkey( self.image.get_at((1,1)) )
        self.rect = self.image.get_rect()
        self.rect.centerx = xPos
        self.rect.centery = yPos
    # The updater method; requires no arguments
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx = -self.dx
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            self.dx = -self.dx
        if self.rect.top < 0:
            self.rect.top = 0
            self.dy = -self.dy
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
            self.dy = -self.dy
    def reverse(self):
        self.dx = -self.dx
        self.dy = -self.dy
class Ghost(pygame.sprite.Sprite):

    # The constructor method for a Ghost object.
    # Accepts four input arguments for location and motion of the object.
    def __init__(self, xPos, yPos, speedX, speedY):
        pygame.sprite.Sprite.__init__(self)         # Initialize the sprite.
        self.dx = speedX
        self.dy = speedY
        self.image = pygame.image.load("10_ghost.png").convert()
        self.image.set_colorkey(self.image.get_at((1, 1)))
        self.rect = self.image.get_rect()
        self.rect.centerx = xPos
        self.rect.centery = yPos
        #### Add code here for the Ghost class constructor.

    # The updater method; requires no arguments
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.left > screen.get_width():
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.right = screen.get_width()
        elif self.rect.top > screen.get_height():
            self.rect.top = 0
        elif self.rect.bottom < 0:
            self.rect.bottom = screen.get_height()
    def reverse(self):
        self.dx = -self.dx
        self.dy = -self.dy
def main():

    # Create some entities:
    # First, the background Surface
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((randint(0,255),randint(0,255),randint(0,255)))

    # Draw the background on the screen before the loop to start with a fresh view
    screen.blit(background, (0,0))

    #Next, construct some Pumpkin and Ghost objects
    pumpkinList = []
    for i in range(SPRITE_COUNT):
        pumpkinList.append(Pumpkin(randint(0,screen.get_width()), randint(0,screen.get_height()), randint(-SPEED_X,SPEED_X), randint(-SPEED_Y,SPEED_Y)))
    ghostList = []
    for i in range(SPRITE_COUNT):
        ghostList.append(Ghost(randint(0, screen.get_width()), randint(0, screen.get_height()), randint(-SPEED_X, SPEED_X),randint(-SPEED_Y, SPEED_Y)))
    # Put the objects into a sprite group    
    allSprites = pygame.sprite.Group(pumpkinList + ghostList) #### Fill this in with your list of objects

    # Action: Assign key variables
    clock = pygame.time.Clock()
    keepGoing = True
    drawButton(background)
    # The Game Loop
    while keepGoing:

        # Set the timer to tick 30 times per second
        clock.tick(30)

        # The Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_SPACE:
                    background.fill((randint(0,255),randint(0,255),randint(0,255)))
                    screen.blit(background, (0,0))
                    drawButton(background)
                elif event.key == pygame.K_r: #Restarts Game
                    keepGoing = False
                    main()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_visible(False)  # Hide the mouse pointer

                (mouseX, mouseY) = pygame.mouse.get_pos()
                if ((mouseX >= RVBUTTON_X and mouseX <= RVBUTTON_X + RVBUTTON_W) and
                        (mouseY >= RVBUTTON_Y and mouseY <= RVBUTTON_Y + RVBUTTON_H)):
                    for sprite in ghostList:
                        sprite.reverse()
                    for sprite in pumpkinList:
                        sprite.reverse()

            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.mouse.set_visible(True)  # Make the mouse visible again
        # Refresh the display                
        allSprites.clear(screen, background)  # Clear the sprites from the previous frame
        allSprites.update()                   # Call update() on each sprite to determine new positions
        allSprites.draw(screen)               # Draw all sprites on the screen at their new positions
        
        pygame.display.flip()                 # Flip the screen to make the changes visible.

# Call main() to kick things off
def drawButton(bg):
    pygame.draw.rect(bg, (0, 0, 0), ((RVBUTTON_X, RVBUTTON_Y), (RVBUTTON_W, RVBUTTON_H)), 0)
    myfont = pygame.font.SysFont('Times New Roman', 30)
    textSurface = myfont.render('Reverse', True, (255, 255, 255))
    bg.blit(textSurface, (RVBUTTON_X + 2, RVBUTTON_Y))
    screen.blit(bg, (0, 0))
main()

# Clean up
pygame.quit()

# frogger.py
#
# B. Kell 11/2018 update 11/2020
#
# Modified by:  Ben Goldstone
# Date:         11/17/2020
#
# This is a game inspired by the old video game "Frogger".  In this simplified
#   version, the player must navigate a frog across six lanes of traffic to
#   land on one of three lily pads.  Player wins if all three lily pads are 
#   occupied.  Player loses if any frog gets squished.

import pygame
from random import randint
pygame.init()

WIDTH=640
HEIGHT=480
#DEFAULT_FONT = pygame.font.get_default_font()

screen = pygame.display.set_mode((WIDTH,HEIGHT))   # Construct the screen and
pygame.display.set_caption("Ben Goldstone")       # set its caption.

##############################################################################
# A Car sprite is the moving obstacle that might run over a frog.
class Car(pygame.sprite.Sprite):

    def __init__(self, ypos, direction):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        # Create a red rectangular car, 40 tall and randint(40,120) wide
        self.image = pygame.Surface((randint(40,120),40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        # Initial location and speed of the car:
        self.rect.centerx = randint(0,screen.get_width())
        self.rect.centery = ypos
        self.dx = randint(3,10) * direction  # Either positive or negative
        
    #  self.update() - Move the car left or right across the screen, with wrap.
    def update(self):

        self.rect.centerx += self.dx        # Move the car horizontally.

        # If the car moves off-screen, wrap it to come back in from the other side
        if self.rect.right < 0:
            self.rect.left = screen.get_width()
        elif self.rect.left > screen.get_width():
            self.rect.right = 0


##############################################################################
# A Frog sprite is used to create the frog!
class Frog(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        self.image = pygame.Surface((40,40))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect();     # Get rectangle for the frog.
        self.rect.center = (320, 450)   # Initial location safe on the grass.

    #  self.moveup() - Move the frog up, but stay on the screen.
    #    Only allows movemnet up from the top lane if frog lines up with
    #    one of the lilypads, which are at x=160, 320, and 480
    def moveup(self):
        if self.rect.top > 120 or (self.rect.centerx in [160, 320, 480] ):
            self.rect.top -= 60

    #  self.movedown() - Move the frog down, but stay on the screen.
    def movedown(self):
        if (self.rect.bottom < (screen.get_height() - 60)):
            self.rect.bottom += 60
        
    #  self.moveleft() - Move the frog left, but stay on the screen.
    def moveleft(self):
        if (self.rect.left > 20):
            self.rect.left -= 20

    #  self.moveright() - Move the frog right, but stay on the screen.
    def moveright(self):
        if (self.rect.right < (screen.get_width() -20)):
            self.rect.right += 20
        
    def reset(self):
        self.rect.center = (320, 450)


##############################################################################
# A Lily sprite is one of the lilypad destinations
class Lily(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)       # Initialize the sprite.

        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect();     # Get rectangle for the lily.
        self.rect.center = position   # position in the water strip

    # If a frog lands on a lilypad, 'mark' the lilypad as 'occupied' by
    #   painting a frog-like blue square on it.
    def paintfrog(self):
        pygame.draw.rect(self.image, (0,0,255), ((5,5),(40,40)), 0)


##############################################################################
# A Label is used to render text on the screen.  When constructed
#         the following parameters are specified:
#              textStr - the text to render on the label.
#              topleft - the topleft pixel location.
#              fontType - the font file or None.
#              fontSize - the size of the font.
#              textColor - the color of the text on the label.
class Label(pygame.sprite.Sprite):

    def __init__(self, textStr, center, fontType, fontSize, textColor):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(fontType, fontSize)
        self.text = textStr
        self.center = center
        self.textColor = textColor

    # self.update() - Render the text on the label.
    def update(self):
        self.image = self.font.render(self.text, 1, self.textColor)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


##############################################################################
#   titleScreen() - Display a title screen and instructions.
#                    The screen stays displayed until the
#                    user clicks the mouse to start the game.
def titleScreen():
    
    background = pygame.Surface(screen.get_size()) # Construct a background
    background = background.convert()
    background.fill((110,255,100))   # Clear the background
    screen.blit(background, (0,0))  # Blit background to screen only once.

    # Construct labels for a title and game instructions.  
    titleMsg = Label("Frogger!", (320,240), None, 60, (0,0,0))
    startMsg = Label("Click to start", (500,420), None, 30,(0,0,0))
    # Add the labels to a group  
    labelGroup = pygame.sprite.Group(titleMsg, startMsg)

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:  
        clock.tick(30)  # Frame rate 30 frames per second.

        for event in pygame.event.get():      # Handle any events
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Title screen ends
                keepGoing = False                      # when mouse clicked
            elif event.type == pygame.KEYDOWN:         # or any key pressed
                keepGoing = False
                                                       
        labelGroup.clear(screen, background)  # Update the display
        labelGroup.update()
        labelGroup.draw(screen)
        
        pygame.display.flip()
                

##############################################################################
#  game() - Play Frogger
def game():

    background = pygame.Surface(screen.get_size()) # Construct a background
    background = background.convert()
    background.fill((255,255,255))   # Clear the background
    pygame.draw.rect(background, (0,128,255), ((0,0),(WIDTH,60)), 0)
    pygame.draw.rect(background, (50,255,50), ((0,420),(WIDTH,60)), 0)  
    for y in range(60,480,60):
        pygame.draw.line(background, (0,0,0), (0,y), (WIDTH,y), 1)
    
    screen.blit(background, (0,0))
    countdown = 30
    frames = 0
    moves = 0
    # Construct the game entities:
    frog = Frog()                  # A Frog object.  
    
    carList = []                   # Make six Car objects
    direction = 1
    for lane in range(90, 400, 60):
        car = Car(lane, direction) 
        direction = -direction     # Alternate direction (+1 or -1)
        carList.append(car)
        
    lilyList = []                  # Make three lily pads
    for pos in range(160, 500, 160) :
        lily = Lily( (pos, 30) )
        lilyList.append(lily)
    countdownTimer = Label(f"Time remaining: {countdown}", (150, screen.get_height() - 20), None, 30, (0, 0, 0))
    totalMoves = Label(f"Total number of moves: {moves}", (screen.get_width() - 150, screen.get_height() - 20), None,30, (0, 0, 0))

    # Add the sprites to groups.
    frogSprite = pygame.sprite.Group(frog)
    carSprites = pygame.sprite.Group(carList)
    lilySprites = pygame.sprite.Group(lilyList)  # Empty lilies
    doneSprites = pygame.sprite.Group()          # Occupied lilies
    labelSprites = pygame.sprite.Group(countdownTimer, totalMoves)

    clock = pygame.time.Clock()    # A clock for setting a frame rate.
    keepGoing = True               # Signals the game is over.
    win = False
    while keepGoing:  
        clock.tick(30)             # Frame rate 30 frames per second.
        frames += 1
        if frames == 30:
            countdown -= 1
            frames = 0
        for event in pygame.event.get():    # Handle any events
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_UP:     # Move frog up.
                    frog.moveup()
                    moves += 1
                elif event.key == pygame.K_DOWN:   # Move frog down.
                    frog.movedown()
                    moves += 1
                elif event.key == pygame.K_LEFT:   # Move frog left.
                    frog.moveleft()
                    moves += 1
                elif event.key == pygame.K_RIGHT:  # Move frog right.
                    frog.moveright()
                    moves += 1

        if pygame.sprite.spritecollide(frog, carSprites, False):  # squish
            keepGoing = False
        else :
            landed = pygame.sprite.spritecollide(frog,lilySprites,True)
            if landed:     # Successfully landed on a lilypad
                landed[0].paintfrog()
                doneSprites.add(landed[0])
                frog.reset()
                
        if len(doneSprites) == 3:
            win = True
            keepGoing = False
        if countdown == 0:
            keepGoing = False
        countdownTimer.text = f"Time remaining: {countdown}"
        totalMoves.text = f"Total number of moves: {moves}"


        frogSprite.clear(screen, background)
        carSprites.clear(screen, background)
        lilySprites.clear(screen, background)
        doneSprites.clear(screen, background)
        labelSprites.clear(screen, background)

        frogSprite.update()
        carSprites.update()
        lilySprites.update()
        doneSprites.update()
        labelSprites.update()

        frogSprite.draw(screen)
        carSprites.draw(screen)
        lilySprites.draw(screen)
        doneSprites.draw(screen)
        labelSprites.draw(screen)

        pygame.display.flip()

    return win,countdown,moves


##############################################################################
# playAgain() - Report the win or loss and ask the user for a replay
def playAgain(winLose,timeLeft,moves):
    
    background = pygame.Surface(screen.get_size()) # Construct a background
    background = background.convert()

    if winLose:
        fillColor = (110,255,100)
        labelText = "You Win!!"
        labelColor = (128,0,0)
    else:
        fillColor = (128,0,0)
        labelText = "You Lose..."
        labelColor = (110,255,100)

    background.fill(fillColor)
    screen.blit(background, (0,0))
    
    # Construct Labels 
    label0 = Label(labelText, (320,110), None, 60, labelColor)
    label1 = Label(f"You did {moves} moves in {timeLeft} seconds!",(320,180),None,50,labelColor)
    label2 = Label("Play again?", (320,280), None, 60, labelColor)
    label3 = Label("(Y/N)", (320,380), None, 60, labelColor)
    labelGroup = pygame.sprite.Group( label0, label1, label2,label3 )

    clock = pygame.time.Clock()
    keepGoing = True
    replay = False

    while keepGoing:
    
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    replay = True
                    keepGoing = False
                elif event.key == pygame.K_n:
                    keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False

        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()
        
    return replay


##############################################################################
# endMessage() - Display a message at end of play for 5 seconds.
def endMessage():
    
    background = pygame.Surface(screen.get_size()) # Construct a background
    background = background.convert()
    background.fill((0,255,255))
    screen.blit(background, (0,0))   # Blit background to screen only once.

    # Construct a Label object to display the message and add it to a group.
    label1 = Label("Good Bye...", (320,210), None, 60, (0,0,0))
    label2 = Label("A Mules Kick production", (320,320), None, 30, (0,0,0))
    label3 = Label("©2020", (320,360), None, 30, (0,0,0))
    labelGroup = pygame.sprite.Group( label1, label2, label3 )

    clock = pygame.time.Clock()
    keepGoing = True
    frames = 0                  # 5 seconds will be 150 frames

    while keepGoing:
    
        clock.tick(30)          # Frame rate 30 frames per second.
        frames = frames + 1     # Count the number of frames displayed
        if frames == 150:        # After 5 seconds end the message display
            keepGoing = False 

        for event in pygame.event.get():    # Impatient people can quit earlier
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN or
                event.type == pygame.MOUSEBUTTONDOWN) :
                keepGoing = False

        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()


##############################################################################
# The main program:
#   Displays the title/instructions page, runs the main game() function
#   (with replay if desired), and then displays the final "The End" message.
def main():
    
    titleScreen()               # Display title and instructions.
    
    replay = True
    while replay :
        (winLose,time,moves)= game()                      # Play the game.
        replay = playAgain(winLose,time,moves)
        
    endMessage()     # Final "The End" Screen.


##############################################################################
# Call the main program
main()
pygame.quit()

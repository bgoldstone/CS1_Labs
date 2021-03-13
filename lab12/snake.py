#################################
# snake.py
#
# Name: Ben Goldstone
# Date: 11/16/2001
#
# The classic arcade game "Snake"
#
#################################

import pygame
from random import randint

pygame.init()

# Constants:
WIDTH  = 900
HEIGHT = 600
CENTER = (WIDTH//2, HEIGHT//2)

INIT_TICK  = 5                      # Clock ticks per second (5 is slow)

SEG_SIZE   = 17                     # Size of a (square) snake segment
SEG_MARGIN = 3                     # Blank space in between segments
STEP_SIZE  = SEG_SIZE + SEG_MARGIN  # Spacing of segments

INIT_SNAKE_LEN = 3                  # Number of segments in a baby snake
WIN_SNAKE_LEN  = 25              # What does it take to win?

# Some basic color names
BLACK     = (0,0,0)
RED       = (255,0,0)
GREEN     = (0,255,0)
BLUE      = (0,0,255)
YELLOW    = (255,255,0)
MAGENTA   = (255,0,255)
CYAN      = (0,255,255)
DARKCYAN = (0, 107, 98)
WHITE     = (255,255,255)
MAROON    = (128,0,0)
ORANGE    = (255,123,0)
BROWN  = (181, 140, 83)
PURPLE   =(31, 0, 74)

# Background fill colors for the various screens
TITLE_BG  = (110,255,100)
REPLAY_BG = (0,0,127)
GAME_BG   = BLACK
END_BG    = DARKCYAN


screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Ben Goldstone")  #### Don't forget this!

#####################################################################################################
# A snake is made up of a series of Segment sprites
class Segment(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SEG_SIZE, SEG_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = location
#####################################################################################################
# An Apple sprite is a target that the snake wants to eat
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SEG_SIZE, SEG_SIZE)).convert()
        self.image.fill(BLACK)
        halfBox = SEG_SIZE//2
        self.apple = pygame.draw.circle(self.image, GREEN, (halfBox, halfBox), halfBox, 0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((1, 1)))
        self.rect.center = (( randint(0,screen.get_width()), randint(0,screen.get_height()) ))
    def reposition(self, segGroup):
        self.rect.centerx = randint(3, (screen.get_width()//STEP_SIZE)  - 3) * STEP_SIZE
        self.rect.centery = randint(3, (screen.get_height()//STEP_SIZE) - 3) * STEP_SIZE
        while( pygame.sprite.spritecollide(self, segGroup, False) ) :
            self.rect.centerx = randint(3, (screen.get_width()//STEP_SIZE)  - 3) * STEP_SIZE
            self.rect.centery = randint(3, (screen.get_height()//STEP_SIZE) - 3) * STEP_SIZE

#####################################################################################################
# Label sprites are used for the scoreboard, the title screen, etc.
#   Creating a Label sprite requires 5 parameters:
#       msg       - a string
#       center    - an (x,y) pair of the center point of the Label object
#       fontFile  - name of a .ttf font file in the current folder (or "None")
#       textSize  - height of the text, in pixels
#       textColor - an (r,g,b) triple of the color of the text
class Label(pygame.sprite.Sprite):
    def __init__(self, msg, center, fontFile, textSize, textColor):
        pygame.sprite.Sprite.__init__(self)
        self.font     = pygame.font.Font(fontFile, textSize)
        self.text     = msg
        self.center   = center
        self.txtColor = textColor

    def update(self):
        self.image       = self.font.render(self.text, 1, self.txtColor)
        self.rect        = self.image.get_rect()  # get a new rect after any text change
        self.rect.center = self.center

#####################################################################################################
# TitleScreen puts up an inital welcome screen and waits for the user to click the mouse
def titleScreen():
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill( TITLE_BG )     # Fill the background
    screen.blit(background, (0,0))  # Blit background to screen
    #### Fill in here to construct labels for a title and game instructions.
    #### Use multiple Label sprites to do this.
    #### Add your Label sprites to labelGroup.
    title = Label("SNAKE GAME", (screen.get_width()//2,125),"fonts/DejaVuSans-Bold.ttf", 56, PURPLE)
    instructions = Label("Goal: get snake to length of " + str(WIN_SNAKE_LEN) + " boxes long by eating green apples", (screen.get_width()//2,200),"fonts/DejaVuSans.ttf", 20, PURPLE)
    instructions2 = Label("Keyboard: hit \"q\" or \"esc\" to quit", (screen.get_width()//2,225),"fonts/DejaVuSans.ttf", 20, PURPLE)
    instructions3 = Label("Use \"up/down/left/right\" arrow keys to move", (screen.get_width()//2,250),"fonts/DejaVuSans.ttf", 20, PURPLE)
    instructions4 = Label("If snake touches tail game over!", (screen.get_width()//2,275),"fonts/DejaVuSans.ttf", 20, PURPLE)
    instructions5 = Label("press Left Mouse Button to Start!", (screen.get_width()//2,300),"fonts/DejaVuSans.ttf", 20, PURPLE)

    labelGroup = pygame.sprite.Group([title,instructions,instructions2,instructions3,instructions4,instructions5])
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:  
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                                                       
        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)
        
        pygame.display.flip()
                
#####################################################################################################
# The game() function performs the actual gameplay.  Returns a boolean
def game():
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill( GAME_BG )
    #image = pygame.image.load("external-content.duckduckgo.com.jpg")
    # Fill the background
    screen.blit(background, (0,0))  # Blit background to screen

    # Create sprites and sprite groups
    scoreboard = Label("Snake Length = " + str(INIT_SNAKE_LEN),
                       (screen.get_width()//2, 50), None, 30, WHITE)

    # A snake is a group of Segment sprites, evenly spaced, 
    #    based on a grid of STEP_SIZE pixels per grid position.
    # The snake's head is the sprite at position [0] in the list,
    #    and the tail is the last sprite in the list.
    # The first segment is placed at grid position (5,5), and each 
    #    subsequent segment is placed one grid position farther to the right.
    snakeSegs = []
    for i in range(INIT_SNAKE_LEN) :
        seg = Segment( (STEP_SIZE*(5+i), (STEP_SIZE*5)) )
        snakeSegs.insert(0, seg)  # insert each new segment to the beginning of the list.
    snakeGroup = pygame.sprite.Group(snakeSegs)

    # Once the snake has been made, create an Apple sprite, and choose a random position
    #   that does not collide with the snake
    apple = Apple()
    apple.reposition(snakeGroup)
    otherSprites = pygame.sprite.Group([scoreboard,apple])

    # Set initial snake movement
    dx = STEP_SIZE
    dy = 0

    clock = pygame.time.Clock()
    
    # Initial clock speed is pretty slow, but could be increased as game progresses (higher levels?)
    clockSpeed = INIT_TICK  
    
    keepGoing = True
    paused    = False
    win       = False

    # The game loop:
    while (keepGoing) :

        clock.tick(clockSpeed)  # Slow tick speed used (snake moves one segment per clock tick)

        # The event loop:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                keepGoing = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q :
                    keepGoing = False
                elif event.key == pygame.K_p :  # Pause
                    paused = not paused
                # Arrow keys dictate where the next snake segment will appear on next clock tick
                elif event.key == pygame.K_LEFT :
                    dx = -STEP_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT :
                    dx = STEP_SIZE
                    dy = 0
                elif event.key == pygame.K_UP :
                    dx = 0
                    dy = -STEP_SIZE
                elif event.key == pygame.K_DOWN :
                    dx = 0
                    dy = STEP_SIZE

        if not paused :
            # Make the snake "move" by adding a new first segment and deleting the last segment
            head = Segment( ((snakeSegs[0].rect.centerx + dx), (snakeSegs[0].rect.centery + dy)) )

            # Check to see if we have lost:
            if  pygame.sprite.spritecollide(head,snakeGroup, False):
                keepGoing = False
            else :
                # It's not colliding, so insert the new head segment at the front of the snake (position [0]).
                snakeSegs.insert(0, head)  # snakeSegs is a Python list
                snakeGroup.add(head)       # snakeGroup is a Pygame group
            if head.rect.centerx >= screen.get_width() or head.rect.centerx <= 0 or head.rect.centery >= screen.get_height() or head.rect.centery <= 0:
                keepGoing = False
            if (pygame.sprite.spritecollide(apple, snakeGroup, False)) :      # Ate an apple!
                apple.reposition(snakeGroup)                   # Move apple and let snake keep its tail
                scoreboard.text = "Snake Length = " + str(len(snakeSegs))     # Snake is one seg longer
            else :
                tail = snakeSegs.pop()                         # Regular move; remove the tail segment
                snakeGroup.remove(tail)
                
            if len(snakeSegs) >= WIN_SNAKE_LEN :               # Did we reach the goal?
                keepGoing = False
                win = True
                
            snakeGroup.clear(screen,background)
            otherSprites.clear(screen,background)
            
            snakeGroup.update()
            otherSprites.update()
            
            snakeGroup.draw(screen)
            otherSprites.draw(screen)
            
            pygame.display.flip()
    
    return win
    
#####################################################################################################
# playAgain asks the obvious question.  Returns a boolean.
def playAgain(winLose):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill( REPLAY_BG )    # Fill the background
    screen.blit(background, (0,0))  # Blit background to screen
    #### Add code here to construct Label sprites that:
    ####    Display a message about whether the player won or lost
    ####    Ask the player if they want to play again
    #### Then add your Label sprites to labelGroup
    if winLose:
        won = Label("You WIN!",(screen.get_width()//2,screen.get_height()//2),"fonts/DejaVuSans-Bold.ttf",24,GREEN)
        won2 = Label("Do you want to play again (y/n)",(screen.get_width()//2,screen.get_height()//2 + 50),"fonts/DejaVuSans-Bold.ttf",24,ORANGE)
        label = [won,won2]
    else:
        lost = Label("You Lost :( you were "+ str(WIN_SNAKE_LEN-INIT_SNAKE_LEN) + " Apples away from winning!", (screen.get_width() // 2, screen.get_height() // 2),"fonts/DejaVuSans-Bold.ttf", 24, RED)
        lost2 = Label("Do you want to play again (y/n)",(screen.get_width() // 2, screen.get_height() // 2 + 50),"fonts/DejaVuSans-Bold.ttf", 24, ORANGE)
        label =[lost,lost2]
    labelGroup = pygame.sprite.Group(label)
    clock = pygame.time.Clock()
    keepGoing = True
    replay = False

    while keepGoing:
    
        clock.tick(30)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    keepGoing = False
                elif event.key == pygame.K_y:
                    replay = True
                    keepGoing = False
                elif event.key == pygame.K_n:
                    keepGoing = False
        if pygame.mouse.get_pressed()[0]:
            keepGoing = False
        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()
        
    return replay

#####################################################################################################
# endScreen puts up a final thankyou or credits screen for a short time, and then closes.
def endScreen():
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill( END_BG )       # Fill the background
    screen.blit(background, (0,0))  # Blit background to screen

    #### Add code here:
    #### Construct Label sprites to display two messages and add them to the labelGroup:
    ####    1: a "Good bye" or "Thanks for playing" message
    ####    2: your name
    ####    (Use at least two label sprites for the two messages on this screen)
    thanks = Label("Thanks For Playing!", (screen.get_width()//2,screen.get_height()//2), "fonts/DejaVuSans-Bold.ttf", 24, BROWN)
    creator = Label("A game brought to you by Ben Goldstone!", (screen.get_width()//2, screen.get_height()//2 + 50),"fonts/DejaVuSans-Bold.ttf", 24, BROWN)
    labelGroup = pygame.sprite.Group(thanks,creator)
    clock = pygame.time.Clock()
    keepGoing = True
    frames = 0                  

    while keepGoing:
    
        clock.tick(30)          # Frame rate 30 frames per second.

        frames = frames + 1     # Count the number of frames displayed

        if frames == 60:        # After 2 seconds (= 60 frames) end the message display
            keepGoing = False 

        for event in pygame.event.get():
            # Impatient people can quit earlier by clicking the mouse or pressing any key
            if ( event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN ): 
                keepGoing = False
            if event.type == pygame.QUIT:
                keepGoing = False

        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)

        pygame.display.flip()

#####################################################################################################
# main coordinates everything
def main():
    
    titleScreen()

    replay = True

    while(replay):
        outcome = game()
        replay = playAgain(outcome)
    endScreen()

# Kick it off!
main()

# Clean it up
pygame.quit()

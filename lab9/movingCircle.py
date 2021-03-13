# movingCircle.py - for CSI-102 Lab 9: More practice with Pygame
# Adds colors and user interaction
#
# Name: Ben Goldstone
# Date: 10/20/2020


#INITIALIZE:
import pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BOX_SIZE = 100
HALF_BOX = BOX_SIZE // 2
SPEED = 5

# Color Constants
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
MAGENTA = (255, 0, 255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
#BG Colors
BG_COLOR = (200, 200, 200)



def main() :
    #DISPLAY:
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption("Ben Goldstone")
    
    #ENTITIES:
    # A solid color background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill( BG_COLOR )
    
    # A surface on which to draw our shape
    box = pygame.Surface( (BOX_SIZE, BOX_SIZE) )  # Size of box in pixels
    box = box.convert()
    box.fill( BG_COLOR )
    
    # Draw a magenta circle on the box
    pygame.draw.circle(box, MAGENTA, (HALF_BOX, HALF_BOX), HALF_BOX, 10)
    
    #ACTION:
    
    #ASSIGN: 
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Set up initial box location and motion
    boxLeft = 0
    boxTop = 200
    dx = SPEED
    dy = 0

    #LOOP:
    while keepGoing:       # The Game Loop
    
        #TIME:
        clock.tick(30)     # refresh screen this many times per second
    
        #EVENTS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User closed the window
                keepGoing = False

            # On KEYDOWN, determine which key was pressed:
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    keepGoing = False

                elif event.key == pygame.K_r:
                    pygame.draw.circle(box, RED, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_g:
                    pygame.draw.circle(box, GREEN, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_b:
                    pygame.draw.circle(box, BLUE, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_c:
                    pygame.draw.circle(box, CYAN, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_m:
                    pygame.draw.circle(box, MAGENTA, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_y:
                    pygame.draw.circle(box, YELLOW, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_k:
                    pygame.draw.circle(box, BLACK, (HALF_BOX, HALF_BOX), HALF_BOX, 10)

                elif event.key == pygame.K_w:
                    pygame.draw.circle(box, WHITE, (HALF_BOX, HALF_BOX), HALF_BOX, 10)
                # Respond to arrow keys:
                elif event.key == pygame.K_RIGHT: # add speed rightwards
                    dx += SPEED

                elif event.key == pygame.K_LEFT:  # add speed leftwards
                    dx -= SPEED

                elif event.key == pygame.K_UP: # add speed upwards
                    dy -= SPEED
                elif event.key == pygame.K_DOWN:  # add speed downwards
                    dy += SPEED
            #if (dx !=0 or dy != 0) and event.type == pygame.MOUSEBUTTONDOWN and boxLeft < pygame.mouse.get_pos()[0] < boxLeft + BOX_SIZE and boxTop < pygame.mouse.get_pos()[1] < boxTop - BOX_SIZE:
                    #print("Cprrect")
 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Stop the box motion
                dx = 0
                dy = 0
        # Move box by changing its location based on current values of dx and dy
        boxLeft += dx
        boxTop  += dy
        
        # Check to see if the box has exceeded any boundaries; if so, wrap around
        if boxLeft >= screen.get_width():   # If box has exceeded the right edge,
            boxLeft = -BOX_SIZE             #  move it back to just beyond the left edge
    
        elif boxLeft + BOX_SIZE <= 0:       # If box has exceeded the left edge,
            boxLeft = screen.get_width()    #  move it back to just beyond the right edge

        if boxTop >= screen.get_height():  # If box has exceeded the right edge,
            boxTop = -BOX_SIZE  # move it back to just beyond the left edge

        elif boxTop + BOX_SIZE <= 0:  # If box has exceeded the left edge,
            boxTop = screen.get_height()  # move it back to just beyond the right edge
        
            

    
        #REFRESH SCREEN:
        screen.blit(background, (0, 0))   # redraw the clean background to erase the old box position
        screen.blit(box, (boxLeft, boxTop))   # 'blit' the box at its new position
        pygame.display.flip()             # swap the double-buffered screen

# Start it running
main()

# Clean up after main() finishes
pygame.quit()

# 8_bouncingBall.py
#
# Modified by: Ben Goldstone
# Date: 10/13/2020
#
# A simple ball-in-a-box game. 

# Initialize pygame
import pygame
pygame.init()

# Constants
WIDTH  = 800
HEIGHT = 600
BOX_SIZE = 100

# Construct a screen - WIDTH x HEIGHT pixels (origin at upper-left)
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption("Ben Goldstone")

def main():

    # Construct a yellow background surface the same size as the screen.
    background = pygame.Surface(screen.get_size())  # Construct background
    background = background.convert()               # Convert graphics format.
    background.fill( (255,255,0) )                  # Fill with color. (255,255,0) is yellow.

    # Now construct a box to move on the screen.
    box = pygame.Surface( (BOX_SIZE,BOX_SIZE) )     # Construct a square surface.
    box = box.convert()                             # Convert graphics format.
    box.fill( (255,255,0) )                         # Fill with color. (Same color as background)

    # Draw a circle on the box object.
    halfBox = BOX_SIZE // 2  # Integer division, so no fractional answers
    pygame.draw.circle(box, (255, 0, 0), (halfBox, halfBox), halfBox, 0)
    #                   ^       ^              ^             ^     ^
    #              object     color    center of circle   radius   0="filled"


    # set up some box variables:
    
    # The initial location of the upper left corner of the box.
    boxLeft = 0       # The initial x-coordinate.
    boxTop  = 0       # The initial y-coordinate.
    # Move this many pixels for each clock tick.
    dx = 10
    dy = 12

    clock = pygame.time.Clock()  # A clock to control the frame rate.
    keepGoing = True             # Signals when the program ends.


    # GAME LOOP:
    while keepGoing:
    
        clock.tick(30)  # Frame rate 30 ticks (frames) per second.

        # EVENT LOOP: Check for events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                background.fill( (0,0,0) )          # (0, 0, 0) is "black"
                box.fill((0, 0, 0))
                pygame.draw.circle(box, (255, 0, 0), (halfBox, halfBox), halfBox, 0)
                print("Ouch!")
            elif event.type == pygame.MOUSEBUTTONUP:
                background.fill( (255,255,0) )      # (255, 255, 0) is "yellow"
                box.fill((255, 255, 0))
                pygame.draw.circle(box, (255, 0, 0), (halfBox, halfBox), halfBox, 0)
                dx = -dx
                dy = -dy
        # Update the box's location by changing its coordinates.
        boxLeft += dx  # move the box horizontally.
        boxTop  += dy  # move the box vertically.
    
        # If the box hits the edge of the screen, reverse its direction
        #    by changing the sign of dx or dy.
        if boxLeft + BOX_SIZE > screen.get_width():
            dx = -1 * abs(dx)                    # Ensure new direction is negative

        if boxLeft < 0:
            dx = abs(dx)                         # Ensure new direction is positive

        if boxTop + BOX_SIZE > screen.get_height():
            dy = -1 * abs(dy)                    # Ensure new direction is negative

        if boxTop < 0:
            dy = abs(dy)                         # Ensure new direction is positive

        # Blit the background to the screen at position (0,0), erasing 
        #  the old position of the box
        screen.blit(background, (0,0))
        
        # Blit the box to the screen at its new (boxLeft, boxTop) coordinates.
        screen.blit(box, (boxLeft, boxTop))  
     
        # Flip the double buffered screen to make the new positions visible.
        pygame.display.flip()  
        
# Call the main() function
main()

# After main() finishes, quit pygame and clean up.  Without this,
#  pygame may never terminate, leaving you sad.
pygame.quit()

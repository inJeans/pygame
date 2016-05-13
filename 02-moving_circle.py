"""Simple pygame script to draw a moving circle

This script will create a blank window with a single coloured circle on
the screen. The circle's position will be updated each frame

Example:
    Simple execution

        $ python 02-moving_circle.py
"""

import sys
import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE

pygame.init()

FPS = 30  # Frames per second setting

DISPLAYSURF = pygame.display.set_mode((400, 300))

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CUSTOM = (?, ?, ?)

def main():
    'Main game function'
    pygame.display.set_caption('02 - moving circle')
    fps_clock = pygame.time.Clock()  # Initiate the game clock

    circle_x = 0  # Initialise x position
    circle_y = 0  # Initialise y position

    while True: # main game loop
        check_for_quit()

        DISPLAYSURF.fill("""enter your colour here""")  # Set background colour

        # Update the position of the circle each frame
        circle_x = # Update x position
        circle_y = # Update y position
        pygame.draw.circle(DISPLAYSURF,
                           """circle colour goes here""",
                           (circle_x, circle_y),
                           5,
                           0)

        pygame.display.update()
        fps_clock.tick(FPS)  # Tick the game clock

def check_for_quit():
    """Function to check if the game has been quit.

    This function will get every quit event and exit the game in a safe
    manner. It will also exit on and ESC keypress.
    """
    for event in pygame.event.get():
        if event.type == QUIT:  # get all the QUIT events
            terminate() # terminate
            sys.exit()

        if event.type == KEYUP:  # get all the KEYUP events
            if event.key == K_ESCAPE:
                terminate()  # terminate if the KEYUP event was for the Esc key
                pygame.event.post(event)  # put the other KEYUP event objects back

def terminate():
    """Function to handle the termination of the game.

    This function will make sure the relevant exit calls have been made.
    """
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

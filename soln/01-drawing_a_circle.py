"""Simple pygame script to draw a circle

This script will create a blank window with a single coloured circle on
the screen.

Example:
    Simple execution

        $ python 01-drawing_a_circle.py
"""

import sys
import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    'Main game function'
    pygame.display.set_caption('01 - drawing a circle')

    while True: # main game loop
        check_for_quit()

        # pygame.draw.circle(Surface, color, pos, radius, width=0)
        pygame.draw.circle(DISPLAYSURF,
                           GREEN,
                           (200, 150),
                           50,
                           0)

        pygame.display.update()

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

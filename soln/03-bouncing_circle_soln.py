"""Simple pygame script to draw a moving circle

This script will create a blank window with a single coloured circle on
the screen. The circle's position will be updated each frame. If the ball
hits the edge of the window it will bounce back.

Example:
    Simple execution

        $ python 03-bouncing_circle.py
"""

import sys
import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

FPS = 30  # Frames per second setting

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Circle properties
RADIUS = 5

def main():
    'Main game function'
    pygame.display.set_caption('03 - bouncing circle')
    fps_clock = pygame.time.Clock()  # Initiate the game clock

    circle_x = 0  # Initialise x position
    circle_y = 0  # Initialise y position

    speed_x = 1  # Set circle x speed
    speed_y = 1  # Set circle y speed

    while True: # main game loop
        check_for_quit()

        # Bounce the circle if needed
        if circle_x > WINDOW_WIDTH-RADIUS or circle_x < 0:
            speed_x = speed_x * -1
        if circle_y > WINDOW_HEIGHT-RADIUS or circle_y < 0:
            speed_y = speed_y * -1

        circle_x += speed_x  # update x position
        circle_y += speed_y  # update y position

        draw_circle(circle_x,
                    circle_y)

        pygame.display.update()
        fps_clock.tick(FPS)  # Tick the game clock

def draw_circle(circle_x,
                circle_y):
    """Draw the circle

    Blank the screen and redraw the circle in a new position.

    Args:
        circle_x (int): x position of the circle
        circle_y (int): y position of the circle
    """
    DISPLAYSURF.fill(BLACK)  # Set background colour

    pygame.draw.circle(DISPLAYSURF,
                       GREEN,
                       (circle_x, circle_y),
                       RADIUS,
                       0)


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

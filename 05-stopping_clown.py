"""Simple pygame script to draw a moving clown

This script will create a blank window with a single clown on
the screen. The clown's position will be updated each frame. If the clown
hits the edge of the window it will bounce back. When the clown is clicked
it will stop moving. There is no way to restart the clown.

Example:
    Simple execution

        $ python 05-stopping_clown.py
"""

import sys
import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

FPS = 60  # Frames per second setting

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    'Main game function'
    pygame.display.set_caption('05 - stopping clown')
    fps_clock = pygame.time.Clock()  # Initiate the game clock

    clown_x = 0  # Initialise x position
    clown_y = 0  # Initialise y position

    speed_x = 1  # Set clown x speed
    speed_y = 1  # Set clown y speed

    clown_img = pygame.image.load('krusty.png')  # load clown image

    while True: # main game loop
        check_for_quit()

        speed_x, speed_y = bounce_clown(clown_img,
                                        clown_x,
                                        clown_y,
                                        speed_x,
                                        speed_y)

        speed_x, speed_y = mouse_click(clown_img,
                                       clown_x,
                                       clown_y,
                                       speed_x,
                                       speed_y)

        clown_x += speed_x
        clown_y += speed_y

        draw_clown(clown_img,
                   clown_x,
                   clown_y)

        pygame.display.update()
        fps_clock.tick(FPS)  # Tick the game clock

def mouse_click(clown_img,
                clown_x,
                clown_y,
                speed_x,
                speed_y):
    """Handles mouse clicks.

    This function will check to see if the mouse click was above the clown
    image. If it is, the clown will be stopped i.e. speed_x, speed_y = 0, 0

    Args:
        clown_img (pygame.image): instance of a pygame image
        clown_x (int): x position of the clown
        clown_y (int): y position of the clown
        speed_x (int): x speed of the clown
        speed_y (int): y speed of the clown

    Returns:
        (int, int) A new tuple containing the speed in the x and y directions
    """
    clown_width = clown_img.get_rect().width
    clown_height = clown_img.get_rect().height

    for event in pygame.event.get(): #Check the events on the event queue
        if event.type == MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # check if the click is on top of the clown
            # if it is stop the clown from moving

    return speed_x, speed_y


def bounce_clown(clown_img,
                 clown_x,
                 clown_y,
                 speed_x,
                 speed_y):
    """Bounce the clown off the wall.

    Check to see if the clown has collided with the window boundaries. If it
    has then reverse the direction of travel, aka bounce.

    Args:
        clown_img (pygame.image): instance of a pygame image
        clown_x (int): x position of the clown
        clown_y (int): y position of the clown
        speed_x (int): x speed of the clown
        speed_y (int): y speed of the clown

    Returns:
        (int, int) A new tuple containing the speed in the x and y directions.
    """
    clown_width = clown_img.get_rect().width
    clown_height = clown_img.get_rect().height

    if clown_x > WINDOW_WIDTH-clown_width or clown_x < 0:
        speed_x = speed_x * -1
    if clown_y > WINDOW_HEIGHT-clown_height or clown_y < 0:
        speed_y = speed_y * -1

    return speed_x, speed_y


def draw_clown(clown_img,
               clown_x,
               clown_y):
    """Draw the clown

    Blank the screen and redraw the clown in a new position.

    Args:
        clown_img (pygame.image): instance of a pygame image
        clown_x (int): x position of the clown
        clown_y (int): y position of the clown
    """
    DISPLAYSURF.fill(BLACK)  # Set background colour
    DISPLAYSURF.blit(clown_img,
                     (clown_x, clown_y))


def check_for_quit():
    """Function to check if the game has been quit.

    This function will get every quit event and exit the game in a safe
    manner. It will also exit on and ESC keypress.
    """
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate() # terminate
        sys.exit()

    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
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
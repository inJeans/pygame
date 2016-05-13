"""Simple pygame implementation of the catch the clown game.

This script will create a blank window with a single clown on
the screen. The clown's position will be updated each frame. If the clown
hits the edge of the window it will bounce back. When the clown is clicked
it will stop moving. If you click again it will begin moving again. Clicking
on the clown will increase your score by 10.

Example:
    Simple execution

        $ python 07-keeping_score.py
"""

import sys
import random
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

BASICFONTSIZE = 12
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

CLOWN_MOVING = True

def main():
    'Main game function'

    pygame.display.set_caption('07 - keeping score')
    fps_clock = pygame.time.Clock()  # Initiate the game clock

    clown_x = 0  # Initialise x position
    clown_y = 0  # Initialise y position

    speed_x = 1  # Set circle x speed
    speed_y = 1  # Set circle y speed

    clown_img = pygame.image.load('krusty.png')  # load clown image

    score = 0

    while True: # main game loop
        check_for_quit()

        speed_x, speed_y = bounce_clown(clown_img,
                                        clown_x,
                                        clown_y,
                                        speed_x,
                                        speed_y)

        speed_x, speed_y, score = mouse_click(clown_img,
                                              clown_x,
                                              clown_y,
                                              speed_x,
                                              speed_y,
                                              score)

        clown_x += speed_x
        clown_y += speed_y

        draw_scene(clown_img,
                   clown_x,
                   clown_y,
                   score)

        pygame.display.update()
        fps_clock.tick(FPS)  # Tick the game clock

def mouse_click(clown_img,
                clown_x,
                clown_y,
                speed_x,
                speed_y,
                score):
    """Handles mouse clicks.

    This function will check to see if the mouse click was above the clown
    image. If it is, the clown will be stopped i.e. speed_x, speed_y = 0, 0.
    It will also restart the clown if it has been stopped.

    Args:
        clown_img (pygame.image): instance of a pygame image
        clown_x (int): x position of the clown
        clown_y (int): y position of the clown
        speed_x (int): x speed of the clown
        speed_y (int): y speed of the clown
        score (int): a score counter for the game

    Returns:
        (int, int, int) A new tuple containing the speed in the x and y
        directions as well as the score
    """
    global CLOWN_MOVING

    clown_width = clown_img.get_rect().width
    clown_height = clown_img.get_rect().height

    for event in pygame.event.get(): #Check the events on the event queue
        if event.type == MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            if CLOWN_MOVING:
                if (mouse_x > clown_x and mouse_x < clown_x + clown_width
                        and mouse_y > clown_y and mouse_y < clown_y + clown_height):
                    speed_x = 0
                    speed_y = 0
                    CLOWN_MOVING = False
                    score += 10
            else:
                speed_x = random.randint(1, 5)
                speed_y = random.randint(1, 5)
                CLOWN_MOVING = True

    return speed_x, speed_y, score


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


def draw_scene(clown_img,
               clown_x,
               clown_y,
               score):
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

    score_string = "Score: %i" % score
    score_surf, score_rect = makeText(score_string,
                                      """Text colour goes here""",
                                      """Background colour goes here""",
                                      """Window y position goes here""",
                                      """Window x position goes here""")
    DISPLAYSURF.blit(score_surf, 
                     score_rect)

def makeText(text,
             colour,
             bg_colour,
             top,
             left):
    # create the Surface and Rect objects for some text.
    global BASICFONT

    text_surf = BASICFONT.render(text,
                                 True,
                                 colour,
                                 bg_colour)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (top, left)
    
    return text_surf, text_rect

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
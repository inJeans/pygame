"""Simple Hello World pygame script

this script will create a blank window with the title '00 - Hello, World!'.

Example:
    Simple execution

        $ python 00-hello_world.py
"""

import sys
import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

def main():
    'Main game function'
    pygame.display.set_caption('00 - Hello World!')

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()

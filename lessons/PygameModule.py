import pygame

# importing sub-modules
from pygame import Color, rect
from pygame import draw
from pygame import display

# variables
SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('lightblue'))


# show the graphical display on the screen
display.flip()

# wait for user input before closing window
input("Press enter to exit")
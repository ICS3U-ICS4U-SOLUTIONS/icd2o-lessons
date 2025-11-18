import pygame

# importing sub-modules
from pygame import Color, Rect
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

# draw a box for a house
draw.rect(gameDisplay, Color('brown'), Rect(100, 200, 300, 200))

# draw a triangle for a roof
draw.polygon(gameDisplay, Color('black'), [(100, 200), (400, 200), (250, 50)])


# show the graphical display on the screen
display.flip()

# wait for user input before closing window
input("Press enter to exit")
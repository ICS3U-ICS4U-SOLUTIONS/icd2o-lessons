# StraightLineStop.py
# Simple demonstration of pygame animation

import pygame
from pygame import Color
from pygame import draw
from pygame import display
from pygame import time

# Constants and Variables
SCREEN_SIZE = (600, 400)
center_x = 50
center_y = 50

# initialize pygame modules
pygame.init()

# create clock
clock = time.Clock()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# let ball go fixed distance
for i in range(1, 250):
    
    # white background
    gameDisplay.fill(Color('white'))
    
    # draw a ball
    draw.circle(gameDisplay, Color('purple'), (center_x, center_y), 30)
    
    # display graphics
    display.flip()

    # move ball down and to the right every frame
    center_x += 2
    center_y += 1
    
    # delay the program to 45 frames per second
    clock.tick(45)
    
    
    
    


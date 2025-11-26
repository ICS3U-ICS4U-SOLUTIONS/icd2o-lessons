# File Name: BallStraightLine.py

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

# create a clock
clock = time.Clock()

# create a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)
    
while True:
    
    # white background
    gameDisplay.fill(Color('white'))
    
    # draw a ball
    draw.circle(gameDisplay, Color('purple'), (center_x, center_y), 30)
    
    # Display screen for testing
    display.flip()

    # change the location of the ball for next time
    center_x = center_x + 1
    center_y = center_y + 1
    
    # slow down the loop with the clock
    clock.tick(450)

#  Do the following exercises

#  1. Move ball right

#  2. Move ball left

#  3. Move ball up

#  4. Move ball down

#  5. Move ball diagonally from bottom right corner to top left corner

#  6. Move ball diagonally from bottom left corner to top right corner

#  7. Move ball diagonally from top right corner to bottom left corner


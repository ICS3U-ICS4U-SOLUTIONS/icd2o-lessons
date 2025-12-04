# BallBounce.py
# pygame animation using selection statements

import pygame
import random

from pygame import Color
from pygame import draw
from pygame import display
from pygame import time

# constant variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
RADIUS = 30

# variables
center_x = 250
center_y = 250

# change in position of the ball
dx = random.randint(2, 4)
dy = random.randint(2, 4)

# initialize pygame modules
pygame.init()

clock = time.Clock()

# create a surface for graphics display
gameDisplay = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    
    # Does the user want to quit?  (x button on upper right)
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            quit()
            
    # make ball respond to keyboard input
    if evt.type == pygame.KEYDOWN:
    
        # check if down arrow key is pressed
        if evt.key == pygame.K_DOWN:
            dy = random.randint(2, 4)

        # check if up arrow key is pressed    
        elif evt.key == pygame.K_UP:
            dy = -random.randint(2, 4)
            
        # check if left key is pressed
        elif evt.key == pygame.K_LEFT:
            dx = -random.randint(2, 4)
        
        # check if right key is pressed
        elif evt.key == pygame.K_RIGHT:
            dx = random.randint(2, 4)
    
    # white background for gameDisplay
    gameDisplay.fill(Color('white'))
    
    # draw the ball
    draw.circle(gameDisplay, Color('purple'), (center_x, center_y), RADIUS)
    
    # show graphics on the screen
    display.flip()
    
    # check for ball hitting the sides; make it bounce
    if (center_x + RADIUS > SCREEN_WIDTH) or  (center_x - RADIUS < 0 ):
        dx = -dx
    
    # check for ball hitting the top or bottom; make it bounce
    if (center_y + RADIUS > SCREEN_HEIGHT)  or  (center_y - RADIUS < 0) :
        dy = -dy
    
    # get ready to move the ball for the next time
    center_x += dx
    center_y += dy
    
    # delay the program to obtain 45 frames per second
    clock.tick(45)
    


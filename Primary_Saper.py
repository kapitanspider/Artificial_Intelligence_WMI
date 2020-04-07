#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys, random
from objects.Bomb import Bomb
from objects.Saper import Saper
from objects.Wall import Wall
from pygame.locals import *

# Defining the program environment
# list containing the map of the game
saper_map = []

# Define the Frames Per Second setting
FPS = 30
fpsClock = pygame.time.Clock()

# Define window size for the environment to run in
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Define saper coordinates - Those are just arbitrary, the map will decide position
saper_x = 0
saper_y = 0

# Define the coordinates of the saper movement
saper_x_movement = 0
saper_y_movement = 0

# List containing the coordinates of the bombs on the map
dest = []

# List containing the bomb priority and their respective coordinates from the 'dest' list
priority = []


# List of used graphics
Saper_A_image = pygame.image.load("images/saper_A.png")

Bomb_Image = pygame.image.load("images/Bomb.png")  # Instead of Bomb_A

Bomb_Defused = pygame.image.load("images/Bomb_Defused.png")  # Instead of thumbs up

Wall_image = pygame.image.load("images/Wall.png")


# Defining all the functions
# Procedure translating an encoded map from a file to a usable format and adding it to the list of maps
def read_map(file):
    f = open("maps/" + file, "r")
    s = f.read()
    saper_map.append([])
    index = 0
    for i in range(len(s)-1):
        if s[i] == "0":
            saper_map[index].append(None)
        if s[i] == "1":
            saper_map[index].append(Wall())
        if s[i] == "2":
            saper_map[index].append(Saper())
        if s[i] == "3":
            saper_map[index].append(Bomb(random.randint(200, 600), "A"))
        if s[i] == "\n":
            saper_map.append([])
            index = index + 1


# Initialize all the required pygame modules
pygame.init()

# Call the translating function for the specified map
read_map("map1.txt")

# Procedure finding the saper coordinates on the translated map and assigning them to the objects XY coordinates
for i in range(len(saper_map)):
    for j in range(len(saper_map[i])):
        if saper_map[i][j].__class__.__name__ == "Saper":
            saper_x = i
            saper_y = j


# Procedure finding the bomb coordinates and the bomb priority and appending them respectively to the 'dest' list and 'priority' list
for i in range(len(saper_map)):
    for j in range(len(saper_map[i])):
        if saper_map[i][j].__class__.__name__ == "Bomb":
            dest.append([i, j])
            priority.append(saper_map[i][j].priority)

# Set up the graphic environment of the program
GAMEBOARD = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)  # set_mode((size_width, size height), flags, depth)

# Set the window name
pygame.display.set_caption('Autonomiczny Saper')

# Set the background image
background_image = pygame.image.load("images/background.png")

# Set up the flag to check if the saper is done clearing the bombs
saper_done_flag = True

# Control variable for movement operations
game_loop = 0

# Set up the main movement and action loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    GAMEBOARD.blit(background_image, (0, 0))
    for i in range(len(saper_map)):
        for j in range(len(saper_map[i])):
            if saper_map[i][j].__class__.__name__ == "Saper":
                if saper_map[i][j].tool == "A":
                    GAMEBOARD.blit(Saper_A_image, [i*50, j*50])

            elif saper_map[i][j].__class__.__name__ == "Wall":
                GAMEBOARD.blit(Wall_image, [i*50, j*50])

            elif saper_map[i][j].__class__.__name__ == "Bomb":
                if saper_map[i][j].type == "done":
                    GAMEBOARD.blit(Bomb_Defused, [i*50, j*50])

                elif saper_map[i][j].type == "A":
                    GAMEBOARD.blit(Bomb_Image, [i*50, j*50])



    # Refresh the GAMEBOARD screen
    pygame.display.flip()

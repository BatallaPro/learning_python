# IMPORTS
import pygame
import numpy as np
from boards import Pattern



# README
#
# With this short code you can play Conway's Game of Life.
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
# This game is one of the discoveries that led me to dive into Data Science.
# Sadly, Conway passed away last year due to SARS-CoV-2.
# I found a short tutorial to replicate this game and couldnt wait to 
# implement it without too much care or sophistications.
#
# You just have to choose any of the patterns I have created and
# see what happens.
#
# Press SPACE to start/stop the game.
# Click on the X of the pop-up window to exit.
#
# Enjoy. Investigate. Stay safe.



# SELECT PATTERN
# Built-in are: glider, acorn, diehard, cros, v, rock, small_random, full_random
pattern = Pattern()
choosen_pattern = pattern.build('small_random')

# WINDOW BUILDER
# Dimensions
width, height = 800, 800  # px
screen = pygame.display.set_mode((width, height))

# Background
bg = 25, 25, 25  # rgb
screen.fill(bg)

# Title
pygame.display.set_caption("Conway's life game")



# BOARD BUILDER
# Shape
cells_x, cells_y = 150, 150

# Cells dimensions
dim_cells_x = width / cells_x
dim_cells_y = height / cells_y



# INITIAL STATE
# A cell is "dead" if its value is 0
# A cell is "alive" if its value is 1
# States are matrices with 0s and 1s forming known or random patterns
current_state = choosen_pattern



# GAME LOOP
# The game has three states: not initiated, paused (default), not paused
running = True
pause = True

while running:
    next_state = np.copy(current_state)

    screen.fill(bg)

    # Switch / Close
    # This block is used to capture if any key is pressed (switches between
    # paused and not paused) or if X in the window is clicked to stop the game.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            pause = not pause

        if event.type == pygame.QUIT:
            running = False
            break

    # Board iterator
    for x in range(0, cells_x):
        for y in range(0, cells_y):

            if not pause:
            # Neighbourhood calculation. For this game it's usuall to chose the
            # toroidal approach, allowing the array indices to wrap, so that a
            # "spaceship" will go off one edge and appear at the other side (for
            # x or y axis). This is made using the modulus operation and will
            # work for a negative index too.
            # E.G. board limit = 15
            # x + 1 = 15 ---> 15 % 15 = 0
            # from last position (15) next position is 0
                neighbours = current_state[(x - 1) % cells_x, (y - 1) % cells_y] + \
                             current_state[(x    ) % cells_x, (y - 1) % cells_y] + \
                             current_state[(x + 1) % cells_x, (y - 1) % cells_y] + \
                             current_state[(x - 1) % cells_x, (y    ) % cells_y] + \
                             current_state[(x + 1) % cells_x, (y    ) % cells_y] + \
                             current_state[(x - 1) % cells_x, (y + 1) % cells_y] + \
                             current_state[(x    ) % cells_x, (y + 1) % cells_y] + \
                             current_state[(x + 1) % cells_x, (y + 1) % cells_y]

                # 1st rule:
                # One "death cell" with exactly 3 alive neighbours "reborns"

                if current_state[x, y] == 0 and neighbours == 3:
                    next_state[x, y] = 1

                # 2nd rule:
                # One "living cell" with less of two neighbours "dies" of
                # solitude, but if it has more than three it "dies" because
                # of overpopulation

                elif current_state[x, y] == 1 and (neighbours < 2 or neighbours > 3):
                    next_state[x, y] = 0

            # Calculate cell dimensions
            poly = [(dim_cells_x * (x), dim_cells_y * (y)),
                    (dim_cells_x * (x+1), dim_cells_y * (y)),
                    (dim_cells_x * (x+1), dim_cells_y * (y+1)),
                    (dim_cells_x * (x), dim_cells_y * (y+1))]
            
            # Draw cells
            if next_state[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255,255), poly, 0)

    # Update game state
    current_state = np.copy(next_state)

    # Update window
    pygame.display.flip()
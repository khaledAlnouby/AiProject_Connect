import pygame
import sys
import random

# Define some constants
ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)


# adding and Setting up the game board
def set_up_board():
    board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
    return board



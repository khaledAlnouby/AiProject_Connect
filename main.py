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
#-----------------------------------------------------------------------------------------------------------------
# adding the draw_game_board function
def draw_game_board(board):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, BLUE, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


# Make the make_move function
def make_move(board, row, col, piece):
    board[row][col] = piece


# Check if a move is valid
def can_place(board, col):
    return board[ROW_COUNT - 1][col] == 0


# Get the next available row in a given column
def next_available_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


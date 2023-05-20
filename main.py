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
        
 # Check if a player has won
def check_win(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c+ 2] == piece and board[r][c + 3] == piece:
                return True
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check diagonal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


# to Create the game board
board = set_up_board()
game_over = False
turn = 1

# Draw the initial board
# make the nini max algorithm with alpha beta
def minimax_with_alpha_beta(board, depth, alpha, beta, maximizingPlayer):
    valid_cols= [col for col in range(COLUMN_COUNT) if can_place(board, col)]

    # Check if the game has ended or the maximum depth has been reached
    if depth == 0 or len(valid_cols) == 0 or check_win(board, 1) or check_win(board, 2):
        if check_win(board, 2):
            return (None, 100000000000000)
        elif check_win(board, 1):
            return (None, -10000000000000)
        else:
            return (None, 0)

    # If the Computer is maximizing
    if maximizingPlayer:
        value = float('-inf')
        column = random.choice(valid_cols)
        for col in valid_cols:
            row = next_available_row(board, col)
            temp_board = [row[:] for row in board]
            make_move(temp_board, row, col, 2)
            new_score = minimax_with_alpha_beta(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    # If the Computer is minimizing
    else:
        value = float('inf')
        column = random.choice(valid_cols)
        for col in valid_cols:
            row = next_available_row(board, col)
            temp_board =[row[:] for row in board]
            make_move(temp_board, row, col, 1)
            new_score = minimax_with_alpha_beta(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
draw_game_board(board)


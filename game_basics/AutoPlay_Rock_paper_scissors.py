# This is a simple implementation of the classic Snake game using Pygame library in Python using PyGame module
# Script by: MrLunk
# https://github.com/mrlunk 

"""
An example implementation of a game of Rock, Paper, Scissors in Python using Pygame. This version has two automatically
playing players competing against each other, and keeps track of the score above the players.
"""

import pygame
import random

# Set up Pygame
pygame.init()
clock = pygame.time.Clock()

# Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FONT_SIZE = 32

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.SysFont(None, FONT_SIZE)

# Define game elements
ROCK = 0
PAPER = 1
SCISSORS = 2
OPTIONS = [ROCK, PAPER, SCISSORS]
WINNING_MOVES = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}

# Define game variables
player1_score = 0
player2_score = 0

# Set up game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear screen
    window.fill(WHITE)

    # Draw scores
    player1_score_text = font.render(f"Player 1: {player1_score}", True, BLACK)
    player2_score_text = font.render(f"Player 2: {player2_score}", True, BLACK)
    window.blit(player1_score_text, (10, 10))
    window.blit(player2_score_text, (WINDOW_WIDTH - player2_score_text.get_width() - 10, 10))

    # Get player moves
    player1_move = random.choice(OPTIONS)
    player2_move = random.choice(OPTIONS)

    # Determine winner
    if player1_move == player2_move:
        result_text = font.render("Tie!", True, BLACK)
    elif WINNING_MOVES[player1_move] == player2_move:
        result_text = font.render("Player 1 wins!", True, BLACK)
        player1_score += 1
    else:
        result_text = font.render("Player 2 wins!", True, BLACK)
        player2_score += 1

    # Draw moves and result
    rock_image = pygame.image.load("rock.png")
    paper_image = pygame.image.load("paper.png")
    scissors_image = pygame.image.load("scissors.png")
    move_images = {ROCK: rock_image, PAPER: paper_image, SCISSORS: scissors_image}
    window.blit(move_images[player1_move], (50, 100))
    window.blit(move_images[player2_move], (WINDOW_WIDTH - 50 - rock_image.get_width(), 100))
    result_x = (WINDOW_WIDTH - result_text.get_width()) // 2
    result_y = (WINDOW_HEIGHT - result_text.get_height()) // 2
    window.blit(result_text, (result_x, result_y))

    # Update screen
    pygame.display.update()

    # Wait for a short time to make the game more playable
    pygame.time.wait(500)

    # Limit the frame rate
    clock.tick(60)

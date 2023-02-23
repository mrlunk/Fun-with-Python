"""
This code sets up the game window, initializes the grid of cells with random live/dead values, defines a function to count live neighbors, and implements the main game loop that updates the grid and draws the cells on the screen.
 
The simulation features a grid of cells that can be either alive or dead, and updates based on the following rules:
 
    If a cell is alive and has fewer than two live neighbors, it dies (underpopulation).
    If a cell is alive and has two or three live neighbors, it continues to live.
    If a cell is alive and has more than three live neighbors, it dies (overpopulation).
    If a cell is dead and has exactly three live neighbors, it becomes alive (reproduction).
 
First, you'll need to install Pygame by running 'pip install pygame' in your terminal.

Script by: MrLunk
https://github.com/mrlunk/

"""
 
import pygame
import random
 
# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL_SIZE = 10
ROWS = WINDOW_HEIGHT // CELL_SIZE
COLS = WINDOW_WIDTH // CELL_SIZE
 
pygame.init()
pygame.display.set_caption("Life Simulation")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
# Initialize the grid of cells
grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
 
# Define a function to count the number of live neighbors of a given cell
def count_live_neighbors(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0) and 0 <= row + i < ROWS and 0 <= col + j < COLS:
                count += grid[row + i][col + j]
    return count
 
# Define the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
    # Update the grid
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            live_neighbors = count_live_neighbors(row, col)
            if grid[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[row][col] = 0
            elif grid[row][col] == 0 and live_neighbors == 3:
                new_grid[row][col] = 1
            else:
                new_grid[row][col] = grid[row][col]
    grid = new_grid
 
    # Draw the cells on the screen
    window.fill((255, 255, 255))
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(window, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

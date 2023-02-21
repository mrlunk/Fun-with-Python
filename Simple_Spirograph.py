# Script by: MrLunk
# https://github.com/mrlunk/

import pygame
import math
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the scale and the line width
scale = 0.3
line_width = 2

# Set the initial values for the angles
theta1 = 0
theta2 = 0
theta3 = 0

# Set the initial values for the wheel radii
R1 = random.randint(5, 250)
R2 = random.randint(5, 250)
R3 = random.randint(5, 250)

# Set the time interval for generating new random wheel sizes
GENERATE_NEW_SIZES_INTERVAL = 5000  # milliseconds

# Set the initial time for generating new random wheel sizes
next_generate_new_sizes_time = pygame.time.get_ticks() + GENERATE_NEW_SIZES_INTERVAL

# Start the loop for drawing the spirograph
running = True
while running:

    # Clear the screen
    screen.fill(WHITE)

    # Set the coordinates for the center of the screen
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Draw the wheels
    # pygame.draw.circle(screen, BLACK, (center_x, center_y), R1, line_width)
    # pygame.draw.circle(screen, BLACK, (int(center_x + (R1 + R2)), center_y), R2, line_width)
    # pygame.draw.circle(screen, BLACK, (int(center_x + (R1 + R2) + R3), center_y), R3, line_width)

    # Calculate the spirograph coordinates and draw the lines
    for i in range(250):
        x = int(center_x + (R1 + R2) * math.cos(theta1) + R3 * math.cos(theta3))
        y = int(center_y + (R1 + R2) * math.sin(theta1) + R3 * math.sin(theta3))
        theta1 += scale
        theta2 += scale * (R1 / R2)
        theta3 += scale * (R2 / R3)
        if i == 0:
            old_x, old_y = x, y
        pygame.draw.line(screen, BLACK, (old_x, old_y), (x, y), line_width)
        old_x, old_y = x, y

    # Generate new random wheel sizes if the time has come
    if pygame.time.get_ticks() >= next_generate_new_sizes_time:
        R1 = random.randint(50, 150)
        R2 = random.randint(50, 150)
        R3 = random.randint(50, 150)
        next_generate_new_sizes_time += GENERATE_NEW_SIZES_INTERVAL

    # Update the screen
    pygame.display.flip()

    # Exit the loop if the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()




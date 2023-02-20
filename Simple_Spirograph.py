# Script by: MrLunk
# https://github.com/mrlunk/

import pygame
import math

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the parameters for the spirograph
R1 = int(input("Enter the radius of the first wheel: "))
R2 = int(input("Enter the radius of the second wheel: "))
R3 = int(input("Enter the radius of the third wheel: "))
P = int(input("Enter the number of points to draw: "))
K = float(R2 / R1)

# Set the scale and the line width
scale = 0.3
line_width = 1

# Set the initial values for the angles
theta1 = 0
theta2 = 0
theta3 = 0

# Start the loop for drawing the spirograph
running = True
while running:

    # Clear the screen
    screen.fill(WHITE)

    # Set the coordinates for the center of the screen
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Calculate the spirograph coordinates and draw the lines
    for i in range(P):
        x = int(center_x + (R1 + R2) * math.cos(theta1) + R3 * math.cos(theta3))
        y = int(center_y + (R1 + R2) * math.sin(theta1) + R3 * math.sin(theta3))
        theta1 += scale
        theta2 += scale * K
        theta3 += scale * (R2 / R3)
        if i == 0:
            old_x, old_y = x, y
        pygame.draw.line(screen, BLACK, (old_x, old_y), (x, y), line_width)
        old_x, old_y = x, y

    # Update the screen
    pygame.display.flip()

    # Exit the loop if the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

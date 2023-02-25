# This is a simple implementation of the classic Snake game using Pygame library in Python using PyGame module
# Script by: MrLunk
# https://github.com/mrlunk 

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the Snake class
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = "right"
        self.body = []
        self.length = 1
        
    def move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
        
        if len(self.body) > self.length - 1:
            self.body.pop(0)
            
        self.body.append((self.x, self.y))
    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(window, black, [block[0], block[1], 10, 10])
        
    def eat_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            self.length += 1
            return True
        else:
            return False

# Define the Food class
class Food:
    def __init__(self):
        self.x = round(random.randrange(0, window_width - 10) / 10.0) * 10.0
        self.y = round(random.randrange(0, window_height - 10) / 10.0) * 10.0
        
    def draw(self):
        pygame.draw.rect(window, red, [self.x, self.y, 10, 10])

# Create the Snake and Food objects
snake = Snake(250, 250)
food = Food()

# Set up the game loop
game_over = False
clock = pygame.time.Clock()
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = "up"
            elif event.key == pygame.K_DOWN:
                snake.direction = "down"
            elif event.key == pygame.K_LEFT:
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT:
                snake.direction = "right"
                
    # Move the Snake
    snake.move()
    
    # Check if the Snake has hit the edges of the window
    if snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height:
        game_over = True
    
    # Check if the Snake has collided with itself
    for block in snake.body[:-1]:
        if block == (snake.x, snake.y):
            game_over = True
    
    # Check if the Snake has eaten the Food
    if snake.eat_food(food.x, food.y):
        food = Food()
    
    # Draw the Snake and Food
    window.fill(white)
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit

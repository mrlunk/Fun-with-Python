# A Python script containing the basics for a life simulation with 3 competing lifeforms and food items...
# for Edu purposes ;)
# https://en.wikipedia.org/wiki/Life_simulation_game
# File : Three_lifeForms_and_food.py 
# Script by: MrLunk
# https://github.com/mrlunk/

"""
This script is a basic simulation of three competing life forms and food items using the Pygame library in Python. It simulates the interactions and behaviors of the life forms in a two-dimensional environment.
"""

import pygame
import random

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Set the width and height of the screen
WIDTH = 1000
HEIGHT = 1000

# Define the life form class
class LifeForm(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.energy = 200
        self.speed = self.energy / 40
        self.image = pygame.Surface([10, 10]) # -------------------------
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, food_group, life_group):
        self.energy -= 1
        
        # Move towards food or other life forms of a different color
        targets = []
        for life in life_group:
            if life.color != self.color:
                distance = ((life.rect.x - self.rect.x) ** 2 + (life.rect.y - self.rect.y) ** 2) ** 0.5
                if distance < 650:
                    targets.append(life)
        for food in food_group:
            distance = ((food.rect.x - self.rect.x) ** 2 + (food.rect.y - self.rect.y) ** 2) ** 0.5
            if distance < 50:
                targets.append(food)
        
        if len(targets) > 0:
            target = min(targets, key=lambda t: ((t.rect.x - self.rect.x) ** 2 + (t.rect.y - self.rect.y) ** 2) ** 0.5)
            dx = target.rect.x - self.rect.x
            dy = target.rect.y - self.rect.y
            distance = ((dx ** 2) + (dy ** 2)) ** 0.5
            if distance > 0:
                self.rect.x += int((dx / distance) * self.speed)
                self.rect.y += int((dy / distance) * self.speed)
                
                # If the life form is close enough to food, eat it
                if isinstance(target, Food) and distance < 20:
                    self.energy += 25
                    target.kill()
                
                # If the life form is close enough to a life form of a different color, fight it
                elif isinstance(target, LifeForm) and target.color != self.color and distance < 20:
                    if self.energy > target.energy:
                        self.energy += target.energy
                        target.kill()
                    else:
                        target.energy += self.energy
                        self.kill()
        
        # Die if energy is too low
        if self.energy < 0:
            self.kill()

# Define the food class
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = GREEN

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Set the title of the window
pygame.display.set_caption('Life Simulation')

# Create groups for the sprites
all_sprites_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()
red_group = pygame.sprite.Group()
blue_group = pygame.sprite.Group()
yellow_group = pygame.sprite.Group()

# Create some initial life forms and food
LifeFormsAmount = 10
FoodItems = 3000

for i in range(LifeFormsAmount ):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    life_form = LifeForm(RED, x, y)
    all_sprites_group.add(life_form)
    red_group.add(life_form)
for i in range(LifeFormsAmount ):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    life_form = LifeForm(BLUE, x, y)
    all_sprites_group.add(life_form)
    blue_group.add(life_form)
for i in range(LifeFormsAmount ):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    life_form = LifeForm(YELLOW, x, y)
    all_sprites_group.add(life_form)
    yellow_group.add(life_form)
for i in range(FoodItems ): 
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    food = Food(x, y)
    all_sprites_group.add(food)
    food_group.add(food)

# Start the game loop
clock = pygame.time.Clock()
done = False

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Update the sprites
    all_sprites_group.update(food_group, all_sprites_group)
    
    # Draw everything
    screen.fill(WHITE)
    all_sprites_group.draw(screen)
    pygame.display.flip()
    
    # Set the framerate
    clock.tick(30)

# Quit Pygame
pygame.quit()


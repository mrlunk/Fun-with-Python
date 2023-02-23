# A Python script containing the basics for a life simulation with 3 competing lifeforms and food items...
# for Edu purposes ;)
# https://en.wikipedia.org/wiki/Life_simulation_game
# File : 3LifeForms_food_and_replication.py
# Script by: MrLunk
# https://github.com/mrlunk/
# pip install pygame 

import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set the dimensions of the screen
WIDTH = 1000
HEIGHT = 1000

# Set the initial energy of the lifeforms
INITIAL_ENERGY = 50

# Define the lifeforms class
class LifeForm(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.energy = INITIAL_ENERGY
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 2
        self.strength = 2
        
    def update(self):
        # Move towards nearest food item or enemy
        target = self.find_target()
        if target:
            self.move_towards(target)
        
        # Check for collisions with food or other lifeforms
        collisions = pygame.sprite.spritecollide(self, all_sprites, False)
        for sprite in collisions:
            if isinstance(sprite, Food):
                self.energy += 10
                sprite.kill()
            elif isinstance(sprite, LifeForm) and sprite.color != self.color:
                if self.energy > sprite.energy:
                    self.energy += sprite.energy
                    sprite.kill()
                elif self.energy < sprite.energy:
                    sprite.energy += self.energy
                    self.kill()
                else:
                    self.kill()
                    sprite.kill()
        
        # Check for duplication
        if self.energy >= INITIAL_ENERGY * 4: # ------------------------------------------------- 3
            self.energy -= INITIAL_ENERGY
            new_lifeform = LifeForm(self.color)
            new_lifeform.rect.x = self.rect.x + random.randint(-20, 20)
            new_lifeform.rect.y = self.rect.y + random.randint(-20, 20)
            all_sprites.add(new_lifeform)
            lifeforms.add(new_lifeform)
        
        # Update speed and strength based on energy
        self.speed = 2 + (self.energy - INITIAL_ENERGY) // 10
        if self.speed > 10:
            self.speed == 10
        self.strength = 2 + (self.energy - INITIAL_ENERGY) // 20
        if self.strength > 16:
            self.strength == 16
        
    def find_target(self):
        # Find the nearest food item or enemy
        targets = []
        for sprite in all_sprites:
            if isinstance(sprite, Food):
                targets.append(sprite)
            elif isinstance(sprite, LifeForm) and sprite.color != self.color:
                targets.append(sprite)
        if targets:
            distances = [math.sqrt((target.rect.x - self.rect.x)**2 + (target.rect.y - self.rect.y)**2) for target in targets]
            index = distances.index(min(distances))
            return targets[index]
        else:
            return None
        
    def move_towards(self, target):
        # Move towards the target
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
        
            # Check for collisions with the edges of the screen
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > WIDTH - 20:
                self.rect.x = WIDTH - 20
            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y > HEIGHT - 20:
                self.rect.y = HEIGHT - 20

# Define the food class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()    
        self.image = pygame.Surface([5, 5]) # ----------------------------------------------- 2
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(0, HEIGHT - 20)
        
# Initialize Pygame
pygame.init()

# Set the title of the window
pygame.display.set_caption("Life Simulation")

# Set the size of the window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Create groups for all sprites and lifeforms
all_sprites = pygame.sprite.Group()
lifeforms = pygame.sprite.Group()

# Create the lifeforms
red_lifeform = LifeForm(RED)
red_lifeform.rect.x = 100
red_lifeform.rect.y = 100
all_sprites.add(red_lifeform)
lifeforms.add(red_lifeform)

blue_lifeform = LifeForm(BLUE)
blue_lifeform.rect.x = 900
blue_lifeform.rect.y = 100
all_sprites.add(blue_lifeform)
lifeforms.add(blue_lifeform)

yellow_lifeform = LifeForm(YELLOW)
yellow_lifeform.rect.x = 500
yellow_lifeform.rect.y = 900
all_sprites.add(yellow_lifeform)
lifeforms.add(yellow_lifeform)

# Create the food items
for i in range(4000): # ------------------------------------------------------------
    food = Food()
    all_sprites.add(food)

# Set the clock for the game
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update all sprites
    all_sprites.update()
    
    # Draw all sprites
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Update the screen
    pygame.display.flip()
    
    # Set the FPS of the game
    clock.tick(12)

# Quit Pygame
pygame.quit()

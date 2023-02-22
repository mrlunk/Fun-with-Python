import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player
player_image = pygame.image.load("player.png")
player_width = 64
player_height = 64
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10
player_speed = 5

# Set up the bullets
bullet_image = pygame.image.load("bullet.png")
bullet_width = 8
bullet_height = 16
bullet_speed = 10
bullets = []

# Set up the enemies
enemy_image = pygame.image.load("enemy.png")
enemy_width = 64
enemy_height = 64
enemy_speed = 2
enemies = []
for i in range(6):
    enemy_x = 100 + i * 125
    enemy_y = 50
    enemies.append([enemy_x, enemy_y])

# Set up the game over text
game_over_font = pygame.font.SysFont(None, 64)

# Set up the score
score = 0
score_font = pygame.font.SysFont(None, 32)

# Set up the game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width / 2 - bullet_width / 2
                bullet_y = player_y - bullet_height
                bullets.append([bullet_x, bullet_y])

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Remove bullets that have gone off-screen
    bullets = [bullet for bullet in bullets if bullet[1] > -bullet_height]

    # Move the enemies
    for enemy in enemies:
        enemy[0] += enemy_speed
        if enemy[0] < 0 or enemy[0] > screen_width - enemy_width:
            enemy_speed = -enemy_speed
            for enemy in enemies:
                enemy[1] += enemy_height
        if enemy[1] > player_y:
            game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, ((screen_width - game_over_text.get_width()) / 2, (screen_height - game_over_text.get_height()) / 2))
            pygame.display.update()
            pygame.time.delay(3000)
            game_running = False

    # Check for bullet-enemy collisions
    for bullet in bullets:
        for enemy in enemies:
            if bullet[0] < enemy[0] + enemy_width and bullet[0] + bullet_width > enemy[0] and bullet[1] < enemy[1] + enemy_height and bullet[1] + bullet_height > enemy[1]:
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_x, player_y))
    for bullet in bullets:
        screen.blit(bullet_image, (bullet[0], bullet[1]))
    for enemy in enemies:
        screen.blit(enemy_image, (enemy[0], enemy[1]))
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # Update the game clock
    clock.tick(60)

# Quit Pygame
pygame.quit()

# A python script by: MrLunk
# https://github.com/mrlunk/

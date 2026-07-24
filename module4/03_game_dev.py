"""
LESSON 3: Game Development with Pygame
Pygame manages game loops, graphic windows, events, and player inputs.
"""

import pygame
import sys

# Initialize Pygame modules
pygame.init()

# Window dimensions & colors
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 4: Pygame Square Move")

clock = pygame.time.Clock()

# Player square variables
x, y = 280, 180
SPEED = 5
SQUARE_SIZE = 40

# --- Main Game Loop ---
running = True
while running:
    # 1. Event Handling (keyboard clicks, exit events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Movement Inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= SPEED
    if keys[pygame.K_RIGHT] and x < WIDTH - SQUARE_SIZE:
        x += SPEED
    if keys[pygame.K_UP] and y > 0:
        y -= SPEED
    if keys[pygame.K_DOWN] and y < HEIGHT - SQUARE_SIZE:
        y += SPEED

    # 3. Drawing to Screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    
    pygame.display.flip()  # Update display surface
    clock.tick(60)        # Limit frame rate to 60 FPS

pygame.quit()
sys.exit()

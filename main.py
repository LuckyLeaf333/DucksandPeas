import pygame
import Button
import tkinter as tk
import Game

# Window size constants
WIN_WIDTH = 820
WIN_HEIGHT = 480

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Sets window size
running = True

# Create the clock
clock = pygame.time.Clock()

# Create Game object to manage the game
game = Game.Game(screen, WIN_WIDTH, WIN_HEIGHT)
game.start_init()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    game.screen_update()
    pygame.display.flip()

    # Ensure program maintains a rate of 6 frames per second
    clock.tick(5)

pygame.quit()

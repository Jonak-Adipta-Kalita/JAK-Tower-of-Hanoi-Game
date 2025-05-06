import pygame
import sys

bg_color = (255, 255, 255)
width, height = 1080, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JAK Tower of Hanoi Game")
screen.fill(bg_color)

pygame.display.flip()

game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

pygame.quit()
sys.exit()

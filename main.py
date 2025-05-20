from src.game import Game
from src.constants import DIMENSIONS, GRAY_COLOR
from src.ui import draw_init_screen

import pygame
import sys

game_loop = True

pygame.init()
game = Game()

screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption("JAK Tower of Hanoi Game")

clock = pygame.time.Clock()
dt = 0

background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, DIMENSIONS)

font = pygame.font.SysFont("Comic Sans MS", 48)

while game_loop:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    if game.did_win():
        win_text = font.render(
            f"You win in {game.moves} Moves!", True, GRAY_COLOR)
        text_rect = win_text.get_rect(
            center=(DIMENSIONS[0]/2, DIMENSIONS[1]/2))
        screen.blit(win_text, text_rect)
    else:
        draw_init_screen(screen, len(game.towers[0].rings))
        # game.perform_operation(str(input(">> ")))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()

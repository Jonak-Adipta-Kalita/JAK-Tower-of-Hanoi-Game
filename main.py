from src.game import Game
from src.constants import DIMENSIONS
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

while game_loop:
    draw_init_screen(screen, background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # try:
    #     game.print_status()
    #     print()
    #
    #     if game.did_win():
    #         print(f"You win in {game.moves} Moves!")
    #         del game
    #         game_loop = False
    #     else:
    #         game.perform_operation(str(input(">> ")))
    #         print()
    # except Exception:
    #     print("ばか がいじん")
    #     print()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()

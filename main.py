from src.game import Game
from src.constants import DIMENSIONS, GRAY_COLOR
from src.ui import draw_ui
from src.db import Database

import pygame
import sys

print()
database = Database()
database.login_or_register()
print()
print("Enjoy the Game!")

game_loop = True

pygame.init()
game = Game(database)

screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption("JAK Tower of Hanoi Game")

clock = pygame.time.Clock()
dt = 0

background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, DIMENSIONS)

font = pygame.font.SysFont("Comic Sans MS", 30)

while game_loop:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            database.close_db()
            game_loop = False

        if (event.type == pygame.KEYDOWN
            and event.key in [pygame.K_1, pygame.K_2, pygame.K_3]
                and not game.has_inputs()):
            game.show_error = False
            game.selected_towers.append(event.unicode)

    if game.did_win():
        game.store_highscore()
        win_text = font.render(
            f"You win in {game.moves} Moves!", True, GRAY_COLOR)
        text_rect = win_text.get_rect(
            center=(DIMENSIONS[0]/2, DIMENSIONS[1]/2))
        screen.blit(win_text, text_rect)
    else:
        draw_ui(screen, game, font)

        if game.show_error:
            error_text = font.render("Invalid Move", True, GRAY_COLOR)
            text_rect = error_text.get_rect(
                center=(DIMENSIONS[0]/2, DIMENSIONS[1] * 3.5/4))
            screen.blit(error_text, text_rect)

        if game.has_inputs():
            game.show_error = False
            game.perform_operation()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()
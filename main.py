from src.game import Game
# import pygame
# import sys

bg_color = (255, 255, 255)
width, height = 1080, 720
game_loop = True

game = Game()

# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("JAK Tower of Hanoi Game")
# screen.fill(bg_color)

# clock = pygame.time.Clock()

while game_loop:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         game_loop = False

    try:
        game.print_status()
        print()

        if game.did_win():
            print(f"You win in {game.moves} Moves!")
            game_loop = False
        else:
            game.perform_operation(str(input(">> ")))
            print()
    except Exception:
        print("ばか がいじん")
        print()

    # pygame.display.flip()
    # clock.tick(60)

# pygame.quit()
# sys.exit()

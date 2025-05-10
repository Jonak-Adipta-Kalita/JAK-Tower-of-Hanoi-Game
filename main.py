from src.tower import Tower, Organizer

# import pygame
# import sys

bg_color = (255, 255, 255)
width, height = 1080, 720
game_loop = True

tower1 = Tower([0, 1, 2])
tower2 = Tower([])
tower3 = Tower([])

organizer = Organizer(tower1=tower1, tower2=tower2, tower3=tower3)

# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("JAK Tower of Hanoi Game")
# screen.fill(bg_color)

# clock = pygame.time.Clock()


def get_operation(operator):
    towers = operator.strip().split("->")

    remove_tower = organizer.get(towers[0])
    add_tower = organizer.get(towers[1])

    if remove_tower == add_tower:
        raise Exception()

    if add_tower.top is not None and add_tower.top > remove_tower.top:
        raise Exception("lmao")

    popped_ring = remove_tower.pop()
    add_tower.push(popped_ring)


while game_loop:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         game_loop = False

    try:
        print(f"Tower 1: {tower1}")
        print(f"Tower 2: {tower2}")
        print(f"Tower 3: {tower3}")
        print()

        if tower3.rings == [0, 1, 2]:
            print("You win!")
            game_loop = False
        else:
            get_operation(str(input(">> ")))
            print()
    except Exception:
        print("ばか がいじん")
        print()

    # pygame.display.flip()
    # clock.tick(60)

# pygame.quit()
# sys.exit()

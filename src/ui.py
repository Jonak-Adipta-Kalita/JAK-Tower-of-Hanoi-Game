from src.constants import GRAY_COLOR, DIMENSIONS, RING_HIERARCHY
from src.utils import section_formula, distance_formula
from src.game import Game
import pygame

width, height = DIMENSIONS

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))

tower_height_i = bl_pos[0][1] * 1/3
tower1_width = section_formula(bl_pos[0][0], width / 2, 1, 2)
tower2_width = width / 2
tower3_width = section_formula(width / 2, bl_pos[1][0], 2, 1)

tower1_pos = ((tower1_width, tower_height_i), (tower1_width, bl_pos[1][1]))
tower2_pos = ((tower2_width, tower_height_i), (tower2_width, bl_pos[1][1]))
tower3_pos = ((tower3_width, tower_height_i), (tower3_width, bl_pos[1][1]))

mid_points = [tower1_pos[1], tower2_pos[1], tower3_pos[1]]


def draw_ring(screen, ring_size: int, mid_point: tuple) -> tuple:
    height = RING_HIERARCHY[ring_size]["height"]
    color = RING_HIERARCHY[ring_size]["color"]
    ring_length = RING_HIERARCHY[ring_size]["ring_length"]

    i = (mid_point[0]-ring_length, mid_point[1]-2)
    f = (mid_point[0]+ring_length, mid_point[1]-2)

    init_dim = (i[0], f[1]-height)
    width_dist = distance_formula(i, f)
    dim = (init_dim[0], init_dim[1], width_dist, height)

    pygame.draw.rect(screen, color, dim, 0, 5)

    return (mid_point[0], init_dim[1]+3)


def draw_ui(screen, game: Game, font):
    pygame.draw.line(screen, GRAY_COLOR, bl_pos[0], bl_pos[1], 5)

    pygame.draw.line(screen, GRAY_COLOR, tower1_pos[0], tower1_pos[1], 5)
    pygame.draw.line(screen, GRAY_COLOR, tower2_pos[0], tower2_pos[1], 5)
    pygame.draw.line(screen, GRAY_COLOR, tower3_pos[0], tower3_pos[1], 5)

    if len(game.selected_towers) > 0:
        the_text = f"{game.selected_towers[0]}->"
        if len(game.selected_towers) > 1:
            the_text + str(game.selected_towers[1])
        move_text = font.render(the_text, True, GRAY_COLOR)
        text_rect = move_text.get_rect(
            center=(DIMENSIONS[0]/2, DIMENSIONS[1]/8))
        screen.blit(move_text, text_rect)

    for k, i in enumerate(game.towers):
        mid_point = mid_points[k]
        for j in i.rings:
            mid_point = draw_ring(screen, j, mid_point)

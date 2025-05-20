from src.constants import GRAY_COLOR, DIMENSIONS, RING_HIERARCHY
from src.utils import section_formula, distance_formula
import pygame

width, height = DIMENSIONS
RING_LENGTH_ = RING_HIERARCHY[0]["ring_length"]

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))

tower_height_i = bl_pos[0][1] * 1/3
tower1_width = section_formula(bl_pos[0][0], width / 2, 1, 2)
tower2_width = width / 2
tower3_width = section_formula(width / 2, bl_pos[1][0], 2, 1)

tower1_pos = ((tower1_width, tower_height_i), (tower1_width, bl_pos[1][1]))
tower2_pos = ((tower2_width, tower_height_i), (tower2_width, bl_pos[1][1]))
tower3_pos = ((tower3_width, tower_height_i), (tower3_width, bl_pos[1][1]))


def draw_ring(screen, ring_size: int, mid_point: tuple) -> tuple:
    height = RING_HIERARCHY[ring_size]["height"]
    color = RING_HIERARCHY[ring_size]["color"]
    ring_length = RING_HIERARCHY[ring_size]["ring_length"]

    i = (mid_point[0]-ring_length, mid_point[1]-2)
    f = (mid_point[0]+ring_length, mid_point[1]-2)

    init_dim = (i[0], f[1]-height)
    width = distance_formula(i, f)
    dim = (init_dim[0], init_dim[1], width, height)

    pygame.draw.rect(screen, color, dim, 0, 5)

    return (mid_point[0], init_dim[1]+3)


def draw_init_screen(screen, bg, rings):
    screen.blit(bg, (0, 0))

    pygame.draw.line(screen, GRAY_COLOR, bl_pos[0], bl_pos[1], 5)

    pygame.draw.line(screen, GRAY_COLOR, tower1_pos[0], tower1_pos[1], 5)
    pygame.draw.line(screen, GRAY_COLOR, tower2_pos[0], tower2_pos[1], 5)
    pygame.draw.line(screen, GRAY_COLOR, tower3_pos[0], tower3_pos[1], 5)

    mid_point = tower1_pos[1]
    for i in range(rings):
        mid_point = draw_ring(screen, i, mid_point)

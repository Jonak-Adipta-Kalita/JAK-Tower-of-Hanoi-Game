from src.constants import GRAY_COLOR, DIMENSIONS, RING_LENGTH
from src.utils import section_formula
import pygame

width, height = DIMENSIONS

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))

tower_height_i = bl_pos[0][1] * 0.5/3.5
tower1_width = section_formula(bl_pos[0][0], width / 2, 1, 2)
tower2_width = width / 2
tower3_width = section_formula(width / 2, bl_pos[1][0], 2, 1)

tower1_pos = (tower1_width, tower_height_i), (tower1_width, bl_pos[1][1])
tower2_pos = (tower2_width, tower_height_i), (tower2_width, bl_pos[1][1])
tower3_pos = (tower3_width, tower_height_i), (tower3_width, bl_pos[1][1])


def get_base_ring_pos(tower_pos):
    big_r_i = (tower_pos[1][0]-RING_LENGTH, tower_pos[1][1]-5)
    big_r_f = (tower_pos[1][0]+RING_LENGTH, tower_pos[1][1]-5)

    big_r = (big_r_i, big_r_f)
    return big_r


def get_tower1_rings_dimensions(rings: int) -> list:
    dimensions = []

    big_r = get_base_ring_pos(tower1_pos)
    dimensions.append(big_r)

    # Now, for the rest of the "rings" rings

    return dimensions


def draw_init_screen(screen, bg, rings):
    screen.blit(bg, (0, 0))

    pygame.draw.line(screen, GRAY_COLOR, bl_pos[0], bl_pos[1], 5)

    pygame.draw.line(screen, GRAY_COLOR, tower1_pos[0], tower1_pos[1], 5)
    pygame.draw.line(screen, GRAY_COLOR, tower2_pos[0], tower2_pos[1], 5)
    pygame.draw.line(screen, GRAY_COLOR, tower3_pos[0], tower3_pos[1], 5)

    rings_dimensions = get_tower1_rings_dimensions(rings)
    for dim in rings_dimensions:
        pygame.draw.line(screen, GRAY_COLOR, dim[0], dim[1], 5)

from src.constants import GRAY_COLOR, ORANGE_COLOR, PINK_COLOR, PURPLE_COLOR
from src.constants import DIMENSIONS, RING_LENGTH
from src.utils import section_formula, distance_formula
import pygame

width, height = DIMENSIONS

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))

tower_height_i = bl_pos[0][1] * 1/3
tower1_width = section_formula(bl_pos[0][0], width / 2, 1, 2)
tower2_width = width / 2
tower3_width = section_formula(width / 2, bl_pos[1][0], 2, 1)

tower1_pos = (tower1_width, tower_height_i), (tower1_width, bl_pos[1][1])
tower2_pos = (tower2_width, tower_height_i), (tower2_width, bl_pos[1][1])
tower3_pos = (tower3_width, tower_height_i), (tower3_width, bl_pos[1][1])


def get_base_ring_pos(tower_pos):
    height = 50

    big_r_i = (tower_pos[1][0]-RING_LENGTH, tower_pos[1][1]-2)
    big_r_f = (tower_pos[1][0]+RING_LENGTH, tower_pos[1][1]-2)
    init_dim = (big_r_i[0], big_r_i[1]-height)

    width = distance_formula(big_r_i, big_r_f)

    big_r = (init_dim[0], init_dim[1], width, height)
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
        pygame.draw.rect(screen, ORANGE_COLOR,
                         (dim[0], dim[1], dim[2], dim[3]), 0, 5)

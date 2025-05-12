from src.constants import GRAY_COLOR, DIMENSIONS
import pygame
import math

width, height = DIMENSIONS

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))


def section_formula(A, B, m, n):
    return (m * B + n * A) / (m + n)


def distance_formula(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


bl_length = distance_formula(bl_pos[0], bl_pos[1])

tower_height_i = bl_pos[0][1] * 0.5/3.5
tower1_width = section_formula(bl_pos[0][0], width / 2, 1, 2)
tower2_width = width / 2
tower3_width = section_formula(width / 2, bl_pos[1][0], 2, 1)


def get_tower1_rings_dimensions(rings: int) -> list:
    dimensions = []

    big_r_i = (bl_pos[0][0], bl_pos[0][1]-5)
    big_r_length_i_to_stick = distance_formula(
        big_r_i, (tower1_width, bl_pos[1][1]))
    big_r_f = (tower1_width + big_r_length_i_to_stick, bl_pos[1][1]-5)
    big_r = (big_r_i, big_r_f)

    dimensions.append(big_r)

    return dimensions


def draw_init_screen(screen, bg, rings):
    screen.blit(bg, (0, 0))

    pygame.draw.line(screen, GRAY_COLOR, bl_pos[0], bl_pos[1], 5)

    pygame.draw.line(screen, GRAY_COLOR, (tower1_width,
                     tower_height_i), (tower1_width, bl_pos[1][1]), 5)
    pygame.draw.line(screen, GRAY_COLOR, (tower2_width,
                     tower_height_i), (tower2_width, bl_pos[1][1]), 5)
    pygame.draw.line(screen, GRAY_COLOR, (tower3_width,
                     tower_height_i), (tower3_width, bl_pos[1][1]), 5)

    rings_dimensions = get_tower1_rings_dimensions(rings)
    pygame.draw.line(screen, GRAY_COLOR,
                     rings_dimensions[0][0], rings_dimensions[0][1], 5)

from src.constants import GRAY_COLOR, DIMENSIONS
import pygame

width, height = DIMENSIONS

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))


def section_formula(A, B, m, n):
    return (m * B + n * A) / (m + n)


tower_height_i = bl_pos[0][1] * 0.5/3.5
tower1_width = section_formula(bl_pos[0][0], width / 2, 1, 2)
tower2_width = width / 2
tower3_width = section_formula(width / 2, bl_pos[1][0], 2, 1)


def draw_init_screen(screen, bg):
    screen.blit(bg, (0, 0))

    pygame.draw.line(screen, GRAY_COLOR, bl_pos[0], bl_pos[1], 5)

    pygame.draw.line(screen, GRAY_COLOR, (tower1_width,
                     tower_height_i), (tower1_width, bl_pos[1][1]), 5)
    pygame.draw.line(screen, GRAY_COLOR, (tower2_width,
                     tower_height_i), (tower2_width, bl_pos[1][1]), 5)
    pygame.draw.line(screen, GRAY_COLOR, (tower3_width,
                     tower_height_i), (tower3_width, bl_pos[1][1]), 5)

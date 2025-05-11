from src.constants import GRAY_COLOR, DIMENSIONS
import pygame

width, height = DIMENSIONS

bl_pos = ((width/9, 3.5/5 * height), (8/9 * width, 3.5/5 * height))


def draw_init_screen(screen, bg):
    screen.blit(bg, (0, 0))

    pygame.draw.line(screen, GRAY_COLOR, bl_pos[0], bl_pos[1], 5)

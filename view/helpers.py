# helpers.py
import pygame

def draw_rounded_rect(surface, color, rect, radius=16):
    try:
        pygame.draw.rect(surface, color, rect, border_radius=radius)
    except TypeError:
        pygame.draw.rect(surface, color, rect)
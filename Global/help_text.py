import pygame


def centre_text(text_surface: pygame.surface.Surface, rect: pygame.rect.Rect):
    width_text, height_text = text_surface.get_size()
    width_rec, height_rec = rect.width, rect.height
    x_rec, y_rec = rect.left, rect.top
    x = width_rec / 2 - width_text / 2 + x_rec
    y = height_rec / 2 - height_text / 2 + y_rec
    return (x, y)
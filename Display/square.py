import pygame
from Global.global_variables import *

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, size, edge=False):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.edge = edge

        if self.edge:
            #self.image.fill(BLACK)
            self.font = pygame.font.SysFont(None, 15)
            self.font.render("X", True, WHITE, BLACK)
        else:
            self.image.fill(BEIGE_LIGHT)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, width=1)

    def clicked(self):
        self.image.fill(BLACK)




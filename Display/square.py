import pygame
from Global.global_variables import *
from Global.help_text import centre_text
import math

pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 10, bold=True)

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, size, grid_idx: tuple, is_edge=False):
        super().__init__()
        self.rect = pygame.Rect((x, y, size, size))
        self.row = grid_idx[0]
        self.col = grid_idx[1]
        self.color = WHITE
        self.is_edge = is_edge
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        # attributes for algorithms
        self.is_visited = False
        self.neighbours = []
        # distance from the start
        self.distance = math.inf
        # f cost for A* algorithm
        self.f_cost = math.inf

        if self.is_edge:
            self.color = BLACK

    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, width=1)
        if self.is_edge or self.is_wall:
            text = font.render("X", True, WHITE)
            surface.blit(text, centre_text(text, self.rect))
        elif self.is_start:
            text = font.render("S", True, BLACK)
            surface.blit(text, centre_text(text, self.rect))
        elif self.is_end:
            text = font.render("E", True, BLACK)
            surface.blit(text, surface.blit(text, centre_text(text, self.rect)))
            #image = pygame.image.load("/Users/jp/Desktop/dev/python/graphics/graph-traversal/images/checkeredFlag.png")
            #image = pygame.transform.scale(image, (self.rect[2], self.rect[3]))
            #surface.blit(image, (self.rect[0], self.rect[1]))

    def clicked(self, surface: pygame.surface.Surface, start_point=False, end_point=False):
        if start_point:
            self.color = YELLOW
            self.is_start = True
        elif end_point:
            self.color = GRAY
            self.is_end = True
        else:
            if self.is_start or self.is_end:
                return
            else:
                self.color = BLACK
                self.is_wall = True

    def reset(self, preserve_map=False):
        if preserve_map:
            if not (self.is_start or self.is_end or self.is_barrier()):
                self.color = WHITE
        else:
            self.is_start = False
            self.is_end = False
            self.is_wall = False
            if not self.is_edge:
                self.color = WHITE
        self.is_visited = False
        self.neighbours = []
        self.distance = math.inf
        self.f_cost = math.inf


    def is_barrier(self):
        return self.is_edge or self.is_wall

    def __lt__(self, other):
        return self.f_cost < other.f_cost


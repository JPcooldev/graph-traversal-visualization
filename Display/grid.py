import pygame
from Display.square import Square
import numpy as np
import random
from Global.global_variables import *


class Grid:
    def __init__(self, grid_size: tuple, square_size: int):
        self.grid_size = grid_size
        self.square_size = square_size
        self.grid = np.empty(shape=grid_size, dtype=Square)
        self.squares = pygame.sprite.Group()
        self.create_grid()

    def create_grid(self):
        nrows: int = self.grid_size[0]
        ncols: int = self.grid_size[1]
        for row in range(0, nrows):
            for col in range(0, ncols):
                # detect edges
                if row == 0 or row == nrows-1 or col == 0 or col == ncols-1:
                    square = Square(row * self.square_size, col * self.square_size, self.square_size, edge=True)
                else:
                    square = Square(row * self.square_size, col * self.square_size, self.square_size)
                self.squares.add(square)

    def draw(self, surface):
        for square in self.squares:
            square.draw(surface)

    def update(self, mouse_pos: tuple):
        for square in self.squares:
            if square.rect.collidepoint(mouse_pos):
                square.clicked()
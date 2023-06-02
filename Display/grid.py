import pygame
from Display.square import Square
from Global.global_variables import *


class Grid:
    def __init__(self, grid_size: tuple, square_size: int):
        self.grid_size: tuple = grid_size
        self.square_size = square_size
        self.grid = []
        self.squares = pygame.sprite.Group()
        self.create_grid()

    def create_grid(self):
        for row in range(0, NUM_ROWS):
            gridrow = []
            for col in range(0, NUM_ROWS):
                # detect edges
                if row == 0 or row == NUM_ROWS-1 or col == 0 or col == NUM_ROWS-1:
                    square = Square(row * self.square_size, col * self.square_size, self.square_size,
                                    grid_idx=(row, col), is_edge=True, )
                else:
                    square = Square(row * self.square_size, col * self.square_size, self.square_size,
                                    grid_idx=(row, col))
                self.squares.add(square)
                gridrow.append(square)
            self.grid.append(gridrow)

    def draw(self, surface):
        for square in self.squares:
            square.draw(surface)
        pygame.display.update()

    def reset(self, color=True, start=True, end=True):
        for row in self.grid:
            for square in row:
                square.reset(color, start, end)

    def get_neighbours(self, square: Square):
        row, col = square.row, square.col
        N = NUM_ROWS
        neighbours = []
        # top
        if 0 <= row-1 < N and 0 <= col < N and not self.grid[row-1][col].is_barrier():
            neighbours.append(self.grid[row-1][col])
        # right
        if 0 <= row < N and 0 <= col+1 < N and not self.grid[row][col+1].is_barrier():
            neighbours.append(self.grid[row][col+1])
        # bottom
        if 0 <= row+1 < N and 0 <= col < N and not self.grid[row+1][col].is_barrier():
            neighbours.append(self.grid[row+1][col])
        # left
        if 0 <= row < N and 0 <= col-1 < N and not self.grid[row][col-1].is_barrier():
            neighbours.append(self.grid[row][col-1])

        return neighbours


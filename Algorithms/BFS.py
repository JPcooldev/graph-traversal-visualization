import pygame.surface
from Display.grid import Grid
from Display.square import Square
from Global.global_variables import *
import time


def BFS(draw, grid: Grid, start: Square, end: Square):
    queue = []
    queue.append(start)

    while queue:
        current = queue.pop(0)
        if current == end:
            break
        if not current.is_visited:
            current.is_visited = True
            if current != start:
                current.color = RED
            draw()
            for neighbour in grid.get_neighbours(current):
                if not neighbour.is_visited:
                    queue.append(neighbour)
                    neighbour.color = GREEN
                    draw()


def color_path(path: list, surface: pygame.surface.Surface):
    for square in path:
        square.color = RED
        square.draw(surface)
        time.sleep(0.5)

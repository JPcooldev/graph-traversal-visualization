from Display.grid import Grid
from Display.square import Square
from Global.global_variables import *


def bfs(draw, grid: Grid, start: Square, end: Square):
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
    return True

import pygame.surface
from Display.grid import Grid
from Display.square import Square
from Global.global_variables import *
import heapq


def astar(draw, grid: Grid, start: Square, end: Square, visualizing_path=False):
    """

    """
    open = []
    # closed set = .is_visited
    open.append(start)
    start.distance = 0
    start.f_cost = 0
    #heapq.heappush(open, (start.f_cost, start))

    while open:
        # sorting to chose node with the lowest f_cost
        open.sort(key=lambda square: square.f_cost)
        current = open.pop(0)
        #current = heapq.heappop(open)[1]

        # current node is closed
        current.is_visited = True
        if current != start or current != end:
            current.color = RED

        if visualizing_path:
            path = find_path(start, current)
            color_path(draw, path, YELLOW)

        # we found an end
        if current == end:
            path = find_path(start, end)
            color_path(draw, path, YELLOW)
            break

        # find a neighbours which has not been visited yet
        for neighbour in grid.get_neighbours(current):
            if neighbour.is_visited:
                continue
            neighbour.distance = current.distance + 1
            h_cost = abs(neighbour.row - end.row) ** 2 + abs(neighbour.col - end.col) ** 2
            f_cost = neighbour.distance + h_cost
            # if node is not in open set, or we found a shorter to it, so we update it
            if neighbour not in open or f_cost < neighbour.f_cost:
                neighbour.f_cost = f_cost
                neighbour.parent = current
                if neighbour not in open:
                    open.append(neighbour)
                    #heapq.heappush(open, (neighbour.f_cost, neighbour))
                    neighbour.color = GREEN

        if visualizing_path:
            color_path(draw, path, RED)
        else:
            draw()
    return True


def color_path(draw, path: list, color):
    for square in path:
        square.color = color
        draw()


def find_path(start, current):
    path = []
    path.append(current)
    # going back to the start based on the shortest distance from the start
    while current != start:
        path.append(current.parent)
        current = current.parent
    return path


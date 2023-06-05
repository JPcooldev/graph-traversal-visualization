import pygame.surface
from Display.grid import Grid
from Display.square import Square
from Global.global_variables import *
import time
import math


def dijkstra(draw, grid: Grid, start: Square, end: Square, visualizing_path=False):
    """
    Traversing a graph using BFS while adding a previous node to each visited node.
    """
    queue = []
    queue.append(start)
    start.distance = 0

    while queue:
        current = queue.pop(0)
        # we found an end
        if current == end:
            path = find_path(start, end)
            color_path(draw, path, YELLOW)
            break
        # node has not been visited yet
        if not current.is_visited:
            # visit a node
            current.is_visited = True
            if current != start:
                current.color = RED

            # coloring path to the start
            if visualizing_path:
                path = find_path(start, current)
                color_path(draw, path, YELLOW)

            # find a neighbours which has not been visited yet
            for neighbour in grid.get_neighbours(current):
                if not neighbour.is_visited:
                    # add node to queue so it can be visited
                    queue.append(neighbour)
                    # add previous node to a node (so it can then be used to find a path back to the start)
                    neighbour.neighbours.append(current)
                    # add distance (how many nodes it is from the start)
                    neighbour.distance = current.distance + 1
                    neighbour.color = GREEN

            # coloring path back
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
    # going back to the start based on the shortest distance from the start
    while current != start:
        shortest_path_node = None
        min_dist = math.inf
        for neighbour in current.neighbours:
            if neighbour.distance < min_dist:
                min_dist = neighbour.distance
                shortest_path_node = neighbour
        path.append(current)
        current = shortest_path_node
    return path

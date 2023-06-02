import pygame.surface
from Display.grid import Grid
from Display.square import Square
from Global.global_variables import *
import time
import math


def Dijkstra(draw, grid: Grid, start: Square, end: Square):
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
            path = []
            node = end
            # going back to the start based on the shortest distance from the start
            while node != start:
                shortest_path_node = None
                min_dist = math.inf
                for neighbour in node.neighbours:
                    if neighbour.distance < min_dist:
                        min_dist = neighbour.distance
                        shortest_path_node = neighbour
                path.append(node)
                node = shortest_path_node
            color_path(draw, path)
            break
        # node has not been visited yet
        if not current.is_visited:
            # visit a node
            current.is_visited = True
            if current != start:
                current.color = RED
            draw()
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
                    draw()


def color_path(draw, path: list):
    for square in path:
        square.color = YELLOW
        draw()


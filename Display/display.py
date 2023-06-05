import pygame
import time
from Display.grid import Grid
from Display.menu import Menu
from Global.global_variables import *
from Algorithms.BFS import bfs
from Algorithms.DFS import dfs
from Algorithms.Dijkstra import dijkstra
from Algorithms.Astar import astar


class Display:
    def __init__(self):
        self.grid = Grid(GRID_SIZE, SQUARE_SIZE)
        self.menu = Menu(MENU_WIDTH, MENU_HEIGHT, topleft=(SCREEN_WIDTH - MENU_WIDTH, 0))
        self.is_startpoint_selected = False
        self.start = None
        self.is_endpoint_selected = False
        self.end = None
        self.algo_finished = False
        # BFS=1, DFS=2, Dijkstra=3, Astar=4
        self.algo_ID = 0


    def run(self):
        pygame.init()
        scene = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("VISUALIZATION OF GRAPH TRAVERSAL ALGORITHMS")

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                # LEFT CLICK
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()

                    if self.menu.checked_grid:
                        # grid modification
                        for square in self.grid.squares:
                            if square.rect.collidepoint(mouse_pos):
                                if not self.is_startpoint_selected:
                                    self.is_startpoint_selected = True
                                    self.start = square
                                    square.clicked(scene, start_point=True)
                                    self.menu.set_algo_info_text("Pick an end point")
                                elif not self.is_endpoint_selected:
                                    self.is_endpoint_selected = True
                                    self.end = square
                                    square.clicked(scene, end_point=True)
                                    self.menu.set_algo_info_text("Pick an algorithm or make barriers")
                                else:
                                    square.clicked(scene)
                    # graph is checked
                    else:
                        pass


                    # button selection
                    if self.menu.button_BFS.collidepoint(mouse_pos):
                        self.menu.button_BFS_color = RED
                        self.menu.set_algo_info_text("Breadth First Search")
                        self.algo_ID = 1
                    elif self.menu.button_DFS.collidepoint(mouse_pos):
                        self.menu.button_DFS_color = RED
                        self.menu.set_algo_info_text("Depth First Search")
                        self.algo_ID = 2
                    elif self.menu.button_Dijkstra.collidepoint(mouse_pos):
                        self.menu.button_Dijkstra_color = RED
                        self.menu.set_algo_info_text("Dijkstra algorithm")
                        self.algo_ID = 3
                    elif self.menu.button_Astar.collidepoint(mouse_pos):
                        self.menu.button_Astar_color = RED
                        self.menu.set_algo_info_text("A* algorithm")
                        self.algo_ID = 4
                    elif self.menu.button_start.collidepoint(mouse_pos):
                        self.menu.button_start_color = RED
                        if self.algo_ID != 0 and self.start and self.end:
                            if self.algo_finished:
                                self.grid.reset(preserve_map=True)

                            if self.algo_ID == 1:
                                self.algo_finished = bfs(lambda: self.grid.draw(scene), self.grid, self.start, self.end)
                            elif self.algo_ID == 2:
                                self.algo_finished = dfs(lambda: self.grid.draw(scene), self.grid, self.start, self.end)
                            elif self.algo_ID == 3:
                                self.algo_finished = dijkstra(lambda: self.grid.draw(scene), self.grid, self.start, self.end,
                                                              visualizing_path=self.menu.checked_visualization)
                            elif self.algo_ID == 4:
                                self.algo_finished = astar(lambda: self.grid.draw(scene), self.grid, self.start, self.end,
                                                           visualizing_path=self.menu.checked_visualization)
                    elif self.menu.button_reset.collidepoint(mouse_pos):
                        self.menu.button_reset_color = RED
                        self.algo_ID = 0
                        self.is_startpoint_selected = False
                        self.start = None
                        self.is_endpoint_selected = False
                        self.end = None
                        self.grid.reset()
                        self.algo_finished = False
                        self.menu.num_squares_path = 0
                        self.menu.set_algo_info_text("Pick a start point")
                    elif self.menu.select_visualization.collidepoint(mouse_pos):
                        self.menu.checked_visualization = not self.menu.checked_visualization
                    elif self.menu.select_grid.collidepoint(mouse_pos):
                        self.grid.create_grid()
                        self.menu.checked_grid = not self.menu.checked_grid
                        self.menu.checked_graph = not self.menu.checked_grid
                    elif self.menu.select_graph.collidepoint(mouse_pos):
                        self.menu.checked_graph = not self.menu.checked_graph
                        self.menu.checked_grid = not self.menu.checked_graph
                # MOUSE MOTION
                elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.menu.checked_grid:
                        for square in self.grid.squares:
                            if square.rect.collidepoint(mouse_pos):
                                square.clicked(scene)
                # MOUSE RELEASED
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.menu.mouse_released()


            #scene.fill(WHITE)
            self.grid.draw(scene)
            self.menu.draw(scene, self.grid)
            pygame.display.flip()
            pygame.time.Clock().tick(60)


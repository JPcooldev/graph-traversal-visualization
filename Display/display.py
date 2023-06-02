import pygame
import time
from Display.grid import Grid
from Display.menu import Menu
from Global.global_variables import *
from Algorithms.BFS import BFS
from Algorithms.DFS import DFS
from Algorithms.Dijkstra import Dijkstra


class Display:
    def __init__(self):
        self.grid = Grid(GRID_SIZE, SQUARE_SIZE)
        self.menu = Menu(MENU_WIDTH, MENU_HEIGHT, topleft=(SCREEN_WIDTH - MENU_WIDTH, 0))
        self.is_startpoint_selected = False
        self.start = None
        self.is_endpoint_selected = False
        self.end = None
        self.is_run_selected = False
        self.is_run_over = False
        # BFS=1, DFS=2, Dijkstra=3, Astar=4
        self.algo_ID = 0

    def run(self):
        pygame.init()
        scene = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                # LEFT CLICK
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()

                    # grid modification
                    for square in self.grid.squares:
                        if square.rect.collidepoint(mouse_pos):
                            if not self.is_startpoint_selected:
                                self.is_startpoint_selected = True
                                self.start = square
                                square.clicked(scene, start_point=True)
                            elif not self.is_endpoint_selected:
                                self.is_endpoint_selected = True
                                self.end = square
                                square.clicked(scene, end_point=True)
                            else:
                                square.clicked(scene)

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
                    elif self.menu.button_start.collidepoint(mouse_pos):
                        self.menu.button_start_color = RED
                        if self.algo_ID != 0 and self.start and self.end:
                            if self.algo_ID == 1:
                                BFS(lambda: self.grid.draw(scene), self.grid, self.start, self.end)
                            elif self.algo_ID == 2:
                                DFS(lambda: self.grid.draw(scene), self.grid, self.start, self.end)
                            elif self.algo_ID == 3:
                                Dijkstra(lambda: self.grid.draw(scene), self.grid, self.start, self.end)
                            self.grid.reset(color=False, start=False, end=False)
                    elif self.menu.button_end.collidepoint(mouse_pos):
                        self.menu.button_end_color = RED
                        self.algo_ID = 0
                        self.is_startpoint_selected = False
                        self.start = None
                        self.is_endpoint_selected = False
                        self.end = None
                        self.grid.reset()
                # MOUSE MOTION
                elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    for square in self.grid.squares:
                        if square.rect.collidepoint(mouse_pos):
                            square.clicked(scene)
                # MOUSE RELEASED
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.menu.mouse_released()


            #scene.fill(WHITE)
            self.grid.draw(scene)
            self.menu.draw(scene)
            pygame.display.flip()
            pygame.time.Clock().tick(60)


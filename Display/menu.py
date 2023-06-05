import pygame
import pygame.font
from Global.global_variables import *
from Global.help_text import centre_text


pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 20)
font_small = pygame.font.SysFont("Times New Roman", 15)

class Menu(pygame.sprite.Sprite):
    def __init__(self, width, height, topleft: tuple):
        super().__init__()
        self.width = width
        self.height = height

        # (x, y, width, height)
        self.rect_algo_info = (800, 0, self.width, 300)
        self.rect_choice_legend = (800, 300, self.width, 50)
        self.rect_choice_algo = (800, 350, self.width, 100)
        self.rect_choice_grid = (800, 450, self.width, 100)
        self.rect_stats = (800, 550, self.width, 100)
        self.rect_button_start_reset = (800, 650, self.width, 50)
        self.rect_legend = (800, 700, self.width, 100)

        # info about algorithms
        #self.algo_info = pygame.Rect((topleft[0], topleft[1], self.width, self.height / 8 * 3))
        self.algo_info = pygame.Rect(self.rect_algo_info)
        self.algo_info_text = "Pick a start point"
        self.algo_info_text_surf = font.render(self.algo_info_text, True, BLACK)

        # button section for selection of algorithm
        self.choice_legend = pygame.Rect(self.rect_choice_legend)
        self.choice = pygame.Rect(self.rect_choice_algo)

        self.button_dims = (self.rect_choice_algo[2] / 2, self.rect_stats[3] / 2)
        self.btn_width = self.rect_choice_algo[2] / 2
        self.btn_alg_height = self.rect_choice_algo[3] / 2

        self.button_BFS = pygame.Rect(self.rect_choice_algo[0], self.rect_choice_algo[1],
                                      self.btn_width, self.btn_alg_height)
        self.button_BFS_color = GRAY

        self.button_DFS = pygame.Rect(self.rect_choice_algo[0] + self.btn_width, self.rect_choice_algo[1],
                                      self.btn_width, self.btn_alg_height)
        self.button_DFS_color = GRAY

        self.button_Dijkstra = pygame.Rect(self.rect_choice_algo[0], self.rect_choice_algo[1] + self.btn_alg_height,
                                           self.btn_width, self.btn_alg_height)
        self.button_Dijkstra_color = GRAY

        self.button_Astar = pygame.Rect(self.rect_choice_algo[0] + self.btn_width, self.rect_choice_algo[1] + self.btn_alg_height,
                                        self.btn_width, self.btn_alg_height)
        self.button_Astar_color = GRAY

        # selection of grid/graph
        self.choice_grid = pygame.Rect(self.rect_choice_grid)

        #selection bars
        self.select_visualization = pygame.Rect(self.choice_grid[0] + 50, self.rect_choice_grid[1] + 5, 20, 20)
        self.select_grid = pygame.Rect(self.choice_grid[0] + 50, self.rect_choice_grid[1] + 40, 20, 20)
        self.select_graph = pygame.Rect(self.choice_grid[0] + 50, self.rect_choice_grid[1] + 75, 20, 20)

        self.select_visualization_text = pygame.Rect(self.choice_grid[0] + 100, self.rect_choice_grid[1] + 5, 280, 20)
        self.select_grid_text = pygame.Rect(self.choice_grid[0] + 100, self.rect_choice_grid[1] + 40, 200, 20)
        self.select_graph_text = pygame.Rect(self.choice_grid[0] + 100, self.rect_choice_grid[1] + 75, 200, 20)

        self.checked_visualization = False
        self.checked_grid = True
        self.checked_graph = False

        # statistics of searching (time, # visited blocks, ...)
        self.stats = pygame.Rect(self.rect_stats)
        self.num_visited = pygame.Rect((self.rect_stats[0], self.rect_stats[1], self.width, 30))
        #self.status = pygame.Rect()

        # start/reset button
        self.button_start_reset = pygame.Rect(self.rect_button_start_reset)
        self.button_start = pygame.Rect((self.rect_button_start_reset[0], self.rect_button_start_reset[1],
                                         self.btn_width, self.rect_button_start_reset[3]))
        self.button_start_color = GRAY
        self.button_reset = pygame.Rect((self.rect_button_start_reset[0] + self.btn_width, self.rect_button_start_reset[1],
                                         self.btn_width, self.rect_button_start_reset[3]))
        self.button_reset_color = GRAY

        # legend
        self.legend = pygame.Rect(self.rect_legend)

    def draw(self, surface, grid):
        # algo_info
        gap_top_bottom = 10
        gap_left_right = 10
        pygame.draw.rect(surface, GRAY_LIGHT, self.algo_info)
        border_algo = pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.algo_info, gap_top_bottom, gap_left_right),
                         width=2)
        surface.blit(self.algo_info_text_surf, centre_text(self.algo_info_text_surf, border_algo))

        pygame.draw.rect(surface, GRAY_LIGHT, self.choice_legend)
        text = font.render("Pick an algorithm:", True, BLACK)
        surface.blit(text, centre_text(text, self.choice_legend))
        pygame.draw.rect(surface, GRAY_LIGHT, self.choice)
        # buttons inside choice
        #   BFS     DFS
        # Dijkstra Astar

        gap_top_bottom = 5
        gap_left_right = 10

        # BFS button
        pygame.draw.rect(surface, self.button_BFS_color, self.adjust_rect_position(self.button_BFS, gap_top_bottom, gap_left_right), border_radius=20)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_BFS, gap_top_bottom, gap_left_right), width=2, border_radius=20)
        text = font.render("BFS", True, WHITE)
        surface.blit(text, centre_text(text, self.button_BFS))

        # DFS button
        pygame.draw.rect(surface, self.button_DFS_color, self.adjust_rect_position(self.button_DFS, gap_top_bottom, gap_left_right), border_radius=20)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_DFS, gap_top_bottom, gap_left_right), width=2, border_radius=20)
        text = font.render("DFS", True, WHITE)
        surface.blit(text, centre_text(text, self.button_DFS))

        # Dijkstra button
        pygame.draw.rect(surface, self.button_Dijkstra_color, self.adjust_rect_position(self.button_Dijkstra, gap_top_bottom, gap_left_right), border_radius=20)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_Dijkstra, gap_top_bottom, gap_left_right), width=2, border_radius=20)
        text = font.render("Dijkstra algorithm", True, WHITE)
        surface.blit(text, centre_text(text, self.button_Dijkstra))

        # Astar button
        pygame.draw.rect(surface, self.button_Astar_color, self.adjust_rect_position(self.button_Astar, gap_top_bottom, gap_left_right), border_radius=20)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_Astar, gap_top_bottom, gap_left_right), width=2, border_radius=20)
        text = font.render("A* algorithm", True, WHITE)
        surface.blit(text, centre_text(text, self.button_Astar))

        # selection part
        pygame.draw.rect(surface, GRAY_LIGHT, self.rect_choice_grid)

        pygame.draw.rect(surface, WHITE, self.select_visualization)
        pygame.draw.rect(surface, BLACK, self.select_visualization, width=2)
        if self.checked_visualization:
            pygame.draw.circle(surface, BLACK, self.get_centre(self.select_visualization), 7)
        """
        pygame.draw.rect(surface, WHITE, self.select_grid)
        pygame.draw.rect(surface, BLACK, self.select_grid, width=2)
        if self.checked_grid:
            pygame.draw.circle(surface, BLACK, self.get_centre(self.select_grid), 7)

        pygame.draw.rect(surface, WHITE, self.select_graph)
        pygame.draw.rect(surface, BLACK, self.select_graph, width=2)
        if self.checked_graph:
            pygame.draw.circle(surface, BLACK, self.get_centre(self.select_graph), 7)
        """
        pygame.draw.rect(surface, WHITE, self.select_visualization_text)
        text = font_small.render("real-time visualization of path (super slow)", True, BLACK)
        surface.blit(text, centre_text(text, self.select_visualization_text))
        """
        pygame.draw.rect(surface, WHITE, self.select_grid_text)
        text = font_small.render("grid", True, BLACK)
        surface.blit(text, centre_text(text, self.select_grid_text))

        pygame.draw.rect(surface, WHITE, self.select_graph_text)
        text = font_small.render("graph", True, BLACK)
        surface.blit(text, centre_text(text, self.select_graph_text))
        """
        # stats section
        pygame.draw.rect(surface, GRAY_LIGHT, self.stats)

        #pygame.draw.rect(surface, RED, self.num_visited)
        #num_visited_text = str(self.num_squares_path)
        #text = font.render(num_visited_text, True, BLACK)
        #surface.blit(text, centre_text(text, self.num_visited))

        # start/end button section
        pygame.draw.rect(surface, GRAY_LIGHT, self.button_start_reset)


        # start and end button
        pygame.draw.rect(surface, self.button_start_color, self.adjust_rect_position(self.button_start, gap_top_bottom, gap_left_right),
                         border_radius=50)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_start, gap_top_bottom, gap_left_right),
                         width=2, border_radius=50)
        text = font.render("START", True, WHITE)
        surface.blit(text, centre_text(text, self.button_start))

        pygame.draw.rect(surface, self.button_reset_color, self.adjust_rect_position(self.button_reset, gap_top_bottom, gap_left_right),
                         border_radius=50)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_reset, gap_top_bottom, gap_left_right),
                         width=2, border_radius=50)
        text = font.render("RESET GRID", True, WHITE)
        surface.blit(text, centre_text(text, self.button_reset))

        # legend section
        pygame.draw.rect(surface, GRAY_LIGHT, self.legend)

    def set_algo_info_text(self, text):
        self.algo_info_text = text
        self.algo_info_text_surf = font.render(self.algo_info_text, True, BLACK)

    def mouse_released(self):
        self.button_BFS_color = GRAY
        self.button_DFS_color = GRAY
        self.button_Dijkstra_color = GRAY
        self.button_Astar_color = GRAY
        self.button_start_color = GRAY
        self.button_reset_color = GRAY

    def adjust_rect_position(self, rect: pygame.rect.Rect, gap_top_bottom, gap_left_right):
        x, y = rect[0], rect[1]
        width, height = rect[2], rect[3]
        # adjusting
        x = x + gap_left_right
        y = y + gap_top_bottom
        width = width - 2 * gap_left_right
        height = height - 2 * gap_top_bottom
        return (x, y, width, height)

    def get_centre(self, rect: pygame.rect.Rect):
        x, y, width, height = rect[0], rect[1], rect[2], rect[3]
        return (x + width/2, y + height/2)
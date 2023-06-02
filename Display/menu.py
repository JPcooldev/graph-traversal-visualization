import pygame
import pygame.font
from Global.global_variables import *
from Global.help_text import centre_text

pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 20)

class Menu(pygame.sprite.Sprite):
    def __init__(self, width, height, topleft: tuple):
        super().__init__()
        self.width = width
        self.height = height

        # (x, y, width, height)
        self.rect_algo_info = (800, 0, self.width, 300)
        self.rect_choice_legend = (800, 300, self.width, 50)
        self.rect_choice = (800, 350, self.width, 100)
        self.rect_stats = (800, 450, self.width, 200)
        self.rect_button_start_end = (800, 650, self.width, 50)
        self.rect_legend = (800, 700, self.width, 100)

        # info about algorithms
        #self.algo_info = pygame.Rect((topleft[0], topleft[1], self.width, self.height / 8 * 3))
        self.algo_info = pygame.Rect(self.rect_algo_info)
        self.algo_info_text = ""
        self.algo_info_text_surf = font.render(self.algo_info_text, True, BLACK)

        # button section for selection of algorithm
        self.choice_legend = pygame.Rect(self.rect_choice_legend)
        self.choice = pygame.Rect(self.rect_choice)

        self.button_dims = (self.rect_choice[2] / 2, self.rect_stats[3] / 2)
        self.btn_width = self.rect_choice[2] / 2
        self.btn_alg_height = self.rect_choice[3] / 2

        self.button_BFS = pygame.Rect(self.rect_choice[0], self.rect_choice[1],
                                      self.btn_width, self.btn_alg_height)
        self.button_BFS_color = GRAY

        self.button_DFS = pygame.Rect(self.rect_choice[0] + self.btn_width, self.rect_choice[1],
                                      self.btn_width, self.btn_alg_height)
        self.button_DFS_color = GRAY

        self.button_Dijkstra = pygame.Rect(self.rect_choice[0], self.rect_choice[1] + self.btn_alg_height,
                                           self.btn_width, self.btn_alg_height)
        self.button_Dijkstra_color = GRAY

        self.button_Astar = pygame.Rect(self.rect_choice[0] + self.btn_width, self.rect_choice[1] + self.btn_alg_height,
                                        self.btn_width, self.btn_alg_height)
        self.button_Astar_color = GRAY

        # statistics of searching (time, # visited blocks, ...)
        self.stats = pygame.Rect(self.rect_stats)
        self.button_start_end = pygame.Rect(self.rect_button_start_end)

        self.button_start = pygame.Rect((self.rect_button_start_end[0], self.rect_button_start_end[1],
                                         self.btn_width, self.rect_button_start_end[3]))
        self.button_start_color = GRAY
        self.button_end = pygame.Rect((self.rect_button_start_end[0] + self.btn_width, self.rect_button_start_end[1],
                                       self.btn_width, self.rect_button_start_end[3]))
        self.button_end_color = GRAY

        # legend
        self.legend = pygame.Rect(self.rect_legend)

    def draw(self, surface):
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

        # stats section
        pygame.draw.rect(surface, GRAY_LIGHT, self.stats)
        pygame.draw.rect(surface, GRAY_LIGHT, self.button_start_end)

        # start and end button
        pygame.draw.rect(surface, self.button_start_color, self.adjust_rect_position(self.button_start, gap_top_bottom, gap_left_right),
                         border_radius=50)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_start, gap_top_bottom, gap_left_right),
                         width=2, border_radius=50)
        text = font.render("START", True, WHITE)
        surface.blit(text, centre_text(text, self.button_start))

        pygame.draw.rect(surface, self.button_end_color, self.adjust_rect_position(self.button_end, gap_top_bottom, gap_left_right),
                         border_radius=50)
        pygame.draw.rect(surface, BLACK, self.adjust_rect_position(self.button_end, gap_top_bottom, gap_left_right),
                         width=2, border_radius=50)
        text = font.render("END", True, WHITE)
        surface.blit(text, centre_text(text, self.button_end))

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
        self.button_end_color = GRAY

    def adjust_rect_position(self, rect: pygame.rect.Rect, gap_top_bottom, gap_left_right):
        x, y = rect[0], rect[1]
        width, height = rect[2], rect[3]
        # adjusting
        x = x + gap_left_right
        y = y + gap_top_bottom
        width = width - 2 * gap_left_right
        height = height - 2 * gap_top_bottom
        return (x, y, width, height)

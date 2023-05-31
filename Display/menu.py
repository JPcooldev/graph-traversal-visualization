import  pygame
import pygame.font
from Global.global_variables import *

pygame.font.init()
font = pygame.font.SysFont("Arial", 15)

class Menu(pygame.sprite.Sprite):
    def __init__(self, width, height, topleft: tuple):
        super().__init__()
        self.width = width
        self.height = height
        self.xyalgo_info = topleft
        self.xychoice = (topleft[0], topleft[1] + self.height / 8 * 3)
        self.xystats = (topleft[0], topleft[1] + self.height / 8 * 5)
        self.xylegend = (topleft[0], topleft[1] + self.height / 8 * 7)

        # info about algorithms
        self.algo_info = pygame.Surface((self.width, self.height / 8 * 3))
        self.algo_info.fill(BEIGE_LIGHT)

        # button section for selection of algorithm
        self.choice = pygame.Surface((self.width, self.height / 4))
        self.choice.fill(BEIGE_LIGHT)

        self.button_dims = (self.width / 2, (self.xystats[1] - self.xychoice[1]) / 2)
        self.button_BFS = pygame.Surface(self.button_dims)
        self.button_BFS.fill(BEIGE_LIGHT)
        self.button_DFS = pygame.Surface(self.button_dims)
        self.button_DFS.fill(BEIGE_LIGHT)
        self.button_Dijkstra = pygame.Surface(self.button_dims)
        self.button_Dijkstra.fill(BEIGE_LIGHT)
        self.button_Astar = pygame.Surface(self.button_dims)
        self.button_Astar.fill(BEIGE_LIGHT)

        # statistics of searching (time, # visited blocks, ...)
        self.stats = pygame.Surface((self.width, self.height / 4))
        self.stats.fill(BEIGE_LIGHT)

        # legend
        self.legend = pygame.Surface((self.width, self.height / 8))
        self.legend.fill(BEIGE_LIGHT)

    def draw(self, surface):
        surface.blit(self.algo_info, self.xyalgo_info)
        algo_border = pygame.Rect(self.xyalgo_info[0], self.xyalgo_info[1], self.width, self.height / 8 * 3)
        pygame.draw.rect(surface, BLACK, algo_border, width=2)

        surface.blit(self.choice, self.xychoice)
        # buttons inside choice
        #   BFS     DFS
        # Dijkstra Astar

        # BFS button
        surface.blit(self.button_BFS, self.xychoice)
        button_BFS_border = pygame.Rect(self.xychoice[0], self.xychoice[1],
                                        self.button_dims[0], self.button_dims[1])
        pygame.draw.rect(surface, BLACK, button_BFS_border, width=2)
        text_BFS = font.render("BFS", True, BLACK)
        surface.blit(text_BFS, self.centre_text(text_BFS, self.button_BFS))

        # DFS button
        surface.blit(self.button_DFS, (self.xychoice[0] + self.button_dims[0], self.xychoice[1]))
        button_DFS_border = pygame.Rect(self.xychoice[0] + self.button_dims[0], self.xychoice[1],
                                        self.button_dims[0], self.button_dims[1])
        pygame.draw.rect(surface, BLACK, button_DFS_border, width=2)

        # Dijkstra button
        surface.blit(self.button_Dijkstra, (self.xychoice[0], self.xychoice[1] + self.button_dims[1]))
        button_Dijkstra_border = pygame.Rect(self.xychoice[0], self.xychoice[1] + self.button_dims[1],
                                             self.button_dims[0], self.button_dims[1])
        pygame.draw.rect(surface, BLACK, button_Dijkstra_border, width=2)

        # Astar button
        surface.blit(self.button_Astar, (self.xychoice[0] + self.button_dims[0], self.xychoice[1] + self.button_dims[1]))
        button_Astar_border = pygame.Rect(self.xychoice[0] + self.button_dims[0], self.xychoice[1] + self.button_dims[1],
                                          self.button_dims[0], self.button_dims[1])
        pygame.draw.rect(surface, BLACK, button_Astar_border, width=2)

        surface.blit(self.stats, self.xystats)
        surface.blit(self.legend, self.xylegend)

    # surface does not return position (x,y)
    def centre_text(self, text_surface: pygame.surface.Surface, surface: pygame.surface.Surface):
        width_text, height_text = text_surface.get_size()
        width_surf, height_surf = surface.get_size()
        #x_surf, y_surf = surface.get
        x = width_surf / 2 - width_text / 2
        y = height_surf / 2 - height_text / 2
        return (x,y)

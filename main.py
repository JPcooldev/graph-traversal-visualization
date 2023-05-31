import pygame
import sys
import time
from Display.grid import Grid
from Display.menu import Menu
from Global.global_variables import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = Grid((30, 30), 20)
menu = Menu(MENU_WIDTH, MENU_HEIGHT, (SCREEN_WIDTH - MENU_WIDTH, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid.update(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                grid.update(pygame.mouse.get_pos())

    screen.fill((255, 255, 255))
    grid.draw(screen)
    menu.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)


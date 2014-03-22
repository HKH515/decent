import pygame
import pymysql
import random
import _HermannSql

pygame.init()
res_x = 800
res_y = 600

screen = pygame.display.set_mode((res_x, res_y))

running = True
while running:
    pygame.draw.rect(screen, (255, 35, 255), (0.5*res_x, 0.5*res_y), (40, 40))
    pygame.display.update()
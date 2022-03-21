import pygame
from sys import exit

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.wall = pygame.image.load('assets/graphics/orange_rectangle.png').convert_alpha()
        self.wall = pygame.transform.scale2x(self.wall)
        self.x = int(x)
        self.y = int(y)
        self.image = self.wall
        self.rect = self.image.get_rect(midbottom = (x,y))
import os
import pygame
from scripts.sprite import Sprite
from scripts.functios import load_image
class Game():
    def __init__(self):
        self.image = pygame.image.load(os.path.join('assets','icons','icon.ico'))
        path = os.path.join('assets','images','background.png')
        self.background = pygame.image.load(path)
        self.platforms = [
            Sprite(load_image('assets','images','platform.png'),(240, 700)),
            Sprite(load_image('assets','images','platform.png'),(100, 450)),
            Sprite(load_image('assets','images','platform.png'),(380, 250)),
        ]
    def render_objects(self,displ):
        displ.blit(self.background,(0,0)) 
        for platform in self.platforms:
            platform.render(displ)
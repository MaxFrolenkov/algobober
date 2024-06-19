import os
import pygame
from scripts.sprite import Sprite
from scripts.functios import load_image
from scripts.player import Player
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
        self.background_image = load_image('assets','images','background.png')
        self.platforms = []
        self.player = Player(load_image('assets','images','player.png'),((240,600)),5,15,0.75)

    def render_objects(self,displ):
        displ.blit(self.background,(0,0)) 
        self.player.render(displ)
        for platform in self.platforms:
            platform.render(displ)
        
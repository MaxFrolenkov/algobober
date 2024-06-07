import os 
import pygame
from scripts.app import game
class App():
    def __init__(self):
    self.runn = True
    self.FPS = 60
    self.displ = pygame.display.set_mode(480,720)
    self.tm = pygame.time.Clock()
    pygame.display.set_caption('Doodle Jump')
    self.image = pygame.image.load(os.path.join('assets','images','background.png')
    pygame.display.set.icon(image))
    def run():
        while self.runn:
            self.handle_events()
            self.update()
            self.render()

            self.
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runn = False
    def render(self):
        self.displ.fill(0,0,0)

        pygame.dispay.update()
    
        
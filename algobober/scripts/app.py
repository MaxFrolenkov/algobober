from scripts.game import Game
import os 
import pygame


class App():
    def __init__(self):
        self.runn = True
        self.FPS = 60
        self.displ = pygame.display.set_mode((480,720))
        self.tm = pygame.time.Clock()
        pygame.display.set_caption('Doodle Jump')
        self.game = Game()
        #self.image = pygame.image.load(os.path.join('assets','images','background.png'))
        #pygame.display.set_icon(image)
    def update(self):
        pass
    def run(self):
        while self.runn:
            self.handle_events()
            self.update()
            self.render()
            self.Clock.tick(self.FPS)

            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runn = False
    def render(self):
        self.displ.fill((0,0,0))
        self.game.render_objects(self.displ)
        pygame.display.update()
    
        
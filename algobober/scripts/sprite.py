import pygame
class Sprite():
    def __init__(self,image,coords):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = coords
    def render(self,displ):
        displ.blit(self.image,self.rect)
    def collide(self, other_rect):
        self.rect.colliderect(other_rect)


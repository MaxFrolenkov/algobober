import pygame
from scripts.sprite import Sprite
class Player():
    def __init__(self, image, coords,speed, jump_power, gravity):
        super().__init__(coords,image)
        self.jump_power = jump_power
        self.speed = speed
        self.gravity = gravity
        self.is_walking_r = False
        self.is_walking_l = False
        self.velocity = 0
        self.on_platform = False
    def process_key_down_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_l = True
        if key == pygame.K_d:
            self.player.is_walking_r = True
    def process_key_up_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_l = False
        if key == pygame.K_d:
            self.player.is_walking_r = False
    def update(self):
        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.rect.y += self.velocity_y

        if self.is_walking_l != self.is_walking_r:
            if self.is_walking_l:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed


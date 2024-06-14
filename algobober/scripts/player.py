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

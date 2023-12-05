# 
import pygame as pg 
from pygame.sprite import Sprite
import os
import math 
from Settings import *
from Sprites import *


class Key(Sprite):
    def __init__(self, x, y, w, h, category, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.category = color
        self.speed = 0
      
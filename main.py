# This file was created by Antonio Santana
# I am interested in game design and I would say I am passionate about the worldbuilding that comes through the music in a game 
# I am also inspired by my personal life as I have picked up guitar recently and have always loved playing rythem games and music
# My biggest inspirations would be games like guitar hero and DJ hero. 
# I can apply Python's libraries by introducing different audios and backgrounds to songs. 
# Goals:
# Rythem game 
# Make a game like guitar hero
# Have multiple stages/songs
# Have Basic controls 
# Have a score system

# Sources---------------------------------------------------------------------------------------------------------------
# https://www.youtube.com/watch?v=_AaUKSjTNY8&t=37s
# https://www.youtube.com/watch?v=u4Iq4niauCo 
# https://github.com/RuolinZheng08/renpy-minigames101 
# https://stackoverflow.com/questions/26767591/pygame-error-video-system-not-initialized
# https://www.simplilearn.com/tutorials/python-tutorial/python-for-loop#:~:text=The%20for%20loop%20in%20Python,tuple%2C%20array%2C%20or%20string.&text=The%20program%20operates%20as%20follows,item%20in%20our%20iterable%20object. 
# https://pygame.readthedocs.io/en/latest/1_intro/intro.html
# https://stackoverflow.com/questions/26767591/pygame-error-video-system-not-initialized

# Import Libraries & Moduels 
import pygame as pg 
from pygame.sprite import Sprite
import os
import math 
from Settings import *
from Sprites import *

# Display/Screen-------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True


# Strings
    class string():
        def __init__(self,x,y,color1,color2,key):
            self.x = x
            self.y = y 
            self. color1 = color1
            self. color2 = color2
            self.key = key 
            self.rect = pg.Rect(self.x,self.y,50,20)
    strings = [
    string(100,1200,(255,0,0),(220,0,0),pg.K_s),
    string(200,1200,(0,255,0),(0,220,0),pg.K_d),
    string(300,1200,(0,0,255),(0,0,220),pg.K_f),
    string(400,1200,(255,255,0),(220,220,0),pg.K_j),
    string(500,1200,(0,255,255),(0,220,220),pg.K_k),
    string(600,1200,(255,0,255),(220,0,220),pg.K_l),]
    def draw(self):
        self.screen.fill(BLACK)
        for string in strings:
            pg.draw.rect(self.screen,string.color1,string.rect)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

pg.display.update()

# etetete   
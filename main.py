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

#Mixer library allows us to get the music and play it 
from pygame import mixer

mixer.init()

# The clock is pur "tempo"/"BPM"
clock = pg.time.Clock() 

#This is the parameters of the window 

screen = pg.display.set_mode((1425, 950))

# Setting up the Background
class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('pianobg.jpg', [0,0])
# Keys/notes
class Key():
    def __init__(self,x,y,color1,color2,key):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.rect = pg.Rect(self.x,self.y,100,40)
        # determining if the key is pushed or not
        self.push = False

#List of all notes/keys

keys = [
    Key(400,800,(255,0,0),(220,0,0),pg.K_a),
    Key(500,800,(0,255,0),(0,220,0),pg.K_s),
    Key(600,800,(0,0,255),(0,0,220),pg.K_d),
    Key(700,800,(255,255,0),(220,220,0),pg.K_j),
    Key(800,800,(255,0,255),(220,0,220),pg.K_k),
    Key(900,800,(0,255,255),(0,220,220),pg.K_l),
]


#Creating the track
# This is the map we create in the "scenery.txt" file
def load(map):
    rects = []
    # loads/plays the music S
    mixer.music.load(map + ".mp3")
    mixer.music.play()
    f = open(map + ".txt", 'r')
    # This reads the lines of zero and turns them into notes on the screen 
    data = f.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0': 
              # append() attatches another element/string to the END of a list
                rects.append(pg.Rect(keys[x].rect.centerx - 25,y * -100,50,25))
    return rects
# Loading the beat map and sound, .txt file and .mp3 file
map_rect = load("Scenery")
# Background image 
bg = pg.image.load("pianobg.jpg")

#INSIDE OF THE GAME LOOP
screen.blit(bg, (1425, 900))

# While loop & ability to exit game
# Background image display
while True:
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    #This is what determines whether the key has been pressed or not, and changes the color of the key when they are pressed
    k = pg.key.get_pressed()
    for key in keys:
        if k[key.key]:
            pg.draw.rect(screen,key.color1,key.rect)
            key.push = False
        if not k[key.key]: 
            pg.draw.rect(screen,key.color2,key.rect)
            key.push = True
        
    for rect in map_rect:
      # Draws our beatmap
        pg.draw.rect(screen,(200,0,0),rect)
        rect.y += 5
        for key in keys: 
            # If the key is pressed the note will be removed 
            if key.rect.colliderect(rect) and not key.push:
                map_rect.remove(rect)
                key.push = True
                # This break causes the loop to continue unless the condition is met which is whether the key is pushed or not
                break

        

# updating the display and our tempo/rythem/bpm
    pg.display.update()
    clock.tick(60)

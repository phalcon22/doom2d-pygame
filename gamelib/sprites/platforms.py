import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.loading import *
from gamelib.sprites.sprite import *

class Doors(Sprite):
    def __init__(self, x, y, number, key):
        self.nom = "doors"
        image = DOORS[key][0]
        image.blit(DOORS[4][0], (0,0))
        Sprite.__init__(self, x ,y, image)
        self.activated = False
        self.opened = False
        self.cooldown = 66
        self.old_cooldown = 66
        self.switch = 0
        self.key = key
        self.number = number

    def update(self, player):
        if self.activated:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.old_cooldown - self.cooldown == 3:
                self.old_cooldown = self.cooldown
                self.switch += 1
        
        if self.switch == 22:
            self.opened = True
        self.image = DOORS[self.key][self.switch]
        self.image.blit(DOORS[4][self.switch], (0,0))

    def open(self):
        DOORS_SOUND.play()
        self.activated = True
    
class Arriver(Sprite):
    def __init__(self, x, y):
        self.nom = "arriver"
        Sprite.__init__(self, x ,y, SWITCH[1])
        self.activated = False
        self.cooldown = 90

    def update(self, player):
        if self.activated:
            self.cooldown -= 1
        if self.cooldown == 0:
            player.win = True

    def activate(self):
        BUTTON_SOUND.play()
        self.activated = True
        self.image = SWITCH[0]

class Tombs(Sprite):
    def __init__(self, x, y, choice):
        self.nom = "decors"
        self.image = TOMB[choice]
        Sprite.__init__(self, x ,y, TOMB[choice])

class Decors(Sprite):
    def __init__(self, x, y, choice):
        self.nom = "decors"
        Sprite.__init__(self, x ,y, DECORS[choice])


class Block(Sprite):
    def __init__(self, x, y, size):
        self.nom= "platform"
        Sprite.__init__(self, x ,y, PLATFORM[size])
    
class Platform(Sprite):
    def __init__(self, x, y, speed):
        self.nom= "moving_platform"
        Sprite.__init__(self, x ,y, PLATFORM[3])
        self.time = 180
        self.speed = speed/(1920/SCREEN_SIZE[0])

    def update(self):
        self.time -= 1
        if self.time < 0:
            self.speed = -self.speed
            self.time = 180
        self.x += self.speed
        self.rect.x = self.x

class Way(Sprite):
    def __init__(self, x, y):
        self.nom= "way"
        Sprite.__init__(self, x ,y, PLATFORM[0])

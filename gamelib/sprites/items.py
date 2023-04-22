import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.loading import *
from gamelib.sprites.sprite import *

class Key(Sprite):
    def __init__(self, x, y, key):
        Sprite.__init__(self, x ,y, KEY[key])
        self.nom = "key"
        self.key = key + 1
        
class Kit(Sprite):
    def __init__(self, x, y, name):
        self.nom = name
        if name == "ammo":
            image = AMMO
        if name == "life":
            image = LIFE
        Sprite.__init__(self, x ,y, image)
        self.movy = 0
        self.contact = False

        self.initialized = False

    def update(self, all_sprite):
        if not self.initialized:
            self.collide(all_sprite)
            self.initialized = True
            
        if not self.contact:
            self.movy += 0.5/(480/SCREEN_SIZE[0])
            self.rect.y += self.movy
            self.collide(all_sprite)

    def collide(self, all_sprite):
        for o in all_sprite:
            if self.rect.colliderect(o):
                if o.nom == "platform" or o.nom == "moving_platform" or o.nom ==   "way":
                    self.rect.bottom = o.rect.top
                    self.contact = True

class Weapon(Sprite):
    def __init__(self, x, y, number):
        self.nom = "dropweapon"
        self.rname = number
        Sprite.__init__(self, x ,y, GUNS[number-1])
        self.movy = 0
        self.contact = False

        self.initialized = False

    def update(self, all_sprite):
        if not self.initialized:
            self.collide(all_sprite)
            self.initialized = True
            
        if not self.contact:
            self.movy += 0.5/(480/SCREEN_SIZE[0])
            self.rect.y += self.movy
            self.collide(all_sprite)

    def collide(self, all_sprite):
        for o in all_sprite:
            if self.rect.colliderect(o):
                if o.nom == "platform" or o.nom == "moving_platform" or o.nom ==   "way":
                    self.rect.bottom = o.rect.top
                    self.contact = True



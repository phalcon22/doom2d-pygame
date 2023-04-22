import pygame
from pygame.locals import *
from math import *

from gamelib.config import *
from gamelib.loading import *
from gamelib.sprites.muzzles import *

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, weapon, level):
        self.frame = 0
        pygame.sprite.Sprite.__init__(self)
        self.weapon = weapon
        if weapon.nom == "weapon":
            self.nom = "bullet"
            self.vertical = weapon.direction2
            self.damages = 1
            if weapon.rname == "shotgun":
                self.damages = 5
        else:
            self.nom = "bullet2"
            self.damages = 5
            self.vertical = "none"

        self.image = BULLET[0]
        self.rect = self.image.get_rect()
        if self.vertical == "none":
            if weapon.direction == "right":
                self.rect.left = weapon.rect.right
                self.image = BULLET[0]
            if weapon.direction == "left":
                self.rect.right = weapon.rect.left
                self.image = BULLET[1]
        if self.vertical == "up":
                self.rect.centerx = weapon.rect.centerx
                self.image = BULLET[2]
        if self.vertical == "down":
                self.rect.centerx = weapon.rect.centerx
                self.image = BULLET[3]
        self.rect.centery = weapon.rect.centery
        self.direction = weapon.direction

    def update(self, camera, level):
        if not self.rect.colliderect(camera.rect):
            self.kill()

        if self.vertical == "up":
            self.rect.y -= 25/(1920/SCREEN_SIZE[0])
        if self.vertical == "down":
            self.rect.y += 25/(1920/SCREEN_SIZE[0])

        if self.vertical == "none":  
            if self.direction == "right":
                self.rect.x += 25/(1920/SCREEN_SIZE[0])
            if self.direction == "left":
                self.rect.x -= 25/(1920/SCREEN_SIZE[0])

        self.collide(level)

    def collide(self, level):
        for o in level.all_sprite:
            if self.rect.colliderect(o):

                if o.nom == "platform" or o.nom == "moving_platform" or o.nom == "way":
                    level.strikes_group.add(Strike(self)) 
                    self.kill()

                if o.nom == "imp" or o.nom == "pink" or o.nom == "zombieman":
                    level.strikes_group.add(Strike(self)) 

class Impbullet(pygame.sprite.Sprite):
    def __init__ (self, imp, level, player):
        self.frame = 0
        pygame.sprite.Sprite.__init__(self)
        self.imp = imp
        self.nom = "impbullet"

        if imp.direction == "right":
            self.image = IMPBULLET[1]
        if imp.direction == "left":
            self.image = IMPBULLET[0]
            
        self.rect = self.image.get_rect()
        self.rect.center = imp.rect.center
        self.x = self.rect.centerx
        self.y = self.rect.centery
        
        self.direction = imp.direction

        self.damages = 10
        self.speed = 15/(1920/SCREEN_SIZE[0])
        
        self.hypotenuse = sqrt((player.rect.centerx-imp.rect.centerx)**2+(player.rect.centery-imp.rect.centery)**2)
        self.movx = (player.rect.centerx-imp.rect.centerx)/self.hypotenuse*self.speed
        self.movy = (player.rect.centery-imp.rect.centery)/self.hypotenuse*self.speed

    def update(self, camera, level):
        self.x += self.movx
        self.y += self.movy
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.collide(level)

    def collide(self, level):
        for o in level.all_sprite:
            if self.rect.colliderect(o):

                if o.nom == "platform" or o.nom == "moving_platform" or o.nom == "way":
                    level.strikes_group.add(Strike(self)) 
                    self.kill()

                if o.nom == "imp" or o.nom == "pink" or o.nom == "zombieman":
                    level.strikes_group.add(Strike(self)) 

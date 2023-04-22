import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.loading import *

class Blood(pygame.sprite.Sprite):
    def __init__ (self, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.image = BLOOD
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy.rect.centerx
        self.rect.centery = enemy.rect.centery

class Rib(pygame.sprite.Sprite):
    def __init__ (self, char, movx, rib):
        pygame.sprite.Sprite.__init__(self)
        if char.nom == "player":
            self.image = PLAYERRIB[rib]
        if char.nom == "imp":
            self.image = IMPRIB[rib]
        if char.nom == "zombieman":
            self.image = ZOMBIEMANRIB[rib]
        if char.nom == "pink":
            self.image = PINKRIB[rib]
        if char.nom == "caco":
            self.image = CACORIB[rib]
        self.contact = False
        self.rect = self.image.get_rect()
        self.rect.center = char.rect.center
        self.x = char.rect.centerx
        self.y = char.rect.centery
        self.movx = movx/(480/SCREEN_SIZE[0])
        self.movy = -4/(480/SCREEN_SIZE[0])
        
        self.initialized = False

    def update(self, all_sprite):
        if not self.initialized:
            self.collide(all_sprite, "y")
            self.initialized = True
        
        self.pos_update(all_sprite)

    def pos_update(self, all_sprite):
        if not self.contact:
            self.x += self.movx
            self.rect.x = self.x
        self.collide(all_sprite, "x")

        if not self.contact:
            self.movy += 1
            self.y += self.movy
            self.rect.y = self.y
        self.collide(all_sprite, "y")
            
    def collide(self, all_sprite, orientation):
        contact = False
        movy = self.movy
        for o in all_sprite:
            if self.rect.colliderect(o):

                if o.nom == "platform" or o.nom == "moving_platform" or o.nom == "way":
                
                    if orientation == "x":
                        if self.rect.centerx > o.rect.centerx:
                            self.rect.left = o.rect.right
                            self.x = self.rect.x
                        if self.rect.centerx < o.rect.centerx:
                            self.rect.right = o.rect.left
                            self.x = self.rect.x
                        self.movx = 0

                    if orientation == "y":
                        if self.movy >= 0 or not self.initialized:
                            self.rect.bottom = o.rect.top
                            self.y = self.rect.y
                            self.movy = 0
                            contact = True
                            self.contact = True
                            if o.nom == "moving_platform":
                                self.x += o.speed
                                self.rect.x = self.x

                if o.nom == "way":
                    if orientation == "y":
                        if self.movy >= 0:
                            if self.rect.bottom < o.rect.bottom:
                                self.rect.bottom = o.rect.top
                                self.y = self.rect.y
                                self.movy = 0
                                self.contact = True
                                contact = True
                            
        if not contact and orientation == "y" and not self.contact:
            self.y -= self.movy
            self.movy -= 1
            self.movy += FALL
            self.y += self.movy
            self.rect.y = self.y
        

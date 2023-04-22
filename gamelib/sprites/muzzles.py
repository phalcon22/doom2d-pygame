import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.loading import *

class Muzzle(pygame.sprite.Sprite):
    def __init__(self, weapon, pos):
        pygame.sprite.Sprite.__init__(self)

        self.number = weapon.number
        self.image = MUZZLE_FLASH[weapon.number][pos][0]
        self.rect = self.image.get_rect()
        self.frame = 15

    def update(self, weapon, player):
        
        if self.frame > 0:
            self.frame -= 1
            if self.frame > 0:
                frame = 5
            if self.frame > 3:
                frame = 4
            if self.frame > 6:
                frame = 3
            if self.frame > 9:
                frame = 2
            if self.frame > 12:
                frame = 1
            if self.frame > 15:
                frame = 0
            
        if self.frame == 0:
            frame = 0
            self.kill()

        if player.direction2 == "none":
            if player.direction == "right":
                pos = 0
                self.rect.left = weapon.rect.right - weapon.rect.width/5
            if player.direction == "left":
                pos = 1
                self.rect.right = weapon.rect.left + weapon.rect.width/5
            self.rect.centery = weapon.rect.centery
                
        if player.direction2 == "up":
            pos = 2
            self.rect.bottom = weapon.rect.top + weapon.rect.height/5
            self.rect.centerx = weapon.rect.centerx 

        if player.direction2 == "down":
            pos = 3
            self.rect.top = weapon.rect.bottom - weapon.rect.height/5
            self.rect.centerx = weapon.rect.centerx

        self.image = MUZZLE_FLASH[self.number][pos][frame]


class Strike(pygame.sprite.Sprite):
    def __init__(self, bullet):
        pygame.sprite.Sprite.__init__(self)

        self.image = BULLET_STRIKE[0]
        self.rect = self.image.get_rect()
        self.rect.center = bullet.rect.center
        self.frame = 15

    def update(self):
        
        if self.frame > 0:
            self.frame -= 1
            if self.frame > 0:
                frame = 5
            if self.frame > 3:
                frame = 4
            if self.frame > 6:
                frame = 3
            if self.frame > 9:
                frame = 2
            if self.frame > 12:
                frame = 1
            if self.frame > 15:
                frame = 0
            
        if self.frame == 0:
            frame = 0
            self.kill()

        self.image = BULLET_STRIKE[frame]

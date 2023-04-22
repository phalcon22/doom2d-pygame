import pygame

from random import randint
from gamelib.config import *
from gamelib.sprites.bullets import *
from gamelib.sprites.ribs import *

from gamelib.enemies.enemie import *

class Imp(Enemie):
    def __init__(self, x, y, bullets_group):
        Enemie.__init__(self, x, y, IMP)
        self.health = 4
        self.damages = 5
        self.speed = 1/(480/SCREEN_SIZE[0])
        self.movx = self.speed
        self.nom = "imp"
        self.bullets_group = bullets_group
        self.hit_sound = IMPHIT_SOUND
        self.death_sound = IMPDEATH_SOUND
        self.rib = 3

    def behavior(self, all_sprite, player):
        
        self.test_wall(all_sprite)
        
        if self.attack_cooldown == 0:
            if abs(player.x - self.x)< 240/(480/SCREEN_SIZE[0]):
                self.attack_cooldown = 150
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        if self.attack_cooldown == 100:
            self.direction = self.old_direction
            self.movx = self.speed
        
        if self.attack_cooldown == 135:
            self.old_direction = self.direction
            if self.rect.centerx - player.rect.centerx > 0:
                self.direction = "left"
            if self.rect.centerx - player.rect.centerx < 0:
                self.direction = "right"
            self.movx = 0
        if self.attack_cooldown == 120:
            self.bullets_group.add(Impbullet(self, all_sprite, player))
            all_sprite.add(self.bullets_group) 
            IMPATTACK_SOUND.play()

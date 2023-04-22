import pygame

from random import randint
from gamelib.config import *
from gamelib.sprites.bullets import *
from gamelib.sprites.ribs import *

from gamelib.enemies.enemie import *

class Zombieman(Enemie):
    def __init__(self, x, y, bullets_group):
        Enemie.__init__(self, x, y, ZOMBIEMAN)
        self.health = 4
        self.damages = 5
        self.speed = 1/(480/SCREEN_SIZE[0])
        self.movx = self.speed
        self.nom = "zombieman"
        self.bullets_group = bullets_group
        self.hit_sound = ZOMBIEMANHIT_SOUND
        self.death_sound = ZOMBIEMANDEATH_SOUND
        self.rib = 3

    def behavior(self, all_sprite, player):

        self.test_wall(all_sprite)

        if self.attack_cooldown == 0:
            if abs(player.x - self.x)< 1500/(1920/SCREEN_SIZE[0]):
                if abs(player.y - self.y)< 100/(1920/SCREEN_SIZE[0]):
                    self.attack_cooldown = 150
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        if self.attack_cooldown == 100:
            self.direction = self.old_direction
            self.movx = self.speed
        
        if self.attack_cooldown == 135:
            self.old_direction = self.direction
            self.movx = 0
            if self.rect.centerx - player.rect.centerx > 0:
                self.direction = "left"
            if self.rect.centerx - player.rect.centerx < 0:
                self.direction = "right"
            
        if self.attack_cooldown == 120:
            self.bullets_group.add(Bullet(self, all_sprite))
            all_sprite.add(self.bullets_group)   
            ZOMBIEMANATTACK_SOUND.play()

import pygame

from random import randint
from gamelib.config import *
from gamelib.sprites.bullets import *
from gamelib.sprites.ribs import *

from gamelib.enemies.enemie import *

class Pink(Enemie):
    def __init__(self, x, y):
        #initialisation des attributs du Pink
        Enemie.__init__(self, x, y, PINK)
        self.health = 10
        self.damages = 5
        self.speed = 5/(1920/SCREEN_SIZE[0])
        self.movx = self.speed
        self.nom = "pink"
        self.hit_sound = PINKHIT_SOUND
        self.death_sound = PINKDEATH_SOUND
        self.rib = 4

    def behavior(self, all_sprite, player):

        self.test_jump()
    
        if player.rect.centerx - self.rect.centerx < 0:
            if player.rect.centerx - self.rect.centerx > -480/(480/SCREEN_SIZE[0]):
                self.direction = "left"
                self.movx = self.speed
                    
        if player.rect.centerx - self.rect.centerx > 0:
            if player.rect.centerx - self.rect.centerx < 480/(480/SCREEN_SIZE[0]):
                self.direction = "right"
                self.movx = self.speed
            
        if abs(player.rect.centerx - self.rect.centerx) < 100/(1920/SCREEN_SIZE[0]):
            self.movx = 0
            if self.attack_sound == 0:
                self.attack_sound = 90
                PINKATTACK_SOUND.play()
                
        if abs(player.rect.centery - self.rect.centery) >= 150/(310/SCREEN_SIZE[1]) and not player.jump_mode:
            self.movx = 0
            if abs(player.rect.centerx - self.rect.centerx) < 100/(1920/SCREEN_SIZE[0]):
                self.jump = True
        if abs(player.rect.centerx - self.rect.centerx) > 1920/(1920/SCREEN_SIZE[0]):
            self.movx = 0

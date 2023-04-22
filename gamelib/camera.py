import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.loading import *

class Camera():
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.rect.center
        self.world_rect = pygame.Rect(0, 0, level_width, level_height)

        self.lagx = 0
        self.lagy = 0

        self.lagx_max = 75
        self.lagy_max = 75

        self.rect.clamp_ip(self.world_rect)

    #FOLLOW PLAYER
    def update (self, all_sprite, game):

        if self.player.rect.centery < self.rect.centery or self.player.rect.centery > self.rect.centery:
            self.rect.centery = self.player.rect.centery + self.lagy

        if self.player.movy < 0:
            self.lagy += 0.25/(480/SCREEN_SIZE[0])
            if self.lagy > self.lagy_max:
                self.lagy = self.lagy_max
        if self.player.movy > 0:
            self.lagy += -0.25/(480/SCREEN_SIZE[0])
            if self.lagy < -self.lagy_max:
                self.lagy = -self.lagy_max
        if self.player.movy == 0:
            if self.lagy < 0:
                self.lagy += 0.75/(480/SCREEN_SIZE[0])
            if self.lagy > 0:
                self.lagy += -0.75/(480/SCREEN_SIZE[0])
                
                
        if self.player.rect.centerx < self.rect.centerx or self.player.rect.centerx > self.rect.centerx:
            self.rect.centerx = self.player.rect.centerx + self.lagx
            
        if self.player.movx < 0:
            self.lagx += 0.25/(480/SCREEN_SIZE[0])
            if self.lagx > self.lagx_max:
                self.lagx = self.lagx_max
        if self.player.movx > 0:
            self.lagx += -0.25/(480/SCREEN_SIZE[0])
            if self.lagx < -self.lagx_max:
                self.lagx = -self.lagx_max
        if self.player.movx == 0:
            if self.lagx < 0:
                self.lagx += 0.75/(480/SCREEN_SIZE[0])
            if self.lagx > 0:
                self.lagx += -0.75/(480/SCREEN_SIZE[0])

        self.rect.clamp_ip(self.world_rect)

    #SHOW GAME
    def draw_sprites(self, screen, level):

        y = 0
        for i in range(int(level.get_size()[1]/BACKGROUND.get_height())):
            y += BACKGROUND.get_height()
            x = 0
            for j in range(int(level.get_size()[0]/BACKGROUND.get_width())):
                screen.blit(BACKGROUND, (x-self.rect.x,y-self.rect.y))
                x += BACKGROUND.get_width()

        for r in (level.decors_group, level.blood_group, level.platforms_group, level.doors_group,
                  level.kits_group, level.enemy_group, level.bullets_group, level.strikes_group):
            for s in r:
                if s.rect.colliderect(self.rect):
                    screen.blit(s.image, (s.rect.x-self.rect.x, s.rect.y-self.rect.y))

        screen.blit(level.player.image, (level.player.rect.x-self.rect.x, level.player.rect.y-self.rect.y))
        screen.blit(level.player.weapon.image, (level.player.weapon.rect.x-self.rect.x, level.player.weapon.rect.y-self.rect.y))

        for s in level.muzzles_group:
            if s.rect.colliderect(self.rect):
                screen.blit(s.image, (s.rect.x-self.rect.x, s.rect.y-self.rect.y))


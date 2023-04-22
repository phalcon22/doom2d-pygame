import pygame

from gamelib.config import *
from gamelib.loading import *

class UI:
    def __init__(self, camera):
        self.camera = camera
        
    def update(self, player, screen):
        screen.blit(GUI, (0,0))

        lifebar = pygame.Surface((int((player.health/player.health_max)*84/(480/SCREEN_SIZE[0])), int(6/(310/SCREEN_SIZE[1]))))
        lifebar.fill((255,0,0))
        screen.blit(lifebar, (int(153/(480/SCREEN_SIZE[0])), int(9/(310/SCREEN_SIZE[1]))))

        ammobar = pygame.Surface((int((player.ammo/player.ammo_max)*84/(480/SCREEN_SIZE[0])), int(6/(310/SCREEN_SIZE[1]))))
        ammobar.fill((0,0,255))
        screen.blit(ammobar, (int(303/(480/SCREEN_SIZE[0])), int(9/(310/SCREEN_SIZE[1]))))
        
        y = 21
        for i in (player.health, player.ammo):
            x = FONT.render(str(i), 1, (255,255,255))
            screen.blit(x, (int(y*SCREEN_SIZE[0]/100), int(SCREEN_SIZE[1]/70)))
            y += 31

        x = 21
        for i in range(1,4):
            if player.keys[i]:
                screen.blit(GUIKEY[i-1], (int(x/(480/SCREEN_SIZE[0])), int(3/(310/SCREEN_SIZE[1]))))
            x += 16
        


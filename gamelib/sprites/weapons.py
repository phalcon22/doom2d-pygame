import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.loading import *
from gamelib.sprites.bullets import *
from gamelib.sprites.muzzles import *

class Weaponroot(pygame.sprite.Sprite):
    def __init__(self, player, name, ammo, number, sound):
        pygame.sprite.Sprite.__init__(self)
        self.nom = "weapon"
        self.rname = name
        self.ammo = ammo
        self.image = WEAPONS[1][number][0]
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
        self.direction = player.direction
        self.direction2 = player.direction2
        self.number = number
        self.sound = sound
        self.frame = 0

    def update(self, player):
        self.direction = player.direction
        self.direction2 = player.direction2
    
        if self.direction2 == "none":
            if player.state == 4:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery
                if player.frameX > 0:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])

            if player.state == 6:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery-2/(480/SCREEN_SIZE[0])
                if player.frameX == 1:
                    self.rect.y = player.rect.centery-3/(480/SCREEN_SIZE[0])
                if player.frameX == 2:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])
                if player.frameX == 3:
                    self.rect.y = player.rect.centery-2/(480/SCREEN_SIZE[0])
                if player.frameX == 4:
                    self.rect.y = player.rect.centery-3/(480/SCREEN_SIZE[0])
                if player.frameX == 5:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])

            if player.state == 3:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery-3/(480/SCREEN_SIZE[0])

            if player.state == 2:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])
                    
        if self.direction2 == "up":

            if player.state == 5:
                if player.frameX == 0:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)
                if player.frameX > 0:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)-1/(480/SCREEN_SIZE[0])

            if player.state == 3:
                if player.frameX == 0:
                    self.rect.bottom = player.rect.centery
                if player.frameX == 1:
                    self.rect.bottom = player.rect.centery+(1.1*player.rect.height/4)+4/(480/SCREEN_SIZE[0])
                if player.frameX == 2:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)-4/(480/SCREEN_SIZE[0])

            if player.state == 2:
                if player.frameX == 0:
                    self.rect.bottom = player.rect.centery
                if player.frameX == 1:
                    self.rect.bottom = player.rect.centery+(1.1*player.rect.height/4)+4/(480/SCREEN_SIZE[0])
                if player.frameX == 2:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)
                    
        if self.direction2 == "down":

            if player.state == 3:
                if player.frameX == 1:
                    self.rect.y = player.rect.centery

            if player.state == 2:
                if player.frameX == 1:
                    self.rect.y = player.rect.centery
                    
        if player.crouch:

            if player.state == 0:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery
                if player.frameX == 1:
                    self.rect.y = player.rect.centery
    
        if player.direction == "right":
            self.rect.x = player.rect.centerx

        if player.direction == "left":
            self.rect.right = player.rect.centerx
            if player.direction2 == "up":
                self.rect.centerx = player.rect.centerx
            if player.direction2 == "down":
                self.rect.centerx = player.rect.centerx

        self.animation_update(player)
        
    def animation_update(self, player):
        frame = 0
        if self.rname == "minigun":
            self.frame += 1
            if self.frame > 20: self.frame = 0
            if self.frame > 10: frame = 1
                    
        if player.direction2 == "none":
            if player.direction == "right":
                pos = 0
            if player.direction == "left":
                pos = 1
                
        if player.direction2 == "up":
            if player.direction == "right":
                pos = 2
            if player.direction == "left":
                pos = 3

        if player.direction2 == "down":
            if player.direction == "right":
                pos = 4
            if player.direction == "left":
                pos = 5

        self.image = WEAPONS[pos][self.number][frame]

    def shoot(self, player, level):
        self.sound.play()
        player.ammo -= self.ammo
        self.muzzle(player, level)
        level.bullets_group.add(Bullet(self, level.all_sprite))
        level.all_sprite.add(level.bullets_group)

    def muzzle(self, player, level):
        if player.direction2 == "none":
            if player.direction == "right":
                pos = 0
            if player.direction == "left":
                pos = 1
                
        if player.direction2 == "up":
            pos = 2

        if player.direction2 == "down":
            pos = 3

        level.muzzles_group.add(Muzzle(self, pos))



class Gun(Weaponroot):
    def __init__(self, player):
        Weaponroot.__init__(self, player, "gun", 1, 0, GUN_SOUND)

class Shotgun(Weaponroot):
    def __init__(self, player):
        Weaponroot.__init__(self, player, "shotgun", 4, 1, SHOTGUN_SOUND)

class Minigun(Weaponroot):
    def __init__(self, player):
        Weaponroot.__init__(self, player, "minigun", 1, 2, GUN_SOUND)
        

class Chainsaw(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.nom = "weapon"
        self.rname = "chainsaw"
        self.ammo = 2
        self.image = WEAPONS[1][3][0]
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
        self.direction = player.direction
        self.direction2 = player.direction2
        self.frame = 0
        self.sound = 0
        self.activated = False
        self.damages = 0
        
    def update(self, player):
        self.frame += 1
        if self.frame > 10: self.frame = 0
        self.sound += 1
        if self.sound > 80: self.sound = 0


        if self.sound == 0 or self.sound == 20 or self.sound == 40 or self.sound == 60:
            if not self.activated:
                SAWIDLE_SOUND.play()
                self.damages = 0

        if self.sound == 0:
            if self.activated:
                SAWFIRING_SOUND.play()
                player.ammo -= self.ammo
                self.damages = 0.02

        
        self.direction = player.direction
        self.direction2 = player.direction2
    
        if self.direction2 == "none":
            if player.state == 4:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery
                if player.frameX > 0:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])

            if player.state == 6:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery-2/(480/SCREEN_SIZE[0])
                if player.frameX == 1:
                    self.rect.y = player.rect.centery-3/(480/SCREEN_SIZE[0])
                if player.frameX == 2:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])
                if player.frameX == 3:
                    self.rect.y = player.rect.centery-2/(480/SCREEN_SIZE[0])
                if player.frameX == 4:
                    self.rect.y = player.rect.centery-3/(480/SCREEN_SIZE[0])
                if player.frameX == 5:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])

            if player.state == 3:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery-3/(480/SCREEN_SIZE[0])

            if player.state == 2:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery-1/(480/SCREEN_SIZE[0])
                    
        if self.direction2 == "up":

            if player.state == 5:
                if player.frameX == 0:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)
                if player.frameX > 0:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)-1/(480/SCREEN_SIZE[0])

            if player.state == 3:
                if player.frameX == 0:
                    self.rect.bottom = player.rect.centery
                if player.frameX == 1:
                    self.rect.bottom = player.rect.centery+(1.1*player.rect.height/4)+4/(480/SCREEN_SIZE[0])
                if player.frameX == 2:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)-4/(480/SCREEN_SIZE[0])

            if player.state == 2:
                if player.frameX == 0:
                    self.rect.bottom = player.rect.centery
                if player.frameX == 1:
                    self.rect.bottom = player.rect.centery+(1.1*player.rect.height/4)+4/(480/SCREEN_SIZE[0])
                if player.frameX == 2:
                    self.rect.bottom = player.rect.centery-(1.1*player.rect.height/4)
                    
        if self.direction2 == "down":

            if player.state == 3:
                if player.frameX == 1:
                    self.rect.y = player.rect.centery

            if player.state == 2:
                if player.frameX == 1:
                    self.rect.y = player.rect.centery
                    
        if player.crouch:

            if player.state == 0:
                if player.frameX == 0:
                    self.rect.y = player.rect.centery
                if player.frameX == 1:
                    self.rect.y = player.rect.centery
    
        if player.direction == "right":
            self.rect.x = player.rect.centerx

        if player.direction == "left":
            self.rect.right = player.rect.centerx
            if player.direction2 == "up":
                self.rect.centerx = player.rect.centerx
            if player.direction2 == "down":
                self.rect.centerx = player.rect.centerx

        self.animation_update(player)
        
    def animation_update(self, player):
        if self.frame > 5: frame = 1
        if self.frame <= 5: frame = 0
                    
        if player.direction2 == "none":
            if player.direction == "right":
                self.image = WEAPONS[0][3][frame]
            if player.direction == "left":
                self.image = WEAPONS[1][3][frame]
                
        if player.direction2 == "up":
            if player.direction == "right":
                self.image = WEAPONS[2][3][frame]
            if player.direction == "left":
                self.image = WEAPONS[3][3][frame]

        if player.direction2 == "down":
            if player.direction == "right":
                self.image = WEAPONS[4][3][frame]
            if player.direction == "left":
                self.image = WEAPONS[5][3][frame]


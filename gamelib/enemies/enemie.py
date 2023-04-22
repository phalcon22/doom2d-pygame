import pygame

from random import randint
from gamelib.config import *
from gamelib.sprites.bullets import *
from gamelib.sprites.ribs import *


class Enemie(pygame.sprite.Sprite):
    def __init__(self, x ,y, image):
        pygame.sprite.Sprite.__init__(self)
        self.movy = 0
        self.image = image[0][0]
        self.picture = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.attack = False
        self.attack_cooldown = 0
        self.direction = "left"
        self.old_direction = "left"
        
        self.jump = False
        self.attack_sound = 0

        self.initialized = False

    def update(self, all_sprite, player, blood_group):
        if not self.initialized:
            self.collide(all_sprite, "y")
            self.initialized = True

        self.test_gameover(player, all_sprite, blood_group)
        self.pos_update(all_sprite)
        self.behavior(all_sprite, player)
        self.animation_update()

    def pos_update(self, all_sprite):

        if self.direction == "left": 
            self.x -= self.movx
        if self.direction == "right":
            self.x += self.movx
        self.rect.x = self.x
        self.collide(all_sprite, "x")

        self.movy += 1
        self.y += self.movy
        self.rect.y = self.y
        self.collide(all_sprite, "y")
        
    def collide(self, all_sprite, orientation):
        self.chute_libre = True
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
                        self.jump = True

                    if orientation == "y":
                        if self.movy > 0 or not self.initialized:
                            self.rect.bottom = o.rect.top
                            self.y = self.rect.y
                            self.movy = 0
                            contact = True
                            self.chute_libre = False
                            if o.nom == "moving_platform":
                                self.x += o.speed
                                self.rect.x = self.x
                        if self.movy < 0:
                            contact = True
                            self.rect.top = o.rect.bottom
                            self.y = self.rect.y
                            self.movy = 0

                if o.nom == "way":
                    if orientation == "y":
                        if self.movy >= 0:
                            if self.rect.bottom < o.rect.bottom:
                                self.rect.bottom = o.rect.top
                                self.y = self.rect.y
                                self.movy = 0
                                contact = True
                                self.chute_libre = False

                if o.nom == "bullet":
                    self.hit_sound.play()
                    self.health -= o.damages
                    o.kill()

                if o.nom == "weapon":
                    if o.rname == "chainsaw":
                        if o.damages > 0:
                            self.hit_sound.play()
                            self.health -= o.damages

                if o.nom == "player":
                    if o.hit_cooldown == 0:
                        o.get_hit(self.damages)

                            
        if not contact and orientation == "y":
            self.y -= self.movy
            self.movy -= 1
            self.movy += FALL
            self.y += self.movy
            self.rect.y = self.y

    def animation_update(self):
        #DETERMINE DIRECTION
        if self.direction == "right":
            direction = 1
        if self.direction == "left":
            direction = 0

        #DETERMINE FRAME
        self.frame += 1
        if self.frame >= ANIM_ROT: self.frame = 0

        if self.frame < ANIM_ROT/4:
            frame = 0
        elif self.frame < 2*ANIM_ROT/4:
            frame = 1
        elif self.frame < 3*ANIM_ROT/4:
            frame = 2
        elif self.frame < ANIM_ROT:
            frame = 3

        if self.attack:
            frame = 4

        if self.movx == 0:
            frame = 0

        self.image = self.picture[direction][frame]

    def test_wall(self, all_sprite):
        contact = False
        self.rect.y +=1
        if self.direction == "left":
            self.rect.x -= self.rect.width
        if self.direction == "right":
            self.rect.x += self.rect.width
            
        for o in all_sprite:
            if self.rect.colliderect(o.rect):
                if o.nom == "way" or o.nom == "platform" or o.nom == "moving_platform":
                    contact = True

        if not contact:
            if self.direction == "left":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "left"

        self.rect.y = self.y
        self.rect.x = self.x

    def test_gameover(self, player, all_sprite, blood_group):         
        if self.health <= 0:
            self.death_sound.play()
            blood_group.add(Blood(self))
            for i in range(self.rib):
                blood_group.add(Rib(self, i-1, i))
            self.kill()

    
    def test_jump(self):
        if self.jump:
            self.jump = False
            if not self.chute_libre:
                self.movy = JUMP

        if self.attack_sound > 0:
            self.attack_sound -=1

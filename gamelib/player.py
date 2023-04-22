import pygame
from random import *

from gamelib.config import *
from gamelib.loading import *
from gamelib.sprites.ribs import *
from gamelib.sprites.weapons import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.nom = "player"
        self.movy = 0
        self.movx = 0
        self.jump_mode = False
        self.chute_libre = True
        self.attack_mode = False
        self.win = False
        self.game_over = False
        self.crouch = False
        self.hit_cooldown = 0
        self.attack_cooldown = 0
        self.sector = 0
        self.keys = [True, False, False, False]

        #ANIMATION INIT
        self.image = PLAYERMASK
        self.frame = 0
        self.rect = self.image.get_rect()

        #POSITION INIT
        self.direction = "right"
        self.direction2 = "none"
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

        #INIT PLAYER STATS
        self.health_max = 100
        self.health = self.health_max
        self.ammo = 50
        self.ammo_max = 100

        #INIT WEAPONS
        self.weapons = [1]

        self.initialized = False

    def update(self, up, down, left, right, attack, jump, level, camera):
        if not self.initialized:
            self.collide(level, "y")
            self.initialized = True
        
        self.test_gameover(camera)
        self.pos_update(up, down, left, right, attack, jump, level)
        self.animation_update(up, down, left, right)

    def pos_update(self, up, down ,left, right, attack, jump, level):
        
        self.direction2 = "none"
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
    
        if self.attack_cooldown == 0:
            if attack:
                if self.ammo >= self.weapon.ammo:
                    if self.weapon.rname != "chainsaw":
                        self.weapon.shoot(self, level)
                        if self.weapon.rname == "minigun":
                            self.attack_cooldown = 5
                        else:
                            self.attack_cooldown = 40
                            
        if attack:
            if self.ammo > 0:    
                if self.weapon.rname == "chainsaw":
                    self.weapon.activated = True
        if not attack:
            if self.weapon.rname == "chainsaw":
                if self.weapon.activated:
                    self.weapon.activated = False
                

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

        if not left and not right:
            if not self.chute_libre:
                self.movx = 0

        if self.crouch or up:
            self.movx = 0

        if not self.crouch and not up:
            if left:
                self.movx = -SPEED
                self.direction = "left"
            if right:
                self.movx = SPEED
                self.direction = "right"
            self.x += self.movx
            self.rect.x = self.x
        self.collide(level, "x")

        if up and not down:
            self.direction2 = "up"

        if down:
            if not self.chute_libre:
                self.rect.height = PLAYER[0][0][0].get_height()
                self.rect.y += 24/(480/SCREEN_SIZE[0])
                self.crouch = True
            if self.chute_libre:
                self.direction2 = "down"

        if not down:
            if self.crouch:
                self.rect.height = PLAYER[0][4][0].get_height()
                self.rect.y -= 24/(480/SCREEN_SIZE[0])
                self.crouch = False

        if not self.crouch:                
            if jump:
                self.jump(level.all_sprite)

        if not jump:
            if self.jump_mode:
                self.jump_mode = False
                self.movy = 0
                
        self.movy += 1
        self.rect.y += self.movy
        self.y = self.rect.y
        self.collide(level, "y", up)


    def collide(self, level, orientation, up=False):
        if orientation == "y":
            self.chute_libre = True
        contact = False
        movy = self.movy
        for o in level.all_sprite:
            if self.rect.colliderect(o):

                if o.nom == "platform" or o.nom == "moving_platform":
                
                    if orientation == "x":
                        if self.rect.centerx > o.rect.centerx:
                            self.rect.left = o.rect.right
                            self.x = self.rect.x
                        if self.rect.centerx < o.rect.centerx:
                            self.rect.right = o.rect.left
                            self.x = self.rect.x

                    if orientation == "y":
                        if self.movy > 0 or not self.initialized:
                            self.rect.bottom = o.rect.top
                            self.y = self.rect.y
                            self.movy = 0
                            contact = True
                            self.chute_libre = False
                            if self.jump_mode:
                                self.jump_mode = False
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
                                if self.jump_mode:
                                    self.jump_mode = False

                if o.nom == "bullet2" or o.nom == "impbullet":
                    if self.hit_cooldown == 0:
                        self.get_hit(o.damages)
                        o.kill()

                if o.nom == "life" or o.nom == "ammo":
                    ITEM_PICKUP_SOUND.play()
                    if o.nom == "life":
                        self.health += 30
                        if self.health > self.health_max:
                            self.health = self.health_max
                    if o.nom == "ammo":
                        self.ammo += 20
                    o.kill()

                if o.nom == "dropweapon":
                    WEAPON_PICKUP_SOUND.play()
                    self.weapons.append(o.rname)
                    o.kill()

                if o.nom == "key":
                    ITEM_PICKUP_SOUND.play()
                    self.keys[o.key] = True
                    o.kill()
                        
                            
        if not contact and orientation == "y":
            self.y -= self.movy
            self.movy -= 1
            self.movy += FALL
            self.y += self.movy
            self.rect.y = self.y

        for o in level.doors_group:
            if self.rect.colliderect(o):

                if o.nom == "doors":
                    if up:
                        if not o.activated:
                            if self.keys[o.key]:
                                o.open()
                        if o.opened:
                            self.sector += o.number
                            
                if o.nom == "arriver":
                    if up:
                        if not o.activated:
                            o.activate()
                        if o.activated:
                            self.win = True
                        

    def animation_update(self, up, down, left, right):
        
        #DETERMINE DIRECTION
        if self.direction == "right":
            direction = 0
        if self.direction == "left":
            direction = 1

        #DETERMINE ACTION
        if not left and not right:
            self.state = 4

            #FRAME
            self.frame += 1
            if self.frame >= ANIM_ROT: self.frame = 0
            
            if self.frame < ANIM_ROT/3:
                self.frameX = 0     
            elif self.frame < 2*ANIM_ROT/3:
                self.frameX = 1
            elif self.frame < ANIM_ROT:
                self.frameX = 2

        #DETERMINE ACTION  
        if left or right:
            self.state = 6
                
            #FRAME
            self.frame += 1
            if self.frame >= ANIM_ROT: self.frame = 0
            
            if self.frame < ANIM_ROT/6:
                self.frameX = 0     
            elif self.frame < 2*ANIM_ROT/6:
                self.frameX = 1
            elif self.frame < 3*ANIM_ROT/6:
                self.frameX = 2
            elif self.frame < 4*ANIM_ROT/6:
                self.frameX = 3
            elif self.frame < 5*ANIM_ROT/6:
                self.frameX = 4
            elif self.frame < ANIM_ROT:
                self.frameX = 5

        #DETERMINE ACTION
        if up:
            self.state = 5

            #FRAME
            self.frame += 1
            if self.frame >= ANIM_ROT: self.frame = 0
            
            if self.frame < ANIM_ROT/3:
                self.frameX = 0     
            elif self.frame < 2*ANIM_ROT/3:
                self.frameX = 1
            elif self.frame < ANIM_ROT:
                self.frameX = 2

        #DETERMINE ACTION
        if self.crouch:
            self.state = 0

            #FRAME
            self.frame += 1
            if self.frame >= ANIM_ROT: self.frame = 0
            
            if self.frame < ANIM_ROT/2:
                self.frameX = 0     
            elif self.frame < ANIM_ROT:
                self.frameX = 1

        #DETERMINE ACTION 
        if self.movy > 0:
            self.state = 2
            if up:
                self.frameX = 2
            if down:
                self.frameX = 1
            if not down and not up:
                self.frameX = 0

        if self.movy < 0:
            self.state = 3
            if up:
                self.frameX = 2
            if down:
                self.frameX = 1
            if not down and not up:
                self.frameX = 0
         
        self.image = PLAYER[direction][self.state][self.frameX]
            

    def test_gameover(self, camera):
        if self.rect.top > camera.world_rect.bottom:
            self.game_over = True
            
        if self.health <= 0:
            self.game_over = True

    def jump(self, all_sprite):
        if not self.chute_libre:
            self.movy = JUMP
            self.chute_libre = True
            self.jump_mode = True

    def attack(self):
        self.attack_cooldown = 30

    def get_hit(self, damages):
        HURT_SOUND.play()
        self.hit_cooldown = 120
        self.health -= damages

    def change_weapon(self, weapon, all_sprite):
        self.weapon.kill()
        if weapon == 1:
            self.weapon = Gun(self)
        if weapon == 2:
            self.weapon = Shotgun(self)
        if weapon == 3:
            self.weapon = Minigun(self)
        if weapon == 4:
            self.weapon = Chainsaw(self)
        all_sprite.add(self.weapon)        

import pygame
from pygame.locals import *

from gamelib.config import *
from gamelib.player import *

from gamelib.sprites.items import *
from gamelib.sprites.platforms import *
from gamelib.sprites.weapons import *

from gamelib.enemies.imp import *
from gamelib.enemies.pink import *
from gamelib.enemies.zombieman import *

class Level:
    def __init__(self, niveau, screen, sector=0, player=None):
        
        level = "level/level" + niveau + "_" + str(sector)
        
        self.all_sprite = pygame.sprite.Group()
        self.decors_group = pygame.sprite.Group()
        self.platforms_group = pygame.sprite.Group()
        self.doors_group = pygame.sprite.Group()
        self.blood_group = pygame.sprite.Group()
        self.kits_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.muzzles_group = pygame.sprite.Group()
        self.strikes_group = pygame.sprite.Group()        
        
        self.niveau = []
        self.sector = sector
        self.level = open(level, "r")
        self.create_level(player)

    def create_level(self, player):
        x = 0
        y = 0
        for l in self.level:
            self.niveau.append(l)

        for line in self.niveau:
            for raw in line:

                if raw == "P":
                    if self.sector == 0:
                        self.player = Player(x, y)
                        self.all_sprite.add(self.player)
                        self.player.weapon = Gun(self.player)
                        self.all_sprite.add(self.player.weapon)

                    if self.sector != 0:
                        self.player = player
                        self.all_sprite.add(self.player)
                        self.all_sprite.add(self.player.weapon)
                        self.player.rect.x = x
                        self.player.x = x
                        self.player.rect.y = y
                        self.player.y = y

                #KEY
                if raw == "f":
                    self.kits_group.add(Key(x, y, 0))
                if raw == "g":
                    self.kits_group.add(Key(x, y, 1))
                if raw == "h":
                    self.kits_group.add(Key(x, y, 2))

                #DOORS
                if raw == "A":
                    self.doors_group.add(Arriver(x, y))

                if raw == "E":
                    self.doors_group.add(Doors(x, y, 1, 0))                    
                if raw == "F":
                    self.doors_group.add(Doors(x, y, 1, 1))
                if raw == "G":
                    self.doors_group.add(Doors(x, y, 1, 2))
                if raw == "H":
                    self.doors_group.add(Doors(x, y, 1, 3))

                #TOMBS
                if raw == "t":
                    self.decors_group.add(Tombs(x, y, 0))

                if raw == "T":
                    self.decors_group.add(Tombs(x, y, 1))

                if raw == "u":
                    self.decors_group.add(Tombs(x, y, 2))

                if raw == "U":
                    self.decors_group.add(Tombs(x, y, 3))

                if raw == "v":
                    self.decors_group.add(Tombs(x, y, 4))

                #DECORS
                if raw == "q":
                    self.decors_group.add(Decors(x, y, 0))

                if raw == "Q":
                    self.decors_group.add(Decors(x, y, 1))

                if raw == "r":
                    self.decors_group.add(Decors(x, y, 2))

                if raw == "R":
                    self.decors_group.add(Decors(x, y, 3))

                if raw == "s":
                    self.decors_group.add(Decors(x, y, 4))
                    
                #PLATFORMS
                if raw == "x":
                    self.platforms_group.add(Block(x, y, 0))
                    
                if raw == "X":
                    self.platforms_group.add(Block(x, y, 1))

                if raw == "y":
                    self.platforms_group.add(Block(x, y, 2))

                if raw == "Y":
                    self.platforms_group.add(Block(x, y, 3))
                    
                if raw == "w":
                    self.platforms_group.add(Way(x, y))
                    
                if raw == "M":
                    self.platforms_group.add(Platform(x,y, 1))

                if raw == "m":
                    self.platforms_group.add(Platform(x,y, -1))

                #WEAPONS
                if raw == "2":
                    self.kits_group.add(Weapon(x, y, 2))

                if raw == "3":
                    self.kits_group.add(Weapon(x, y, 3))

                if raw == "4":
                    self.kits_group.add(Weapon(x, y, 4))

                #ENEMIES
                if raw == "O":
                    self.enemy_group.add(Pink(x,y))

                if raw == "Z":
                    self.enemy_group.add(Zombieman(x,y, self.bullets_group))

                if raw == "I":
                    self.enemy_group.add(Imp(x,y, self.bullets_group))
                    
                #KIT
                if raw == "l":
                    self.kits_group.add(Kit(x,y, "life"))
                    
                if raw == "a":
                    self.kits_group.add(Kit(x,y, "ammo")) 

                x += BLOCK_SIZE
            y += BLOCK_SIZE
            x = 0

        for i in (self.decors_group, self.platforms_group, self.doors_group, self.blood_group,
                  self.kits_group, self.enemy_group, self.bullets_group):
            self.all_sprite.add(i)

        self.get_size()

    def update(self, all_sprite, camera):
        self.player.weapon.update(self.player)
        self.platforms_group.update()
        self.bullets_group.update(camera, self)
        self.enemy_group.update(all_sprite, self.player, self.blood_group)
        self.kits_group.update(all_sprite)
        self.blood_group.update(all_sprite)
        self.doors_group.update(self.player)
        self.muzzles_group.update(self.player.weapon, self.player)
        self.strikes_group.update()

    def get_size(self):
        lines = self.niveau
        line = max(lines, key=len)
        self.width = (len(line))*BLOCK_SIZE
        self.height = (len(lines))*BLOCK_SIZE
        return (self.width, self.height)

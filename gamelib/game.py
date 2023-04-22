import pygame, sys, gamelib.main, gamelib.menu.map

from gamelib.data import *
from gamelib.camera import *
from gamelib.level import *
from gamelib.menu.main_menu import *
from gamelib.menu.pause import *
from gamelib.menu.game_over import *
from gamelib.menu.weapons import *
from gamelib.levels.level1 import *
from gamelib.UI import *

class Game:

    def __init__(self, screen, niveau):

        #JOYSTICK INIT
        self.no_controller = False
        try:
            self.controller = pygame.joystick.Joystick(0)
        except:
            self.no_controller = True

        if not self.no_controller:
            self.controller.init()

        #MUSIC INIT
        pygame.mixer.music.load("data/musics/" + str(niveau) + ".mid")
        pygame.mixer.music.play(-1)

        #GAME INIT
        self.niveau = niveau
        self.screen = screen
        self.level = Level(str(niveau), self.screen)
        self.player = self.level.player
        self.camera = Camera(self.screen, self.player, self.level.get_size()[0], self.level.get_size()[1])
        self.UI = UI(self.camera)
        self.up = self.down = self.left = self.right = self.attack = self.jump = False
        self.clock = pygame.time.Clock()

        if niveau == 0:
            self.level_script = Level1()
            
        self.update_game()

    def update_game(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_a:
                        pygame.image.save(self.screen,"data/x.jpg")
                    if event.key == K_ESCAPE:
                        self.up = self.down = self.left = self.right = self.attack = self.jump = False
                        pygame.image.save(self.screen,"data/screenshot.jpg")
                        Pause(self.screen, self)
                    if event.key == K_SPACE:
                        self.jump = True
                    if event.key == K_UP:
                        self.up = True
                    if event.key == K_DOWN:
                        self.down = True
                    if event.key == K_LEFT:
                        self.left = True
                    if event.key == K_RIGHT:
                        self.right = True
                    if event.key == K_RCTRL:
                        self.attack = True
                    if event.key == K_TAB:
                        self.up = self.down = self.left = self.right = self.attack = self.jump = False
                        pygame.image.save(self.screen,"data/screenshot.jpg")
                        SelectWeapons(self.screen, self.player, self.level.all_sprite)
                    
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        self.jump = False
                    if event.key == K_UP:
                        self.up = False
                    if event.key == K_DOWN:
                        self.down = False
                    if event.key == K_LEFT:
                        self.left = False
                    if event.key == K_RIGHT:
                        self.right = False
                    if event.key == K_RCTRL:
                        self.attack = False

                if not self.no_controller:
                    if event.type == JOYBUTTONDOWN:
                        if BUTTON[event.button] == "OPTIONS":
                            self.up = self.down = self.left = self.right = self.attack = self.jump = False
                            pygame.image.save(self.screen,"data/screenshot.jpg")
                            Pause(self.screen, self)

                        if BUTTON[event.button] == "SHARE":
                            self.up = self.down = self.left = self.right = self.attack = self.jump = False
                            pygame.image.save(self.screen,"data/screenshot.jpg")
                            SelectWeapons(self.screen, self.player, self.level.all_sprite)
                                
                        if BUTTON[event.button] == "CROSS":
                            self.jump = True
                        if BUTTON[event.button] == "R2":
                            self.attack = True

                    if event.type == JOYBUTTONUP:
                        if BUTTON[event.button] == "CROSS":
                            self.jump = False
                        if BUTTON[event.button] == "R2":
                            self.attack = False

                    if event.type == JOYHATMOTION:
                        if event.value[0] == -1:
                            self.right = False
                            self.left = True
                        if event.value[0] == 1:
                            self.left = False
                            self.right = True
                        if event.value[0] == 0:
                            self.left = False
                            self.right = False

                        if event.value[1] == -1:
                            self.up = False
                            self.down = True
                        if event.value[1] == 1:
                            self.down = False
                            self.up = True
                        if event.value[1] == 0:
                            self.up = False
                            self.down = False
                            

            if self.niveau == 0:
                self.level_script.update(self.screen, self.player, self)

            self.player.update(self.up, self.down, self.left, self.right, self.attack, self.jump, self.level, self.camera)
            self.level.update(self.level.all_sprite, self.camera)
            self.camera.update(self.level.all_sprite, self)
            self.camera.draw_sprites(self.screen, self.level)
            self.UI.update(self.player, self.screen)

            self.clock.tick(FPS)
            pygame.display.flip()

            if self.player.game_over:
                Game_over(self.screen, self.niveau)

            if self.player.win:
                self.continuer()

            if self.level.sector != self.player.sector:
                self.teleport(self.player.sector)

    def teleport(self, sector):
        #GAME REINIT
        self.up = self.down = self.left = self.right = self.attack = self.jump = False
        self.level = Level(str(self.niveau), self.screen, sector, self.player)
        self.player = self.level.player
        self.camera = Camera(self.screen, self.player, self.level.get_size()[0], self.level.get_size()[1])
        self.update_game()

    def continuer(self):
        self.up = self.down = self.left = self.right = self.attack = self.jump = False
        
        niveau = load_save()
        self.niveau += 1

        if self.niveau > niveau and self.niveau < NB_LEVEL:
            save(self.niveau)
        gamelib.menu.map.Map(screen)

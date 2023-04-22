import gamelib.game, gamelib.menu

from gamelib.menu.default_menu import *

class Map(Default_menu):

    def __init__(self, screen):
        Default_menu.__init__(self, screen)
    
        #LOAD SAVE
        set_save_folder()
        self.niveau = load_save()

        #MUSIC INIT
        pygame.mixer.music.load("data/musics/map.mid")
        pygame.mixer.music.play(-1)

        self.map = [[216,540,"up","none",-1,0],[216,470,"right","down",0,1],[288,470,"up","left",-1,1],[288,420,"left","down",1,2],
                    [168,420,"up","right",-1,2],[168,372,"up","down",2,3],[168,276,"right","down",3,4],[288,276,"up","left",-1,4],
                    [288,230,"left","down",4,5],[240,230,"up","right",-1,5],[240,182,"up","down",5,6],[240,132,"none","down",6,7]]
        
        self.frame = 0

        self.mapy = -314/(480/SCREEN_SIZE[0])

        self.playerx = 216/(480/SCREEN_SIZE[0])
        self.playery = 546/(480/SCREEN_SIZE[0])

        self.update()
        

    def draw(self):
        self.frame += 1
        if self.frame > 20: self.frame = 0

        if self.frame < 10:
            frame = 0
        if self.frame >= 10:
            frame = 1
        
        self.screen.blit(MAP, (0,self.mapy))
        self.screen.blit(MAPPLAYER[frame], (self.playerx, self.playery+self.mapy))

    def transition(self, direction):
        if direction == self.map[self.option][2]:
            if self.map[self.option][5] <= (self.niveau):
                if direction == "up":
                    y = -2
                    x = 0
                if direction == "down":
                    y = 2
                    x = 0
                if direction == "left":
                    y = 0
                    x = -2
                if direction == "right":
                    y = 0
                    x = 2

                while self.playery != self.map[self.option+1][1]/(480/SCREEN_SIZE[0]) or self.playerx != self.map[self.option+1][0]/(480/SCREEN_SIZE[0]):
                    self.clock.tick(FPS)
                    self.playerx += x/(480/SCREEN_SIZE[0])
                    self.playery += y/(480/SCREEN_SIZE[0])
                    self.mapy -= y/(480/SCREEN_SIZE[0])
                    if self.mapy > 0: self.mapy = 0
                    self.draw()
                    pygame.display.flip()
                self.option += 1

        elif direction == self.map[self.option][3]:
            if self.option-1 >= 0:
                if direction == "up":
                    y = -2
                    x = 0
                if direction == "down":
                    y = 2
                    x = 0
                if direction == "left":
                    y = 0
                    x = -2
                if direction == "right":
                    y = 0
                    x = 2
                while self.playery != self.map[self.option-1][1]/(480/SCREEN_SIZE[0]) or self.playerx != self.map[self.option-1][0]/(480/SCREEN_SIZE[0]):
                    self.clock.tick(FPS)
                    self.playerx += x/(480/SCREEN_SIZE[0])
                    self.playery += y/(480/SCREEN_SIZE[0])
                    self.mapy -= y/(480/SCREEN_SIZE[0])
                    if self.mapy < -314/(480/SCREEN_SIZE[0]): self.mapy = -314/(480/SCREEN_SIZE[0])
                    self.draw()
                    pygame.display.flip()
                self.option -= 1

    def update(self):
        while 1:
                    
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    gamelib.menu.main_menu.Main_menu(self.screen)
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                         self.transition("right")
                    if e.key == pygame.K_LEFT:
                         self.transition("left")
                    if e.key == pygame.K_UP:
                         self.transition("up")
                    if e.key == pygame.K_DOWN:
                         self.transition("down")
                    if e.key == pygame.K_RETURN:
                        if self.map[self.option][4] != -1:
                            gamelib.game.Game(self.screen, self.map[self.option][4])

                if not self.no_controller:
                    if e.type == JOYBUTTONDOWN:
                        if BUTTON[e.button] == "CROSS":
                            if self.map[self.option][4] != -1:
                                gamelib.game.Game(self.screen, self.map[self.option][4])
                        if BUTTON[e.button] == "CIRCLE":
                            gamelib.menu.main_menu.Main_menu(self.screen)
                        
                    if e.type == JOYHATMOTION:
                        if e.value[0] == 1:
                            self.transition("right")
                        if e.value[0] == -1:
                            self.transition("left")
                        if e.value[1] == 1:
                            self.transition("up")
                        if e.value[1] == -1:
                            self.transition("down")
                            
            self.display_update()

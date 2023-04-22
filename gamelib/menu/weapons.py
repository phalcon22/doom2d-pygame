from gamelib.menu.default_menu import *

class SelectWeapons(Default_menu):
    def __init__(self, screen, player, all_sprite):
        Default_menu.__init__(self, screen)
    
        self.player = player
        self.all_sprite = all_sprite

        self.screenshot()
        
        self.image = SELECT[0]

        self.weapons_list = [[235,55],[280,75],[306,145],[275,210]]
        self.weapons = []

        for i in player.weapons:
            self.weapons.append(self.weapons_list[i-1])

        self.UP = self.DOWN = self.LEFT = self.RIGHT = False

        self.update()

    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(SELECT[self.option], (0,0))

        for i in range(len(self.weapons)):
            self.screen.blit(WEAPONS[0][self.player.weapons[i]-1][0], (self.weapons[i][0]/(480/SCREEN_SIZE[0]), self.weapons[i][1]/(480/SCREEN_SIZE[0])))

        pygame.display.flip()
    def update(self):
        while 1:
            
            for e in pygame.event.get():
                if e.type == KEYUP:
                    if e.key == K_UP:
                        self.UP = False
                    if e.key == K_DOWN:
                        self.DOWN = False
                    if e.key == K_LEFT:
                        self.LEFT = False
                    if e.key == K_RIGHT:
                        self.RIGHT = False
                
                if e.type == KEYDOWN:
                    if e.key == K_UP:
                        self.UP = True
                    if e.key == K_DOWN:
                        self.DOWN = True
                    if e.key == K_LEFT:
                        self.LEFT = True
                    if e.key == K_RIGHT:
                        self.RIGHT = True

                    if e.key == K_RETURN:
                        for i in self.player.weapons:
                            if self.option == i:
                                self.player.change_weapon(self.option, self.all_sprite)
                                return
                    if e.key == K_ESCAPE:
                        return
                        

                if not self.no_controller:     
                    if e.type == JOYHATMOTION:
                        self.RIGHT = self.LEFT = self.DOWN = self.UP = False
                        if e.value[1] == 1:
                            self.UP = True
                        if e.value[1] == -1:
                            self.DOWN = True
                        if e.value[0] == -1:
                            self.LEFT = True
                        if e.value[0] == 1:
                            self.RIGHT = True

                    if e.type == JOYBUTTONDOWN:
                        if BUTTON[e.button] == "CROSS":
                            for i in self.player.weapons:
                                if self.option == i:
                                    self.player.change_weapon(self.option, self.all_sprite)
                                    return
                        if BUTTON[e.button] == "CIRCLE":
                            return

            if self.UP:
                if self.LEFT:
                    self.option = 8
                if self.RIGHT:
                    self.option = 2
                if not self.LEFT and not self.RIGHT:
                    self.option = 1
            elif self.DOWN:
                if self.LEFT:
                    self.option = 6
                if self.RIGHT:
                    self.option = 4
                if not self.LEFT and not self.RIGHT:
                    self.option = 5
            elif self.LEFT:
                self.option = 7
            elif self.RIGHT:
                self.option = 3
            else:
                self.option = 0
                
            self.display_update()

import gamelib.menu.main_menu, gamelib.game

from gamelib.menu.default_menu import *

class Game_over(Default_menu):

    def __init__(self, screen, niveau):
        Default_menu.__init__(self, screen)
    
        self.options = [["RESTART", lambda: gamelib.game.Game(screen, niveau)],
                   ["MAIN MENU", lambda: gamelib.menu.main_menu.Main_menu(self.screen)],
                   ["CONTROLS", lambda: gamelib.main.Controls(screen)],
                   ["QUIT GAME", sys.exit]]
                   
        pygame.mixer.music.stop()

        #TEXT INIT
        self.set_text()        

        self.bg = pygame.Surface(SCREEN_SIZE)
        self.bg.fill((0,0,0))
        
        self.update()         
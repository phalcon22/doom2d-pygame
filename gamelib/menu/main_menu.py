from gamelib.menu.default_menu import *
from gamelib.menu.map import *

class Main_menu(Default_menu):

    def __init__(self, screen):
        Default_menu.__init__(self, screen)
    
        self.options = [["SELECT LEVEL", lambda: Map(screen)],
                        ["CONTROLS", lambda: gamelib.main.Controls(screen)],
                        ["QUIT GAME", sys.exit]]

        self.old_option = 0
        
        pygame.mixer.music.load("data/musics/menu.mid")
        pygame.mixer.music.play(-1)

        #TEXT INIT        
        self.set_text()       

        self.bg = TITLE
        self.filter.set_alpha(100)
        
        self.update()
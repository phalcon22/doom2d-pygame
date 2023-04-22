import gamelib.menu.main_menu

from gamelib.menu.default_menu import *

class Pause(Default_menu):

    def __init__(self, screen, game):
        Default_menu.__init__(self, screen)
    
        self.options = [["CONTINUE", lambda: self.game.update_game()],
                        ["MAIN MENU", lambda: gamelib.menu.main_menu.Main_menu(self.screen)],
                        ["CONTROLS", lambda: gamelib.main.Controls(screen)],
                        ["QUIT GAME", lambda: sys.exit()]]

        self.game = game
        self.old_option = 0
        
        #TEXT INIT  
        self.set_text()  
        
        self.screenshot()
        
        self.update()






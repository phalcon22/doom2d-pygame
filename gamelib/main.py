from gamelib.menu.main_menu import*
from gamelib.cutscenes import*
#LOADS RESOURCES
from gamelib.loading import *

#SHOW MAIN MENU
def main():
    Main_menu(screen)

#SHOW CONTROLS MENU
def Controls(screen):
    cutscene(screen, ["CONTROLS",
    "",
    "Move: Arrow Keys",
    "Jump: Space",
    "Attack : Ctrl",
    "Select Weapon : Tab",
    "",
    ""])

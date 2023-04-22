import os
from gamelib.config import *

#CREATE SAVE FOLDER
def set_save_folder():
    try:
        os.makedirs((SAVE_PATH))
    except:
        pass

#CURRENT LEVEL
def load_save():
    try:
        save_file = open((SAVE_PATH + "save.sav"), "r")
        niveau = int(save_file.read())
        save_file.close()
    except:
        save()
        niveau = 0
    return niveau

#SAVE CURRENT LEVEL
def save(niveau=0):
    save_file = open((SAVE_PATH + "save.sav"), "w+")
    save_file.write(str(niveau))
    save_file.close()

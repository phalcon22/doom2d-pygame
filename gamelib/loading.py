import pygame
from pygame.locals import *
from gamelib.config import *

#SOUND INIT
pygame.mixer.pre_init(44100, -16, 2, 512)
#PYGAME INIT
pygame.init()
#SET RESOLUTION - FULLSCREEN - HARDWARE MEMORY - BUFFERING - COLORS
screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF, 32)
#MOUSE INVISIBLE
pygame.mouse.set_visible(0)
#WINDOW TITLE
pygame.display.set_caption("PyDOOM")
#WINDOW ICON
pygame.display.set_icon(pygame.image.load("Icon.ico"))

#IMPORT SCREEN LOADING FUNCTION
from gamelib.loading_screen import *

# ld IS THE PROGRESSION OF THE LOADING SCREEN
ld = 0
#SHOW THE LOADING SCREEN WITH HIS BAR
load_screen(screen, ld)

"""UI"""

GUI = pygame.image.load("data/assets/GUI/gui3_1.png").convert_alpha()
GUI = pygame.transform.scale(GUI, SCREEN_SIZE)

GUIKEY = []
l = 0
for i in ("blue", "red", "yellow"):
    GUIKEY.append(pygame.image.load("data/assets/GUI/sprite-key-" + i + "-2.png").convert_alpha())
    GUIKEY[l] = pygame.transform.scale(GUIKEY[l], (int(GUIKEY[l].get_width()/(480/SCREEN_SIZE[0])), int(GUIKEY[l].get_height()/(480/SCREEN_SIZE[0]))))
    l += 1

ld += 1
load_screen(screen, ld)

SELECT = []
for i in range(9):
    SELECT.append(pygame.image.load("data/assets/GUI/wep_select/" + str(i) + ".png").convert_alpha())
    SELECT[i] = pygame.transform.scale(SELECT[i], SCREEN_SIZE)

ld += 1
load_screen(screen, ld)

"""SYSTEM"""

ICON = pygame.image.load("Icon.ico")

FONT = pygame.font.Font(("data/fonts/font.ttf"), int(48/(1920/SCREEN_SIZE[0])))

ld += 1
load_screen(screen, ld)

"""SOUNDS"""

CLICK_SOUND = pygame.mixer.Sound("data/sounds/click.wav")

BUTTON_SOUND = pygame.mixer.Sound("data/sounds/dsswtchn.wav")
DOORS_SOUND = pygame.mixer.Sound("data/sounds/dsdoropn.wav")

ITEM_PICKUP_SOUND = pygame.mixer.Sound("data/sounds/dsitemup.wav")
WEAPON_PICKUP_SOUND = pygame.mixer.Sound("data/sounds/dswpnup.wav")
GAMEOVER_SOUND = pygame.mixer.Sound("data/sounds/dspldeth.wav")
HURT_SOUND = pygame.mixer.Sound("data/sounds/dsplpain.wav")

GUN_SOUND = pygame.mixer.Sound("data/sounds/dspistol.wav")
SHOTGUN_SOUND = pygame.mixer.Sound("data/sounds/dsshotgn.wav")
SAWIDLE_SOUND = pygame.mixer.Sound("data/sounds/dssawidl.wav")
SAWFIRING_SOUND = pygame.mixer.Sound("data/sounds/dssawful.wav")
SAWHITTING_SOUND = pygame.mixer.Sound("data/sounds/dssawhit.wav")

ZOMBIEMANHIT_SOUND = pygame.mixer.Sound("data/sounds/dspopain.wav")
ZOMBIEMANATTACK_SOUND = pygame.mixer.Sound("data/sounds/dspistol.wav")
ZOMBIEMANDEATH_SOUND = pygame.mixer.Sound("data/sounds/dspodth3.wav")

IMPHIT_SOUND = pygame.mixer.Sound("data/sounds/dspopain.wav")
IMPATTACK_SOUND = pygame.mixer.Sound("data/sounds/dsfirsht.wav")
IMPDEATH_SOUND = pygame.mixer.Sound("data/sounds/dsbgdth2.wav")

CACOHIT_SOUND = pygame.mixer.Sound("data/sounds/dsdmpain.wav")
CACOATTACK_SOUND = pygame.mixer.Sound("data/sounds/dsfirsht.wav")
CACODEATH_SOUND = pygame.mixer.Sound("data/sounds/dscacdth.wav")

PINKHIT_SOUND = pygame.mixer.Sound("data/sounds/dsdmpain.wav")
PINKATTACK_SOUND = pygame.mixer.Sound("data/sounds/dssgtatk.wav")
PINKDEATH_SOUND = pygame.mixer.Sound("data/sounds/dssgtdth.wav")

ld +=1
load_screen(screen, ld)

"""PLAYER"""

PLAYERMASK = pygame.image.load("data/assets/player/player_mask.png").convert_alpha()
PLAYERMASK = pygame.transform.scale(PLAYERMASK, (int(PLAYERMASK.get_width()/(480/SCREEN_SIZE[0])), int(PLAYERMASK.get_height()/(480/SCREEN_SIZE[0]))))

PLAYER = [[[]for j in range(7)]for i in range(2)]
z = 0
for j in range(2):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/crouch/crouch_" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))
z += 1
for j in range(9):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/death/" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))
z += 1
for j in range(3):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/fall/f-" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))
z += 1
for j in range(3):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/jump/j-" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))
z += 1
for j in range(3):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/stand/" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))
z += 1
for j in range(3):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/up/up_" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))
z += 1
for j in range(6):
    PLAYER[0][z].append(pygame.image.load("data/assets/player/walk/" + str(j+1) + ".png").convert_alpha())
    PLAYER[0][z][j] = pygame.transform.scale(PLAYER[0][z][j], (int(PLAYER[0][z][j].get_width()/(480/SCREEN_SIZE[0])), int(PLAYER[0][z][j].get_height()/(480/SCREEN_SIZE[0]))))
    PLAYER[1][z].append(pygame.transform.flip(PLAYER[0][z][j], True, False))

PLAYERRIB= []
for i in range(9):
    PLAYERRIB.append(pygame.image.load("data/assets/player/death/" + str(i+1) + ".png").convert_alpha())
    PLAYERRIB[i] = pygame.transform.scale(PLAYERRIB[i], (int(PLAYERRIB[i].get_width()/(480/SCREEN_SIZE[0])), int(PLAYERRIB[i].get_height()/(480/SCREEN_SIZE[0]))))

ld += 1
load_screen(screen, ld)

"""WEAPONS"""

WEAPONS = [[[]for i in range(4)]for i in range(6)]

WEAPONS[0][0].append(pygame.image.load("data/assets/player/weapons/1gun2.png").convert_alpha())
WEAPONS[0][1].append(pygame.image.load("data/assets/player/weapons/2shotG2.png").convert_alpha())
WEAPONS[0][2].append(pygame.image.load("data/assets/player/weapons/3minigun.png").convert_alpha())
WEAPONS[0][2].append(pygame.image.load("data/assets/player/weapons/3minigun2.png").convert_alpha())
WEAPONS[0][3].append(pygame.image.load("data/assets/player/weapons/8saw1.png").convert_alpha())
WEAPONS[0][3].append(pygame.image.load("data/assets/player/weapons/8saw2.png").convert_alpha())

WEAPONS[0][0][0] = pygame.transform.scale(WEAPONS[0][0][0], (int(WEAPONS[0][0][0].get_width()/(480/SCREEN_SIZE[0])), int(WEAPONS[0][0][0].get_height()/(480/SCREEN_SIZE[0]))))
WEAPONS[0][1][0] = pygame.transform.scale(WEAPONS[0][1][0], (int(WEAPONS[0][1][0].get_width()/(480/SCREEN_SIZE[0])), int(WEAPONS[0][1][0].get_height()/(480/SCREEN_SIZE[0]))))
WEAPONS[0][2][0] = pygame.transform.scale(WEAPONS[0][2][0], (int(WEAPONS[0][2][0].get_width()/(480/SCREEN_SIZE[0])), int(WEAPONS[0][2][0].get_height()/(480/SCREEN_SIZE[0]))))
WEAPONS[0][2][1] = pygame.transform.scale(WEAPONS[0][2][1], (int(WEAPONS[0][2][1].get_width()/(480/SCREEN_SIZE[0])), int(WEAPONS[0][2][1].get_height()/(480/SCREEN_SIZE[0]))))
WEAPONS[0][3][0] = pygame.transform.scale(WEAPONS[0][3][0], (int(WEAPONS[0][3][0].get_width()/(480/SCREEN_SIZE[0])), int(WEAPONS[0][3][0].get_height()/(480/SCREEN_SIZE[0]))))
WEAPONS[0][3][1] = pygame.transform.scale(WEAPONS[0][3][1], (int(WEAPONS[0][3][1].get_width()/(480/SCREEN_SIZE[0])), int(WEAPONS[0][3][1].get_height()/(480/SCREEN_SIZE[0]))))

WEAPONS[1][0].append(pygame.transform.flip(WEAPONS[0][0][0], True, False))
WEAPONS[1][1].append(pygame.transform.flip(WEAPONS[0][1][0], True, False))
WEAPONS[1][2].append(pygame.transform.flip(WEAPONS[0][2][0], True, False))
WEAPONS[1][2].append(pygame.transform.flip(WEAPONS[0][2][1], True, False))
WEAPONS[1][3].append(pygame.transform.flip(WEAPONS[0][3][0], True, False))
WEAPONS[1][3].append(pygame.transform.flip(WEAPONS[0][3][1], True, False))

WEAPONS[2][0].append(pygame.transform.rotate(WEAPONS[0][0][0], 90))
WEAPONS[2][1].append(pygame.transform.rotate(WEAPONS[0][1][0], 90))
WEAPONS[2][2].append(pygame.transform.rotate(WEAPONS[0][2][0], 90))
WEAPONS[2][2].append(pygame.transform.rotate(WEAPONS[0][2][1], 90))
WEAPONS[2][3].append(pygame.transform.rotate(WEAPONS[0][3][0], 90))
WEAPONS[2][3].append(pygame.transform.rotate(WEAPONS[0][3][1], 90))

WEAPONS[3][0].append(pygame.transform.flip(WEAPONS[2][0][0], True, False))
WEAPONS[3][1].append(pygame.transform.flip(WEAPONS[2][1][0], True, False))
WEAPONS[3][2].append(pygame.transform.flip(WEAPONS[2][2][0], True, False))
WEAPONS[3][2].append(pygame.transform.flip(WEAPONS[2][2][1], True, False))
WEAPONS[3][3].append(pygame.transform.flip(WEAPONS[2][3][0], True, False))
WEAPONS[3][3].append(pygame.transform.flip(WEAPONS[2][3][1], True, False))

WEAPONS[4][0].append(pygame.transform.rotate(WEAPONS[0][0][0], -90))
WEAPONS[4][1].append(pygame.transform.rotate(WEAPONS[0][1][0], -90))
WEAPONS[4][2].append(pygame.transform.rotate(WEAPONS[0][2][0], -90))
WEAPONS[4][2].append(pygame.transform.rotate(WEAPONS[0][2][1], -90))
WEAPONS[4][3].append(pygame.transform.rotate(WEAPONS[0][3][0], -90))
WEAPONS[4][3].append(pygame.transform.rotate(WEAPONS[0][3][1], -90))

WEAPONS[5][0].append(pygame.transform.flip(WEAPONS[4][0][0], True, False))
WEAPONS[5][1].append(pygame.transform.flip(WEAPONS[4][1][0], True, False))
WEAPONS[5][2].append(pygame.transform.flip(WEAPONS[4][2][0], True, False))
WEAPONS[5][2].append(pygame.transform.flip(WEAPONS[4][2][1], True, False))
WEAPONS[5][3].append(pygame.transform.flip(WEAPONS[4][3][0], True, False))
WEAPONS[5][3].append(pygame.transform.flip(WEAPONS[4][3][1], True, False))

ld += 1
load_screen(screen, ld)

"""ENEMIES"""

CACO = [[]for i in range(2)]
for j in range(3):
    CACO[0].append(pygame.image.load("data/assets/enemies/caco/caco-0" + str(j+1) + ".png").convert_alpha())
    CACO[0][j] = pygame.transform.scale(CACO[0][j], (int(CACO[0][j].get_width()/(480/SCREEN_SIZE[0])), int(CACO[0][j].get_height()/(480/SCREEN_SIZE[0]))))
    CACO[1].append(pygame.transform.flip(CACO[0][j], True, False))
CACO[0].append(pygame.image.load("data/assets/enemies/caco/caco-shoot.png").convert_alpha())
CACO[0][3] = pygame.transform.scale(CACO[0][3], (int(CACO[0][3].get_width()/(480/SCREEN_SIZE[0])), int(CACO[0][3].get_height()/(480/SCREEN_SIZE[0]))))
CACO[1].append(pygame.transform.flip(CACO[0][3], True, False))

CACORIB = []
for i in range(4):
    CACORIB.append(pygame.image.load("data/assets/enemies/caco/caco-chunk" + str(i+1) + ".png").convert_alpha())
    CACORIB[i] = pygame.transform.scale(CACORIB[i], (int(CACORIB[i].get_width()/(480/SCREEN_SIZE[0])), int(CACORIB[i].get_height()/(480/SCREEN_SIZE[0]))))

IMP = [[]for i in range(2)]
for j in range(4):
    IMP[0].append(pygame.image.load("data/assets/enemies/imp/imp-walk-" + str(j+1) + ".png").convert_alpha())
    IMP[0][j] = pygame.transform.scale(IMP[0][j], (int(IMP[0][j].get_width()/(480/SCREEN_SIZE[0])), int(IMP[0][j].get_height()/(480/SCREEN_SIZE[0]))))
    IMP[1].append(pygame.transform.flip(IMP[0][j], True, False))
IMP[0].append(pygame.image.load("data/assets/enemies/imp/imp-shoot.png").convert_alpha())
IMP[0][4] = pygame.transform.scale(IMP[0][4], (int(IMP[0][4].get_width()/(480/SCREEN_SIZE[0])), int(IMP[0][4].get_height()/(480/SCREEN_SIZE[0]))))
IMP[1].append(pygame.transform.flip(IMP[0][4], True, False))

IMPRIB = []
for i in range(3):
    IMPRIB.append(pygame.image.load("data/assets/enemies/imp/imp-chunk" + str(i+1) + ".png").convert_alpha())
    IMPRIB[i] = pygame.transform.scale(IMPRIB[i], (int(IMPRIB[i].get_width()/(480/SCREEN_SIZE[0])), int(IMPRIB[i].get_height()/(480/SCREEN_SIZE[0]))))

PINK_MASK = pygame.image.load("data/assets/enemies/pink/pink_mask.png").convert_alpha()
PINK_MASK = pygame.transform.scale(PINK_MASK, (int(PINK_MASK.get_width()/(480/SCREEN_SIZE[0])), int(PINK_MASK.get_height()/(480/SCREEN_SIZE[0]))))
PINK = [[]for i in range(2)]
for j in range(4):
    PINK[0].append(pygame.image.load("data/assets/enemies/pink/pinky-" + str(j+1) + ".png").convert_alpha())
    PINK[0][j] = pygame.transform.scale(PINK[0][j], (int(PINK[0][j].get_width()/(480/SCREEN_SIZE[0])), int(PINK[0][j].get_height()/(480/SCREEN_SIZE[0]))))
    PINK[1].append(pygame.transform.flip(PINK[0][j], True, False))

PINKRIB = []
for i in range(4):
    PINKRIB.append(pygame.image.load("data/assets/enemies/pink/pink-chunk" + str(i+1) + ".png").convert_alpha())
    PINKRIB[i] = pygame.transform.scale(PINKRIB[i], (int(PINKRIB[i].get_width()/(480/SCREEN_SIZE[0])), int(PINKRIB[i].get_height()/(480/SCREEN_SIZE[0]))))


ZOMBIEMAN = [[]for i in range(2)]
for j in range(4):
    ZOMBIEMAN[0].append(pygame.image.load("data/assets/enemies/zombieman/zombie-guy-" + str(j+1) + ".png").convert_alpha())
    ZOMBIEMAN[0][j] = pygame.transform.scale(ZOMBIEMAN[0][j], (int(ZOMBIEMAN[0][j].get_width()/(480/SCREEN_SIZE[0])), int(ZOMBIEMAN[0][j].get_height()/(480/SCREEN_SIZE[0]))))
    ZOMBIEMAN[1].append(pygame.transform.flip(ZOMBIEMAN[0][j], True, False))
ZOMBIEMAN[0].append(pygame.image.load("data/assets/enemies/zombieman/zombie-guy-shoot.png").convert_alpha())
ZOMBIEMAN[0][4] = pygame.transform.scale(ZOMBIEMAN[0][4], (int(ZOMBIEMAN[0][4].get_width()/(480/SCREEN_SIZE[0])), int(ZOMBIEMAN[0][4].get_height()/(480/SCREEN_SIZE[0]))))
ZOMBIEMAN[1].append(pygame.transform.flip(ZOMBIEMAN[0][4], True, False))

ZOMBIEMANRIB = []
for i in range(3):
    ZOMBIEMANRIB.append(pygame.image.load("data/assets/enemies/zombieman/soldier-chunk" + str(i+1) + ".png").convert_alpha())
    ZOMBIEMANRIB[i] = pygame.transform.scale(ZOMBIEMANRIB[i], (int(ZOMBIEMANRIB[i].get_width()/(480/SCREEN_SIZE[0])), int(ZOMBIEMANRIB[i].get_height()/(480/SCREEN_SIZE[0]))))

ld += 1
load_screen(screen, ld)

"""BULLETS"""

BULLET = []
BULLET.append(pygame.image.load("data/assets/enemies/zombieman/bullet.png").convert_alpha())
BULLET[0] = pygame.transform.scale(BULLET[0], (int(BULLET[0].get_width()/(480/SCREEN_SIZE[0])), int(BULLET[0].get_height()/(480/SCREEN_SIZE[0]))))
BULLET.append(pygame.transform.flip(BULLET[0], True, False))
BULLET.append(pygame.transform.rotate(BULLET[0], 90))
BULLET.append(pygame.transform.rotate(BULLET[0], -90))

IMPBULLET = []
IMPBULLET.append(pygame.image.load("data/assets/enemies/imp/sprite-bullet-imp2.png").convert_alpha())
IMPBULLET[0] = pygame.transform.scale(IMPBULLET[0], (int(IMPBULLET[0].get_width()/(480/SCREEN_SIZE[0])), int(IMPBULLET[0].get_height()/(480/SCREEN_SIZE[0]))))
IMPBULLET.append(pygame.transform.flip(IMPBULLET[0], True, False))
    
CACOBULLET = []
CACOBULLET.append(pygame.image.load("data/assets/enemies/caco/sprite-bullet-caco.png").convert_alpha())
CACOBULLET[0] = pygame.transform.scale(CACOBULLET[0], (int(CACOBULLET[0].get_width()/(480/SCREEN_SIZE[0])), int(CACOBULLET[0].get_height()/(480/SCREEN_SIZE[0]))))
CACOBULLET.append(pygame.transform.flip(CACOBULLET[0], True, False))

ld += 1
load_screen(screen, ld)


"""MUZZLE FLASH"""

MUZZLE_FLASH = [[[]for j in range(4)]for i in range(3)]
for i in range(6):
    MUZZLE_FLASH[0][0].append(pygame.image.load("data/assets/effects/muzzle flash/gun/small gun_0000" + str(i) + ".png").convert_alpha())
    MUZZLE_FLASH[0][0][i] = pygame.transform.scale(MUZZLE_FLASH[0][0][i], (int(MUZZLE_FLASH[0][0][i].get_width()/(480/SCREEN_SIZE[0])), int(MUZZLE_FLASH[0][0][i].get_height()/(480/SCREEN_SIZE[0]))))
    MUZZLE_FLASH[0][1].append(pygame.transform.flip(MUZZLE_FLASH[0][0][i], True, False))
    MUZZLE_FLASH[0][2].append(pygame.transform.rotate(MUZZLE_FLASH[0][0][i], 90))
    MUZZLE_FLASH[0][3].append(pygame.transform.rotate(MUZZLE_FLASH[0][0][i], -90))

for i in range(8):
    MUZZLE_FLASH[1][0].append(pygame.image.load("data/assets/effects/muzzle flash/shotgun/shotgun 2_0000" + str(i) + ".png").convert_alpha())
    MUZZLE_FLASH[1][0][i] = pygame.transform.scale(MUZZLE_FLASH[1][0][i], (int(MUZZLE_FLASH[1][0][i].get_width()/(480/SCREEN_SIZE[0])), int(MUZZLE_FLASH[1][0][i].get_height()/(480/SCREEN_SIZE[0]))))
    MUZZLE_FLASH[1][1].append(pygame.transform.flip(MUZZLE_FLASH[1][0][i], True, False))
    MUZZLE_FLASH[1][2].append(pygame.transform.rotate(MUZZLE_FLASH[1][0][i], 90))
    MUZZLE_FLASH[1][3].append(pygame.transform.rotate(MUZZLE_FLASH[1][0][i], -90))

for i in range(6):
    MUZZLE_FLASH[2][0].append(pygame.image.load("data/assets/effects/muzzle flash/chaingun/1gun_0000" + str(i) + ".png").convert_alpha())
    MUZZLE_FLASH[2][0][i] = pygame.transform.scale(MUZZLE_FLASH[2][0][i], (int(MUZZLE_FLASH[2][0][i].get_width()/(480/SCREEN_SIZE[0])), int(MUZZLE_FLASH[2][0][i].get_height()/(480/SCREEN_SIZE[0]))))
    MUZZLE_FLASH[2][1].append(pygame.transform.flip(MUZZLE_FLASH[2][0][i], True, False))
    MUZZLE_FLASH[2][2].append(pygame.transform.rotate(MUZZLE_FLASH[2][0][i], 90))
    MUZZLE_FLASH[2][3].append(pygame.transform.rotate(MUZZLE_FLASH[2][0][i], -90))


"""BULLET STRIKE"""

BULLET_STRIKE = []
for i in range(6):
    BULLET_STRIKE.append(pygame.image.load("data/assets/effects/bullet strike/Comp 6_0000" + str(i) + ".png").convert_alpha())
    BULLET_STRIKE[i] = pygame.transform.scale(BULLET_STRIKE[i], (int(BULLET_STRIKE[i].get_width()/(480/SCREEN_SIZE[0])), int(BULLET_STRIKE[i].get_height()/(480/SCREEN_SIZE[0]))))
    

"""DOORS"""

DOORS = [[]for i in range(5)]
l = 0
for i in ("1/", "blue/", "red/", "yellow/", "black/"):
    for j in range(23):
        DOORS[l].append(pygame.image.load("data/assets/objects/doors/" + i + str(j) + ".png").convert_alpha())
        DOORS[l][j] = pygame.transform.scale(DOORS[l][j], (int(DOORS[l][j].get_width()/(480/SCREEN_SIZE[0])), int(DOORS[l][j].get_height()/(480/SCREEN_SIZE[0]))))
    l += 1

"""BLOOD"""

BLOOD = pygame.image.load("data/assets/effects/splatters/1.png").convert_alpha()
BLOOD = pygame.transform.scale(BLOOD, (int(BLOOD.get_width()/(480/SCREEN_SIZE[0])), int(BLOOD.get_height()/(480/SCREEN_SIZE[0]))))

"""SWITCH"""

SWITCH = []
SWITCH.append(pygame.image.load("data/assets/objects/switch-03-off.png").convert_alpha())
SWITCH.append(pygame.image.load("data/assets/objects/switch-03-on.png").convert_alpha())
SWITCH[0] = pygame.transform.scale(SWITCH[0], (int(SWITCH[0].get_width()/(480/SCREEN_SIZE[0])), int(SWITCH[0].get_height()/(480/SCREEN_SIZE[0]))))
SWITCH[1] = pygame.transform.scale(SWITCH[1], (int(SWITCH[1].get_width()/(480/SCREEN_SIZE[0])), int(SWITCH[1].get_height()/(480/SCREEN_SIZE[0]))))
    
"""POWERUPS"""

GUNS = []
GUNS.append(pygame.image.load("data/assets/powerups/weapon-gun.png").convert_alpha())
GUNS.append(pygame.image.load("data/assets/powerups/weapon-shootgun.png").convert_alpha())
GUNS.append(pygame.image.load("data/assets/powerups/weapon-minigun.png").convert_alpha())
GUNS.append(pygame.image.load("data/assets/powerups/weapon-saw.png").convert_alpha())
for i in range(4):
    GUNS[i] = pygame.transform.scale(GUNS[i], (int(GUNS[i].get_width()/(480/SCREEN_SIZE[0])), int(GUNS[i].get_height()/(480/SCREEN_SIZE[0]))))

AMMO = pygame.image.load("data/assets/powerups/ammo-balas3.png").convert_alpha()
LIFE = pygame.image.load("data/assets/powerups/s_pow_hp3_0.png").convert_alpha()
AMMO = pygame.transform.scale(AMMO, (int(AMMO.get_width()/(480/SCREEN_SIZE[0])), int(AMMO.get_height()/(480/SCREEN_SIZE[0]))))
LIFE = pygame.transform.scale(LIFE, (int(LIFE.get_width()/(480/SCREEN_SIZE[0])), int(LIFE.get_height()/(480/SCREEN_SIZE[0]))))

KEY = []
l = 0
for i in ("blue", "red", "yellow"):
    KEY.append(pygame.image.load("data/assets/powerups/key-" + i + ".png").convert_alpha())
    KEY[l] = pygame.transform.scale(KEY[l], (int(KEY[l].get_width()/(480/SCREEN_SIZE[0])), int(KEY[l].get_height()/(480/SCREEN_SIZE[0]))))
    l += 1
    
ld += 1
load_screen(screen, ld)

"""MENU"""

CURSOR = pygame.image.load("data/assets/GUI/sprites_cursor_skull.png").convert_alpha()
CURSOR = pygame.transform.scale(CURSOR, (int(CURSOR.get_width()/(480/SCREEN_SIZE[0])), int(CURSOR.get_height()/(480/SCREEN_SIZE[0]))))
TITLE = pygame.image.load("data/assets/GUI/main_menu.png").convert_alpha()
TITLE = pygame.transform.scale(TITLE, SCREEN_SIZE)

MAP = pygame.image.load("data/assets/overworld/overworld-mars.png").convert_alpha()
MAP = pygame.transform.scale(MAP, (int(MAP.get_width()/(480/SCREEN_SIZE[0])), int(MAP.get_height()/(480/SCREEN_SIZE[0]))))

MAPPLAYER = []
MAPPLAYER.append(pygame.image.load("data/assets/overworld/overworld-doomguy-1.png").convert_alpha())
MAPPLAYER.append(pygame.image.load("data/assets/overworld/overworld-doomguy-2.png").convert_alpha())
MAPPLAYER[0] = pygame.transform.scale(MAPPLAYER[0], (int(MAPPLAYER[0].get_width()/(480/SCREEN_SIZE[0])), int(MAPPLAYER[0].get_height()/(310/SCREEN_SIZE[1]))))
MAPPLAYER[1] = pygame.transform.scale(MAPPLAYER[1], (int(MAPPLAYER[1].get_width()/(480/SCREEN_SIZE[0])), int(MAPPLAYER[1].get_height()/(310/SCREEN_SIZE[1]))))

"""LEVELS"""

PLATFORM = []
for i in range(4):
    PLATFORM.append(pygame.image.load("data/assets/levels/level/platform_" + str(i+1) + ".png").convert_alpha())
    PLATFORM[i] = pygame.transform.scale(PLATFORM[i], (int(PLATFORM[i].get_width()/(480/SCREEN_SIZE[0])), int(PLATFORM[i].get_height()/(310/SCREEN_SIZE[1]))))


"""DECORS"""

SWITCH = []
SWITCH.append(pygame.image.load("data/assets/objects/switch-03-on.png").convert_alpha())
SWITCH[0] = pygame.transform.scale(SWITCH[0], (int(SWITCH[0].get_width()/(480/SCREEN_SIZE[0])), int(SWITCH[0].get_height()/(310/SCREEN_SIZE[1]))))
SWITCH.append(pygame.image.load("data/assets/objects/switch-03-off.png").convert_alpha())
SWITCH[1] = pygame.transform.scale(SWITCH[1], (int(SWITCH[1].get_width()/(480/SCREEN_SIZE[0])), int(SWITCH[1].get_height()/(310/SCREEN_SIZE[1]))))

DECORS = []
for i in range(3):
    DECORS.append(pygame.image.load("data/assets/levels/level/decors_" + str(i+1) + ".png").convert_alpha())
    DECORS[i] = pygame.transform.scale(DECORS[i], (int(DECORS[i].get_width()/(480/SCREEN_SIZE[0])), int(DECORS[i].get_height()/(310/SCREEN_SIZE[1]))))
DECORS.append(pygame.image.load("data/assets/levels/level/Door_exit.png").convert_alpha())
DECORS[3] = pygame.transform.scale(DECORS[3], (int(DECORS[3].get_width()/(480/SCREEN_SIZE[0])), int(DECORS[3].get_height()/(310/SCREEN_SIZE[1]))))
DECORS.append(pygame.image.load("data/assets/levels/level/exit.png").convert_alpha())
DECORS[4] = pygame.transform.scale(DECORS[4], (int(DECORS[4].get_width()/(480/SCREEN_SIZE[0])), int(DECORS[4].get_height()/(310/SCREEN_SIZE[1]))))

TOMB = []
for i in range(5):
    TOMB.append(pygame.image.load("data/assets/levels/dod/tomb_" + str(i+1) + ".png").convert_alpha())
    TOMB[i] = pygame.transform.scale(TOMB[i], (int(TOMB[i].get_width()/(480/SCREEN_SIZE[0])), int(TOMB[i].get_height()/(310/SCREEN_SIZE[1]))))

BACKGROUND = pygame.image.load("data/assets/levels/level/Background_3.png").convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (int(BACKGROUND.get_width()/(480/SCREEN_SIZE[0])), int(BACKGROUND.get_height()/(310/SCREEN_SIZE[1]))))

ld += 1
load_screen(screen, ld)



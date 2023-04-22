import pygame, gamelib.main, sys
from pygame.locals import *

from gamelib.data import *
from gamelib.loading import *

from PIL import Image, ImageFilter

class Default_menu:

    def __init__(self, screen):
        self.screen = screen
        self.option = 0
        self.font = FONT
        self.color = [255, 0, 0]

        self.filter = pygame.Surface(SCREEN_SIZE)
        self.filter.fill((0,0,0))
        self.filter.set_alpha(0)
        
        self.clock = pygame.time.Clock()

        #JOYSTICK INIT
        self.joystick_init()

    def screenshot(self):
        img = Image.open("data/screenshot.jpg")
        im = img.filter(ImageFilter.GaussianBlur(radius=8))
        im.save("data/screenshot.jpg")
        self.bg = pygame.image.load("data/screenshot.jpg")

    def set_text(self):
        self.height = len(self.options)*self.font.get_height()
        self.width = 0
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

        self.x = SCREEN_SIZE[0]/2-(self.width/2)
        self.y = SCREEN_SIZE[1]/2-(self.height/2)

    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.filter, (0,0))
        
        i=0
        for o in self.options:
            if i==self.option:
                self.screen.blit(CURSOR, (self.x-SCREEN_SIZE[0]/12, self.y + i*(self.font.get_height()+4)))
            text = o[0]
            ren = self.font.render(text, 1, self.color)
            self.screen.blit(ren, ((self.x), self.y + i*(self.font.get_height()+4)))
            i+=1

    def joystick_init(self):
        self.no_controller = False
        try:
            self.controller = pygame.joystick.Joystick(0)
        except:
            self.no_controller = True

        if not self.no_controller:
            self.controller.init()

    def update(self):
        while 1:
            for e in pygame.event.get():

                if e.type == QUIT:
                    sys.exit()
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_DOWN or e.key == pygame.K_UP or e.key == pygame.K_RETURN:
                        CLICK_SOUND.play()
                        if e.key == pygame.K_DOWN:
                            self.option += 1
                        if e.key == pygame.K_UP:
                            self.option -= 1
                        if e.key == pygame.K_RETURN:
                            self.options[self.option][1]()               
                    if e.key == K_ESCAPE:
                        return

                if e.type == JOYBUTTONDOWN:
                    if BUTTON[e.button] == "CROSS":
                        CLICK_SOUND.play() 
                        self.options[self.option][1]()

                if e.type == JOYBUTTONDOWN:
                    if BUTTON[e.button] == "CIRCLE":
                        return

                if e.type == JOYHATMOTION:
                    if e.value[1] == 1 or e.value[1] == -1:
                        CLICK_SOUND.play()
                        if e.value[1] == 1:
                            self.option -= 1 
                        if e.value[1] == -1:
                            self.option += 1

                self.check_len()
            self.display_update()

    def check_len(self):
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

    def display_update(self):
        self.clock.tick(FPS)
        self.draw()
        pygame.display.flip()

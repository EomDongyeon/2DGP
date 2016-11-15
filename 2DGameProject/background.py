from pico2d import *

class Background:
    image1_flag = True
    image1 = None
    image2 = None
    def __init__(self):
        self.w, self.h = 800, 600
        self.bg1_X, self.bg1_Y = 0, 0
        self.bg2_X, self.bg2_Y = 0, 600
        if Background.image1 == None:
            self.image1 = load_image('resource/stage_1.png')
        if Background.image2 == None:
            self.image2 = load_image('resource/stage_1-3.png')
    def bg_moveY(self):
        if(self.bg1_Y >= -600):
            self.bg1_Y -= 50
        else:
            image1_flag = False
        if(self.bg2_Y <= 0):
            self.bg2_Y = 600
        else:
            self.bg2_Y -= 30
    def draw(self):
        self.image2.clip_draw(0, 0, 800, 1200, self.bg2_X + 400, self.bg2_Y)
        if(Background.image1_flag == True):
           self.image1.clip_draw(0, 0, 800, 600, self.bg1_X + 400, self.bg1_Y + 300)
        #self.image2.clip_draw(0,0,800,600,400,300)

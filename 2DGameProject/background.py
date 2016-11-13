from pico2d import *

class Background:
    image = None
    def __init__(self):
        self.x, self.y = 0, 0
        if Background.image == None:
            self.image = load_image('resource/stage_1.png')
    def draw(self):
        self.image.clip_draw(0,0,800,600,400,300)
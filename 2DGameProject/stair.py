from pico2d import *

import random



class Stair:
    LEFT_DIR, RIGHT_DIR = 0, 1
    i = 0
    x, y = 400, 20
    image = None
    dir = 1
    def __init__(self):
        self.num = Stair.i
        self.x, y = Stair.x, Stair.y
        self.dir = random.randint(0,1)
        if (self.dir == 0):
            self.dir = -1
        if(Stair.i == 0):
            Stair.dir = self.dir
        if((self.x + 51) >= 600):
            self.dir  = 1
        elif((self.x - 51) <= 0):
            self.dir = -1

        self.x = self.x + ((self.dir * -1) * 51)
        self.y = self.y + 27

        if Stair.image == None:
            Stair.image = load_image('resource/stair.png')

        Stair.i += 1
        Stair.x,Stair.y = self.x, self.y
        print(self.i, self.x, self.y, self.dir)

    def reset(self):
        self.num = Stair.i
        self.x, y = Stair.x, Stair.y
        self.dir = random.randint(0,1)

        if self.dir == 0:
            self.dir = -1

        if(Stair.i == 0):
            Stair.dir = self.dir

        if(self.x >= 600 or self.x <= 0):
            self.dir * -1
        self.x = self.x + ((self.dir * -1) * 51)
        self.y = self.y + 27
        if Stair.image == None:
            Stair.image = load_image('resource/stair.png')
        Stair.i += 1
        Stair.x,Stair.y = self.x, self.y


    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(0,0,50,27,self.x,self.y)
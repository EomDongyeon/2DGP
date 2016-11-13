from pico2d import *

class Timer:
    cnt_time = 0.0
    frame_image = None
    gauge_image = None
    time_speed = 25
    def __init__(self):
        self.x, self.y = 400, 570
        if Timer.frame_image == None:
            self.frame_image = load_image('resource/Time_Frame.png')
        if Timer.gauge_image == None:
            self.gauge_image = load_image('resource/time_gauge.png')
    def update(self):
        Timer.cnt_time += 0.05
    def draw(self):
        self.gauge_image.clip_draw(0, 0, 338, 54, self.x - ((Timer.cnt_time * Timer.time_speed) / 2), self.y, (300 - ((Timer.cnt_time * Timer.time_speed))), 20)
        self.frame_image.clip_draw(0,0,338,54,self.x,self.y, 300, 40)
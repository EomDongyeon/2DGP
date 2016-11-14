from pico2d import *

from character import Character


class Timer:
    cnt_time = 0.0
    frame_image = None
    gauge_image = None
    time_speed = 50
    def __init__(self):
        self.x, self.y = 400, 570
        Timer.cnt_time = 0.0
        if Timer.frame_image == None:
            self.frame_image = load_image('resource/Time_Frame.png')
        if Timer.gauge_image == None:
            self.gauge_image = load_image('resource/time_gauge.png')
    def update(self):
        Timer.cnt_time += 0.05
    def draw(self):
        cnt_gauge = Timer.cnt_time * Timer.time_speed - (Character.player_score * 20)
        if (cnt_gauge < 0):
            cnt_gauge = 0
        elif(cnt_gauge > 300):
            cnt_gauge = 300
        total_gauge = 300 - cnt_gauge
        self.gauge_image.clip_draw(0, 0, 338, 54, self.x - (cnt_gauge/2), self.y, total_gauge, 20)
        self.frame_image.clip_draw(0,0,338,54,self.x,self.y, 300, 40)

        if(total_gauge <= 0):
            Character.die_state = True
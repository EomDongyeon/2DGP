from pico2d import *
from character import Character

class Timer:
    cnt_time = 0.0
    cnt_time2 = 30.0
    TIME_ACTIVATION, TIME_STOP = 1, 0
    total_gauge = 290.0
    frame_image = None
    gauge_image = None
    gauge_stop_image = None
    time_speed = 10
    time_state = TIME_ACTIVATION
    def __init__(self):
        self.x, self.y = 400, 570
        Timer.cnt_time = 0.0
        if Timer.frame_image == None:
            self.frame_image = load_image('resource/Time_Frame.png')
        if Timer.gauge_image == None:
            self.gauge_image = load_image('resource/time_gauge.png')
        if Timer.gauge_stop_image == None:
            self.gauge_stop_image = load_image('resource/time_gauge_stop.png')
    def update(self):
        if(Timer.time_state == Timer.TIME_STOP):
            Timer.cnt_time2 -= 0.5
            if(Timer.cnt_time2 <= 0.0):
                Timer.cnt_time2 = 30.0
                Timer.time_state = Timer.TIME_ACTIVATION
        Timer.cnt_time += 0.5 * ((Timer.time_speed / 10) * Timer.time_state)
        Timer.total_gauge -= 0.5 * ((Timer.time_speed / 10) * Timer.time_state)
    def draw(self):
        # cnt_gauge = Timer.cnt_time * Timer.time_speed + ((Character.player_score) * 20)
        if (Timer.total_gauge < 0):
            Timer.total_gauge = 0
        elif(Timer.total_gauge > 290):
            Timer.total_gauge = 290
        sizeX_gauge = 250 + (Timer.total_gauge / 2)
        self.gauge_image.clip_draw(0, 0, 338, 54, sizeX_gauge, self.y, Timer.total_gauge, 20)
        self.frame_image.clip_draw(0,0,338,54, self.x,self.y, 300, 40)
        if(Timer.time_state == Timer.TIME_STOP):
            self.gauge_stop_image.clip_draw(0, 0, 51, 26, self.x, self.y)

        if(Timer.total_gauge <= 0):
            self.bgm1 = load_music('resource/sound/game_over.wav')
            self.bgm1.set_volume(10)
            self.bgm1.play(1)
            Character.die_state = True
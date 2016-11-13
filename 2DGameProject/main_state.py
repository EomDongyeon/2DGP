from pico2d import *

import random
import json
import os
import game_framework
import main_state_2
# import class
#from character import Character # import Boy class from boy.py
from stair import Stair
from background import Background
#from timer import Timer

name = "MainState"

player = None
stair = None
timer = None
bg = None
font = None
up_key = False
player_score = 0
main_time = 0.0
current_time = 0.0

class Character:
    image = None
    die_image = None
    global player_score, up_key, stair

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN, RIGHT_DIE, LEFT_DIE = 0, 1, 2, 3, 4, 5
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = 0
        self.dir = 1
        self.state = Character.LEFT_STAND
        self.total_frames = 0.0
        if(Character.image == None):
            Character.image = load_image('resource/character_sprite_05.png')
        if(Character.die_image == None):
            Character.die_image = load_image('resource/character_die_sprite(200x214).png')
    def update(self, frame_time):
        distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
    def change_dir(self, stairs):
            self.dir *= -1
    def jump(self, frame_time, stairs):
        global player_score
        if(stairs[player_score].dir == self.dir):
            if(self.dir == -1):
                self.state = Character.LEFT_RUN
                self.x = stairs[player_score].x
            else:
                self.state = Character.RIGHT_RUN
                self.x = stairs[player_score].x

            self.y = stairs[player_score].y + 100
        else:
            if (self.dir == -1):
                self.state = Character.LEFT_DIE
                self.frame = 0
                self.x = (stairs[player_score + 1].x) + ((self.dir * -1) * 51)
            else:
                self.state = Character.RIGHT_DIE
                self.frame = 0
                self.x = (stairs[player_score + 1].x) + ((self.dir * -1) * 51)
            self.y = stairs[player_score].y + 100
            player_score -= 1
    def die(self):
        pass
    def draw(self):
        if(self.state < Character.RIGHT_DIE):
            Character.TIME_PER_ACTION = 1.0
            self.image.clip_draw(self.frame * 100, self.state * 214, 100, 214, self.x, self.y)
        else:
            self.die_image.clip_draw(self.frame * 200, (self.state % 2) * 214, 200, 214, self.x, self.y,150,180)

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
        global player_score
        cnt_gauge = Timer.cnt_time * Timer.time_speed - (player_score * 20)
        if (cnt_gauge < 0):
            cnt_gauge = 0
        total_gauge = 300 - cnt_gauge
        self.gauge_image.clip_draw(0, 0, 338, 54, self.x - (cnt_gauge/2), self.y, total_gauge, 20)
        self.frame_image.clip_draw(0,0,338,54,self.x,self.y, 300, 40)

def enter():
    global player, bg, stair, stairs, player_score, timer, main_time
    bg = Background()
    player = Character()
    stair = Stair()
    stairs = [Stair() for i in range(20)]
    timer = Timer()
    running = True
    player_score = -1


def exit():
    global player, bg, stair, timer
    del(player)
    del(bg)
    del(stair)
    del(timer)


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global player_score, player, stairs
    global up_key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_q:
                player_score += 1
                current_time = get_time()
                frame_time = get_frame_time(frame_time)
                player.jump(frame_time, stairs)
                if player_score >= 20:
                    game_framework.change_state(main_state_2)
            if event.key == SDLK_w:
                player_score += 1
                player.change_dir(stairs)
                current_time = get_time()
                frame_time = get_frame_time(frame_time)
                player.jump(frame_time, stairs)
                #방향전환

current_time = 0.0

def get_frame_time(frame_time):

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def update(frame_time):
    global main_time
    main_time += 0.05

    for stair in stairs:
        stair.update()
    player.update(frame_time)
    timer.update()


def draw(frame_time):
    # global stairs, up_key, player, cnt_time
    clear_canvas()
    bg.draw()

    for stair in stairs:
        stair.draw()

    player.draw()
    timer.draw()

    font = load_font('resource/Typo_SsangmunDongB.TTF', 30)
    font.draw(20, 570, "SCORE: %d" % (player_score + 1) , (0, 0, 0))

    update_canvas()
    print('%d',player_score)
    delay(0.05)







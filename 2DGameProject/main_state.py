from pico2d import *

import random
import json
import os

import game_framework
import main_state_2
import title_state



name = "MainState"

player = None
stair = None
bg = None
font = None
up_key = False
player_score = None
current_time = 0.0


class Character:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    image = None
    global player_score, up_key, stair
    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = 0
        self.dir = 1
        self.total_frames = 0.0
        if(Character.image == None):
            Character.image = load_image('resource/character_sprite_05.png')
    def update(self, frame_time):
        distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
    def change_dir(self, stairs):
            self.dir *= -1
    def jump(self, frame_time, stairs):
        global player_score
        if(stairs[player_score].dir == self.dir):
            if(self.dir == 1):
                self.x = stairs[player_score].x
            else:
                self.x = stairs[player_score].x
            self.y = stairs[player_score].y + 100
        else:
            player_score -= 1
    def draw(self):
        if self.dir == -1:
            self.state = 3
        else:
             self.state = 2
        self.image.clip_draw(self.frame * 100, self.state * 214,100,214,self.x,self.y)

class Background:
    image = None
    def __init__(self):
        self.x, self.y = 0, 0
        if Background.image == None:
            self.image = load_image('resource/stage_1.png')
    def draw(self):
        self.image.clip_draw(0,0,800,600,400,300)

class Stair:
    LEFT_DIR, RIGHT_DIR = 0, 1
    i = 0
    x,y = 400, 20
    image = None
    dir = 1
    def __init__(self):
        self.num = Stair.i
        self.x,y = Stair.x, Stair.y
        self.dir = random.randint(0,1)
        if self.dir == 0:
            self.dir = -1

        if(Stair.i == 0):
            Stair.dir = self.dir
        if(self.x >= 600 or self.x <= 0):
            self.dir *= -1
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


def enter():
    global player, bg, stair, stairs, player_score
    bg = Background()
    player = Character()
    stair = Stair()
    stairs = [Stair() for i in range(20)]
    running = True
    player_score = -1


def exit():
    global player, bg, stair
    del(player)
    del(bg)
    del(stair)



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
    global stairs
    global player_score, current_time
    global up_key
    for stair in stairs:
        stair.update()
    player.update(frame_time)

def draw(frame_time):
    global stairs, up_key, player
    clear_canvas()
    bg.draw()

    for stair in stairs:
        stair.draw()

    player.draw()

    font = load_font('ENCR10B.TTF', 30)
    font.draw(600, 570, "SCORE: %d" % (player_score + 1) , (0, 0, 0))


    update_canvas()
    print('%d',player_score)
    delay(0.05)





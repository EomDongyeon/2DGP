from pico2d import *

import random
import json
import os
import game_framework
import gameover_state
# import class
from character import Character # import Boy class from boy.py
from stair import Stair
from background import Background
from timer import Timer
from score import score_check

name = "Stage1"

player = None
stair = None
timer = None
bg = None
font = None
up_key = False
main_time = 0.0
current_time = 0.0

def enter():
    global player, bg, stair, stairs, timer, main_time
    bg = Background()
    player = Character()
    stair = Stair()
    stairs = [Stair() for i in range(20)]
    timer = Timer()
    running = True


def exit():
    global player, bg, stair, timer, stairs
    del(player)
    del(bg)
    del(stair)
    del (stairs)
    del(timer)


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global player, stairs,up_key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_q:
                Character.player_score += 1
                if (Character.player_score < 20):
                    current_time = get_time()
                    frame_time = get_frame_time(frame_time)
                    player.jump(frame_time, stairs)
            if event.key == SDLK_w: #방향전환
                Character.player_score += 1
                if (Character.player_score < 20):
                    player.change_dir(stairs)
                    current_time = get_time()
                    frame_time = get_frame_time(frame_time)
                    player.jump(frame_time, stairs)


current_time = 0.0

def get_frame_time(frame_time):

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def update(frame_time):
    global main_time
    main_time += 0.05
    if (Character.player_score >= 20):
        Character.player_score = 0
        game_framework.push_state(gameover_state)
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
    font.draw(20, 570, "SCORE: %d" % (Character.player_score + 1) , (0, 0, 0))

    update_canvas()
    print('%d', Character.player_score)
    delay(0.05)







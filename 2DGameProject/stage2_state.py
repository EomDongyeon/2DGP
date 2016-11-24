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

name = "Stage2"

player = None
stair = None
stairs = None
timer = None
bg = None
font = None
up_key = False
main_time = 0.0
current_time = 0.0

def enter():
    global player, bg, stairs, timer, main_time
    bg = Background()
    stairs = [Stair() for i in range(100)]
    player = Character(stairs)
    timer = Timer()
    main_time = 0.0
    current_time = 0.0
    running = True

def exit():
    global player, bg, timer, stairs
    del(player)
    del(bg)
    del(stairs)
    #del(timer)


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global player, bg, stairs, up_key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_q:
                Character.player_score += 1
                if (Character.player_score < 100):
                    current_time = get_time()
                    frame_time = get_frame_time(frame_time)
                    player.jump(frame_time, stairs)
                    if (Character.player_score >= 5):
                        bg.bg_moveY()
                        for stair in stairs:
                            stair.moveY()
                        player.moveY(stairs)
            if event.key == SDLK_w: #방향전환
                Character.player_score += 1
                if (Character.player_score < 100):
                    player.change_dir(stairs)
                    current_time = get_time()
                    frame_time = get_frame_time(frame_time)
                    player.jump(frame_time, stairs)
                    if (Character.player_score >= 5):
                        bg.bg_moveY()
                        for stair in stairs:
                            stair.moveY()
                        player.moveY(stairs)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_q:
                Character.jump_key = True
            if event.key == SDLK_w:
                Character.jump_key = True

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

    player.update(frame_time,stairs)
    timer.update()

    if (Character.player_score >= 100):
        Character.player_score = 0
        game_framework.push_state(gameover_state)


def draw(frame_time):
    global stair, stairs, up_key, player, cnt_time, timer
    clear_canvas()
    bg.draw()

    for stair in stairs:
        stair.draw()

    player.draw()
    timer.draw()

    font = load_font('resource/Typo_SsangmunDongB.TTF', 30)
    font.draw(20, 570, "SCORE: %d" % (Character.player_score) , (0, 0, 0))

    update_canvas()

    delay(0.05)







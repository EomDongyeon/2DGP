from pico2d import *

import random
import json
import os
import game_framework
import stage2_intro_state
import gameover_state
# import class
from character import Character # import Boy class from boy.py
from stair import Stair
from background import Background
from item import Item
from timer import Timer
from score import score_check

name = "Stage1"

player = None
stair = None
stairs = None
timer = None
item = None
bg = None
font = None
up_key = False
main_time = 0.0
current_time = 0.0


def enter():
    global player, bg, stairs, timer, current_time, main_time, item
    bg = Background()
    item = Item()
    stairs = [Stair() for i in range(100)]
    print("계단생성")
    player = Character(stairs)
    timer = Timer()
    main_time = 0.0
    current_time = 0.0
    running = True
    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()
    if(info_data[-1]['item_life'] == True):
        Character.life_state = True

def exit():
    global player, bg, stairs
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
                if(Timer.time_state == Timer.TIME_ACTIVATION):
                    Timer.total_gauge += 10
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
                if(Timer.time_state == Timer.TIME_ACTIVATION):
                    Timer.total_gauge += 10
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
            if event.key == SDLK_F1:
                f = open('data/player_info_data.txt', 'r')
                info_data = json.load(f)
                f.close()
                info_data[-1]['item_life'] = False
                f = open('data/player_info_data.txt', 'w')
                json.dump(info_data, f)
                f.close()

            if event.key == SDLK_F2:
                f = open('data/player_info_data.txt', 'r')
                info_data = json.load(f)
                f.close()
                if(info_data[-1]['item_stop'] == True):
                    Timer.time_state = Timer.TIME_STOP
                    info_data[-1]['item_stop'] = False
                f = open('data/player_info_data.txt', 'w')
                json.dump(info_data, f)
                f.close()

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

    if (Character.player_score >= 30):
        Character.player_score = 0
        game_framework.push_state(stage2_intro_state)


def draw(frame_time):
    global stair, stairs, up_key, player, cnt_time, timer, item
    clear_canvas()
    bg.draw(2)

    for stair in stairs:
        stair.draw()

    player.draw()
    timer.draw()
    item.draw()

    font = load_font('resource/Typo_SsangmunDongB.TTF', 30)
    font.draw(20, 570, "SCORE: %d" % (Character.player_score) , (0, 0, 0))

    update_canvas()

    delay(0.05)







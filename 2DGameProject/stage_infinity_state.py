from pico2d import *

import random
import json
import os
import game_framework
import best_score_state
import gameover_state
import intinity_itemshop_state
# import class
from character import Character
from stair import Stair
from background import Background
from item import Item
from timer import Timer

name = "Stage1"

player = None
stair = None
stairs = list()
timer = None
item = None
bg = None
font = None
up_key = False
best_score = 0
main_time = 0.0
current_time = 0.0


def enter():
    global player, bg, stairs, timer, current_time, main_time, item, best_score
    bg = Background()
    item = Item()
    stairs = [Stair() for i in range(10)]
    player = Character(stairs)
    Character.infinity_state = True
    timer = Timer()
    timer.reset()
    main_time = 0.0
    current_time = 0.0
    running = True
    # 파일 출력
    f = open('data/infinity_player_data.txt', 'r')
    infinity_player_data = json.load(f)
    f.close()

    infinity_player_data.append({'score': 0, 'money': 300, 'item_life': False, 'item_stop': False })

    # 파일 쓰기
    f = open('data/infinity_player_data.txt', 'w')
    json.dump(infinity_player_data, f)
    f.close()

    if(infinity_player_data[-1]['item_life'] == True):
        Character.life_state = True

    f = open('data/best_score_data.txt', 'r')
    best_score_data = json.load(f)
    f.close()
    best_score = best_score_data['best_score']



def exit():
    global player, bg, stairs, timer, current_time, main_time, item
    del(player)
    del(bg)
    del(stairs)
    del(item)
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
                f = open('data/infinity_player_data.txt', 'r')
                infinity_player_data = json.load(f)
                f.close()
                infinity_player_data[-1]['item_life'] = False
                f = open('data/infinity_player_data.txt', 'w')
                json.dump(infinity_player_data, f)
                f.close()

            if event.key == SDLK_F2:
                f = open('data/infinity_player_data.txt', 'r')
                infinity_player_data = json.load(f)
                f.close()
                if(infinity_player_data[-1]['item_stop'] == True):
                    Timer.time_state = Timer.TIME_STOP
                    infinity_player_data[-1]['item_stop'] = False
                f = open('data/infinity_player_data.txt', 'w')
                json.dump(infinity_player_data, f)
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
    global main_time,stairs,player,bg
    main_time += 0.05
    for stair in stairs:
        stair.update()

    print("계단 %d" % Stair.i)
    if(Character.player_score >= ((Stair.i / 2) - 1)):
        for i in range(100):
            stairs.append(Stair())

    player.update(frame_time,stairs)
    timer.update()

    if (Character.player_score >= 799):
        # 계단 추가하기.
        pass



def draw(frame_time):
    global stair, stairs, up_key, player, cnt_time, timer, item, best_score
    clear_canvas()
    bg.draw(3)

    for stair in stairs:
        if(stair.num == best_score):
            stair.draw(3)
        else:
            stair.draw(0)

    player.draw()
    timer.draw()
    item.draw()

    font = load_font('resource/Typo_SsangmunDongB.TTF', 30)
    font.draw(20, 570, "SCORE: %d" % (Character.player_score) , (0, 0, 0))

    update_canvas()

    delay(0.05)







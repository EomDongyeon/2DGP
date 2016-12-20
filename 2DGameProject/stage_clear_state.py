import game_framework
import stage2_intro_state
import stage3_intro_state
from sound import GameSound
from pico2d import *


name = "Stage_Clear"
image1 = None
image2 = None
sound = GameSound()
load_num = 0
logo_time = 0.0


def enter():
    global image1, info_data
    image1 = load_image('resource/stage_clear.png')
    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()
    total_money()
    GameSound.sound_state = GameSound.CLEAR
    sound.play(GameSound.CLEAR)

def total_money():
    global info_data
    if (info_data[-1]['stage'] == 2):
        info_data[-1]['money'] += info_data[-1]['score1']
    elif (info_data[-1]['stage'] == 3):
        info_data[-1]['money'] += info_data[-1]['score2']
    f = open('data/player_info_data.txt', 'w')
    json.dump(info_data, f)
    f.close()


def exit():
    global image1
    del(image1)
    close_canvas()


def update(frame_time):
    global logo_time,load_num,info_data
    if (logo_time > 1.5):
        logo_time = 0
        if(info_data[-1]['stage'] == 2):
            game_framework.push_state(stage2_intro_state)
        elif(info_data[-1]['stage'] == 3):
            game_framework.push_state(stage3_intro_state)

    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image1
    clear_canvas()
    image1.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass





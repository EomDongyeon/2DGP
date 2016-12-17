import game_framework
import stage1_state

from pico2d import *


name = "Stage2_Intro"
image1 = None
image2 = None
load_num = 0
logo_time = 0.0

def enter():
    global image1, image2
    image1 = load_image('resource/stage_2.png')
    image2 = load_image('resource/stage_2-2.png')



def exit():
    global image1, image2
    del(image1)
    del(image2)
    close_canvas()


def update(frame_time):
    global logo_time
    global load_num
    if (logo_time > 0.3 and logo_time < 1.0):
        load_num = 1
    elif (logo_time > 1.5):
        logo_time = 0
        game_framework.push_state(stage1_state)

    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image1,image2, load_num
    clear_canvas()
    if(load_num == 0):
         image1.draw(400, 300)
    else:
        image2.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass





import game_framework
import home_state

from sound import GameSound
from pico2d import *


name = "Stage_Win"
image1 = None
image2 = None
sound = GameSound()
load_num = 0
logo_time = 0.0


def enter():
    global image1, image2, info_data
    image1 = load_image('resource/game_win.png')
    image2 = load_image('resource/game_win-2.png')
    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()
    total_money()
    GameSound.sound_state = GameSound.WIN
    sound.play(GameSound.WIN)

def total_money():
    global info_data
    info_data[-1]['money'] += info_data[-1]['score3']
    f = open('data/player_info_data.txt', 'w')
    json.dump(info_data, f)
    f.close()

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
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                select_sound = load_wav('resource/sound/itemize.wav')
                select_sound.set_volume(50)
                select_sound.play(1)
                delay(0.3)
                GameSound.sound_state = GameSound.BG
                sound.play(GameSound.BG)
                game_framework.push_state(home_state)


def pause(): pass


def resume(): pass





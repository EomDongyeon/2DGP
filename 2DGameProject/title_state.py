import game_framework
import stage1_intro_state
from pico2d import *


name = "TitleState"
image = None
bgm = None

def enter():
    global image, bgm
    bgm = load_music('resource/sound/bgm.mp3')
    bgm.set_volume(3)
    bgm.repeat_play()
    image = load_image('resource/title.png')


def exit():
    global image, bgm
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(stage1_intro_state)



def draw(frame_time):
    global bgm
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update(frame_time):
    global bgm
    pass


def pause():
    pass


def resume():
    pass







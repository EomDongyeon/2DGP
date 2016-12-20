import game_framework
import home_state
from sound import GameSound
from pico2d import *


name = "TitleState"
image = None
sound = GameSound()

def enter():
    global image, bgm
    GameSound.sound_state = GameSound.BG
    sound.play(GameSound.BG)
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
                game_framework.push_state(home_state)



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







import game_framework
import home_state
from sound import GameSound
from pico2d import *





name = "Tutorial State"
bg_image = None
board_image = None
score_data = None
select_image = None
key_num = 0
font = 0
sound = GameSound()


def enter():
    global bg_image, select_image, info_data
    bg_image = load_image('resource/tutorial.png')

def exit():
    global bg_image, select_image, info_data
    del(bg_image)
    del(select_image)




def handle_events(frame_time):
    global key_num, info_data, sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                select_sound = load_wav('resource/sound/itemize.wav')
                select_sound.set_volume(50)
                select_sound.play(1)
                delay(0.3)
                game_framework.push_state(home_state)



def draw(frame_time):
    global font, key_num, info_data
    clear_canvas()
    bg_image.draw(400, 300)

    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







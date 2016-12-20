import game_framework
import stage1_intro_state
import itemshop_state
import tutorial_state
import stage_infinity_intro_state
from sound import GameSound
from pico2d import *





name = "GameOverState"
bg_image = None
board_image = None
score_data = None
select_image = None
key_num = 0
font = 0
sound = GameSound()


def enter():
    global bg_image, select_image, info_data
    bg_image = load_image('resource/start_menu.png')
    select_image = load_image('resource/sel.png')

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
                game_framework.quit()
            if (event.key == SDLK_UP or event.key == SDLK_LEFT): # 아이템샵
                if(key_num > 0):
                    key_num -= 1
            if (event.key == SDLK_DOWN or event.key == SDLK_RIGHT) : # 게임시작
                if (key_num < 3):
                    key_num += 1
            if event.key == SDLK_SPACE:
                select_sound = load_wav('resource/sound/itemize.wav')
                select_sound.set_volume(50)
                select_sound.play(1)
                delay(0.3)
                if(key_num == 0):
                    GameSound.sound_state = GameSound.BG
                    sound.play(GameSound.BG)
                    game_framework.push_state(stage1_intro_state)
                elif(key_num == 1):
                    game_framework.push_state(itemshop_state)
                elif(key_num == 2):
                    game_framework.push_state(tutorial_state)
                elif (key_num == 3):
                    GameSound.sound_state = GameSound.BG
                    sound.play(GameSound.BG)
                    game_framework.push_state(stage_infinity_intro_state)


def draw(frame_time):
    global font, key_num, info_data
    clear_canvas()
    bg_image.draw(400, 300)

    if(key_num == 0):
        select_image.draw(400, 400)
    elif(key_num == 1):
         select_image.draw(400, 300)
    elif(key_num == 2):
         select_image.draw(400, 190)
    elif(key_num == 3):
         select_image.draw(400, 100)

    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







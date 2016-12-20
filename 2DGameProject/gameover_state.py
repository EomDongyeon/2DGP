import game_framework
import stage1_intro_state
import stage2_intro_state
import stage3_intro_state
import itemshop_state
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
    global bg_image, board_image, select_image, info_data
    bg_image = load_image('resource/default_bg.png')
    board_image = load_image('resource/score_board.png')
    select_image = load_image('resource/sel.png')
    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()
    total_money()

def exit():
    global bg_image, board_image, select_image, info_data
    del(bg_image)
    del(board_image)
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
            if event.key == SDLK_LEFT: # 아이템샵
                key_num = 0
            if event.key == SDLK_RIGHT: # 게임시작
                key_num = 1
            if event.key == SDLK_SPACE:
                select_sound = load_wav('resource/sound/itemize.wav')
                select_sound.set_volume(50)
                select_sound.play(1)
                delay(0.3)
                if(key_num == 0):
                    game_framework.change_state(itemshop_state)
                else:
                    GameSound.sound_state = GameSound.BG
                    sound.play(GameSound.BG)
                    if (info_data[-1]['stage'] == 1):
                        game_framework.change_state(stage1_intro_state)
                    elif (info_data[-1]['stage'] == 2):
                        info_data[-1]['money'] += info_data[-1]['score2']
                        game_framework.change_state(stage2_intro_state)
                    elif (info_data[-1]['stage'] == 3):
                        info_data[-1]['money'] += info_data[-1]['score3']
                        game_framework.change_state(stage3_intro_state)

def total_money():
    global info_data
    if (info_data[-1]['stage'] == 1):
        info_data[-1]['money'] += info_data[-1]['score1']
    elif (info_data[-1]['stage'] == 2):
        info_data[-1]['money'] += info_data[-1]['score2']
    elif (info_data[-1]['stage'] == 3):
        info_data[-1]['money'] += info_data[-1]['score3']
    f = open('data/player_info_data.txt', 'w')
    json.dump(info_data, f)
    f.close()

def score_check(num):      # 게임 스코어 및 게임 머니 체크
    Num = []
    temp_num = num
    count = 0
    while temp_num > 0:
        Num.append(int(temp_num % 10))
        temp_num = int(temp_num / 10)
        count += 1
    return Num

def draw(frame_time):
    global font, key_num, info_data
    clear_canvas()
    bg_image.draw(400, 300)
    board_image.draw(400, 300)

    font = load_font('resource/Typo_SsangmunDongB.TTF', 50)
    if(info_data[-1]['stage'] == 1):
        font.draw(380, 340, "%d" % (info_data[-1]['score1']) , (0, 0, 0))
    elif(info_data[-1]['stage'] == 2):
        font.draw(380, 340, "%d" % (info_data[-1]['score2']) , (0, 0, 0))
    elif(info_data[-1]['stage'] == 3):
        font.draw(380, 340, "%d" % (info_data[-1]['score3']) , (0, 0, 0))

    if(key_num == 0):
        select_image.draw(320, 170)
    elif(key_num == 1):
         select_image.draw(520, 170)

    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







import game_framework
import home_state

from pico2d import *


name = "ItemShopState"
bg_image = None
board_image = None
select_image = None
coin_image = None
coin_sound = None
info_data = None
key_num = 0
font = 0

def enter():
    global bg_image, board_image, select_image, coin_image,info_data
    bg_image = load_image('resource/default_bg.png')
    board_image = load_image('resource/store_menu.png')
    select_image = load_image('resource/sel.png')
    coin_image = load_image('resource/coin.png')

    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()


def exit():
    global bg_image, board_image, select_image, coin_image
    del(bg_image)
    del(board_image)
    del(select_image)
    del(coin_image)


def handle_events(frame_time):
    global key_num, info_data
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_LEFT: # 아이템샵
                if(key_num > 0):
                    key_num -= 1
            if event.key == SDLK_RIGHT: # 게임시작
                if (key_num < 4):
                 key_num += 1
            if event.key == SDLK_SPACE:
                select_sound = load_wav('resource/sound/itemize.wav')
                select_sound.set_volume(50)
                if (key_num == 0):
                    # 아이템구입 생명력
                    item_purchase(key_num)
                if (key_num == 1):
                    # 아이템구입 시간멈추기
                    item_purchase(key_num)
                elif(key_num == 2):
                    select_sound.play(1)
                    delay(0.3)
                    game_framework.change_state(home_state)
                elif(key_num == 3):
                    select_sound.play(1)
                    delay(0.3)
                    game_framework.change_state(home_state)


def item_purchase(key_num):
    global coin_sound
    coin_sound = load_wav('resource/sound/coin_sound.wav')
    coin_sound.set_volume(64)

    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()

    if(key_num == 0): # 생명력
        if(info_data[-1]['item_life'] == False):
            coin_sound.play(1)
            info_data[-1]['money'] -= 100
            info_data[-1]['item_life'] = True
    elif(key_num == 1): # 시간멈추기
        if (info_data[-1]['item_stop'] == False):
            coin_sound.play(1)
            info_data[-1]['money'] -= 100
            info_data[-1]['item_stop'] = True

    f = open('data/player_info_data.txt', 'w')
    json.dump(info_data, f)
    f.close()




def draw(frame_time):
    global font, key_num, info_data
    clear_canvas()
    bg_image.draw(400, 300)
    board_image.draw(400, 300)
    coin_image.draw(320, 380)

    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()

    font = load_font('resource/Typo_SsangmunDongB.TTF', 50)
    font.draw(355, 380, "%d" % (info_data[-1]['money']) , (0, 0, 0))

    if(key_num == 0):
        select_image.draw(330, 220)
    elif(key_num == 1):
         select_image.draw(510, 220)
    elif (key_num == 2):
        select_image.draw(320, 120)
    elif(key_num == 3):
         select_image.draw(520, 120)

    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







import game_framework
import score
import stage1_intro_state

from pico2d import *


name = "ItemShopState"
bg_image = None
board_image = None
select_image = None
coin_image = None
total_money_data = None
total_money = 0
key_num = 0
font = 0

def enter():
    global bg_image, board_image, select_image, coin_image, total_money, total_money_data
    bg_image = load_image('resource/default_bg.png')
    board_image = load_image('resource/store_menu.png')
    select_image = load_image('resource/sel.png')
    coin_image = load_image('resource/coin.png')

    f = open('data/money_data.txt', 'r')
    money_data = json.load(f)
    f.close()

    f = open('data/score_data.txt', 'r')
    score_data = json.load(f)
    f.close()

    total_money = money_data['money'] + score_data[-1]['score']

    f = open('data/money_data.txt', 'w')
    total_money_data = {'money': total_money}
    json.dump(total_money_data, f)
    f.close()

    f = open('data/money_data.txt', 'r')
    total_money_data = json.load(f)
    f.close()


def exit():
    global bg_image, board_image, select_image, coin_image
    del(bg_image)
    del(board_image)
    del(select_image)
    del(coin_image)


def handle_events(frame_time):
    global key_num
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
                if (key_num == 0):
                    # 아이템구입 생명력
                    purchase(key_num)
                if (key_num == 1):
                    # 아이템구입 시간멈추기
                    purchase(key_num)
                elif(key_num == 2):
                    game_framework.change_state(stage1_intro_state)
                elif(key_num == 3):
                    game_framework.change_state(stage1_intro_state)

def purchase(key_num):
    pass

def draw(frame_time):
    global font, key_num, total_money_data
    clear_canvas()
    bg_image.draw(400, 300)
    board_image.draw(400, 300)
    coin_image.draw(320, 380)

    font = load_font('resource/Typo_SsangmunDongB.TTF', 50)
    font.draw(355, 380, "%d" % (total_money_data['money']) , (0, 0, 0))

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







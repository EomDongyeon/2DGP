import game_framework
import score
import stage1_state

from pico2d import *


name = "GameOverState"
bg_image = None
board_image = None
select_image = None
key_num = 0
font = 0

def enter():
    global bg_image, board_image, select_image
    bg_image = load_image('resource/default_bg.png')
    board_image = load_image('resource/score_board.png')
    select_image = load_image('resource/sel.png')


def exit():
    global bg_image, board_image, select_image
    del(bg_image)
    del(board_image)
    del(select_image)


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
                key_num = 0
            if event.key == SDLK_RIGHT: # 게임시작
                key_num = 1
            if event.key == SDLK_SPACE:
                if(key_num == 0):
                    game_framework.change_state(item_shop_state)
                else:
                    stage1_state.enter()
                    game_framework.push_state(stage1_state)

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
    global font, key_num
    clear_canvas()
    bg_image.draw(400, 300)
    board_image.draw(400, 300)

    f = open('data/score_data.txt', 'r')
    score_data = json.load(f)
    f.close()

    font = load_font('resource/Typo_SsangmunDongB.TTF', 50)
    font.draw(380, 340, "%d" % (score_data[-1]['score']) , (0, 0, 0))

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







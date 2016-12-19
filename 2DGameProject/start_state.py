import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('resource/kpu_credit.png')
    f = open('data/money_data.txt', 'w')
    first_money_data = {'money': 300 }
    json.dump(first_money_data, f)
    f.close()

    # 파일 출력
    f = open('data/player_info_data.txt', 'r')
    info_data = json.load(f)
    f.close()

    info_data.append({'stage': 1, 'score1': 0, 'score2': 0, 'score3': 0, 'money': 300, 'item_life': False, 'item_stop': False })

    # 파일 쓰기
    f = open('data/player_info_data.txt', 'w')
    json.dump(info_data, f)
    f.close()


def exit():
    global image
    del(image)


def update(frame_time):
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
       #  game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass





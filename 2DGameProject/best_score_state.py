import game_framework
import home_state
from sound import GameSound
from pico2d import *





name = "GameOverState"
bg_image = None
board_image = None
score_data = None
select_image = None
infinity_player_data =None
best_score_data = None
key_num = 0
font = 0
sound = GameSound()


def enter():
    global bg_image, board_image, select_image, infinity_player_data, best_score_data
    bg_image = load_image('resource/default_bg.png')
    board_image = load_image('resource/best_score_board.png')
    select_image = load_image('resource/sel.png')

    f = open('data/infinity_player_data.txt', 'r')
    infinity_player_data = json.load(f)
    f.close()
    print("ddd %d" %infinity_player_data[-1]['score'])

    f = open('data/best_score_data.txt', 'r')
    best_score_data = json.load(f)
    f.close()

def exit():
    global bg_image, board_image, select_image, infinity_player_data, best_score_data
    del(bg_image)
    del(board_image)
    del(select_image)




def handle_events(frame_time):
    global key_num, infinity_player_data, sound, best_score_data
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_SPACE:
                select_sound = load_wav('resource/sound/itemize.wav')
                select_sound.set_volume(50)
                select_sound.play(1)
                delay(0.3)
                game_framework.change_state(home_state)


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
    global font, key_num, infinity_player_data, best_score_data
    clear_canvas()
    bg_image.draw(400, 300)
    board_image.draw(400, 300)

    font = load_font('resource/Typo_SsangmunDongB.TTF', 50)
    font.draw(380, 340, "%d" % (infinity_player_data[-1]['score']), (0, 0, 0))
    font.draw(380, 220, "%d" % (best_score_data['best_score']), (0, 0, 0))

    select_image.draw(380, 120)

    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







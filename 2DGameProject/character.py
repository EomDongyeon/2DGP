from pico2d import *
from stair import Stair
from sound import GameSound

import game_framework
import gameover_state
import best_score_state
import best_score_intro_state

sound = GameSound()

class Character:
    image = None
    die_image = None
    jump_key = False
    player_score = 0
    die_state = False
    infinity_state = False
    invincibility_mode = False
    dead_time = 0.0
    life_state = False
    DIE, RIGHT_RUN, LEFT_RUN, RIGHT_STAND, LEFT_STAND = 0, 1, 2, 3, 4
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    def __init__(self,stairs):
        Character.die_state = False
        Character.dead_time = 0.0
        Character.player_score = 0
        Character.jump_key = False
        self.x, self.y = stairs[0].x, stairs[0].y + 50
        self.frame = 0
        self.dir = stairs[0].dir
        if(stairs[0].dir == -1):
            self.state = Character.LEFT_STAND
        else:
            self.state = Character.RIGHT_STAND
        print(1, stairs[0].dir, self.dir)
        self.total_frames = 0.0

        if(Character.image == None):
            Character.image = load_image('resource/player.png')
        if(Character.die_image == None):
            Character.die_image = load_image('resource/player.png')

    def reset(self, stairs):
        Character.dead_time = 0.0
        Character.player_score = 0
        Character.die_state = False
        Character.jump_key = False
        self.x, self.y = stairs[0].x, stairs[0].y + 50
        self.frame = 0
        if(stairs[0].dir == -1):
            self.state = Character.LEFT_STAND
        else:
            self.state = Character.RIGHT_STAND
        self.state = Character.LEFT_STAND
        self.total_frames = 0.0
        if(Character.image == None):
            Character.image = load_image('resource/player.png')
        if(Character.die_image == None):
            Character.die_image = load_image('resource/player.png')

    def update(self, frame_time,stairs):
        distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
        if(Character.die_state == True):
            Character.dead_time += 0.1
            self.die(stairs)
        if (self.state == Character.LEFT_RUN):
            if (Character.jump_key == True):
                Character.jump_key = False
                self.state = Character.LEFT_STAND
        elif (self.state == Character.RIGHT_RUN):
            if (Character.jump_key == True):
                Character.jump_key = False
                self.state = Character.RIGHT_STAND

    def change_dir(self, stairs):
            self.dir *= -1
    def jump(self, frame_time, stairs):
        global sound
        self.bgm2 = load_wav('resource/sound/walk_sound.wav')
        self.bgm2.set_volume(64)
        self.bgm2.play(1)
        if(stairs[Character.player_score].dir == self.dir):
            if(self.dir == -1):
                self.state = Character.LEFT_RUN
                self.x = stairs[Character.player_score].x
            else:
                self.state = Character.RIGHT_RUN
                self.x = stairs[Character.player_score].x

            self.y = stairs[Character.player_score].y + 60
        else:
            if(Character.invincibility_mode == True):
                Character.player_score -= 1
                self.dir = stairs[Character.player_score].dir
            else:
                if(Character.life_state == True):
                    Character.player_score -= 1
                    self.dir = stairs[Character.player_score].dir
                    if (self.dir == -1):
                        self.state = Character.LEFT_RUN
                    else:
                        self.state = Character.RIGHT_RUN
                    Character.life_state = False
                    f = open('data/player_info_data.txt', 'r')
                    info_data = json.load(f)
                    f.close()
                    info_data[-1]['item_life'] = False
                    f = open('data/player_info_data.txt', 'w')
                    json.dump(info_data, f)
                    f.close()
                else:
                    self.y = stairs[Character.player_score].y + 60
                    Character.player_score -= 1
                    if (self.dir == -1):
                        Character.die_state = True
                        self.state = Character.DIE
                        self.frame = 0
                        self.x = (stairs[Character.player_score + 1].x) + ((self.dir * -1) * 51)
                        self.die(stairs)
                        GameSound.sound_state = GameSound.OVER
                        sound.play(GameSound.OVER)
                    else:
                        Character.die_state = True
                        self.state = Character.DIE
                        self.frame = 0
                        self.x = (stairs[Character.player_score + 1].x) + ((self.dir * -1) * 51)
                        self.die(stairs)
                        GameSound.sound_state = GameSound.OVER
                        sound.play(GameSound.OVER)
    def die(self, stairs):
        if(Character.dead_time >= 0.5):
            Character.dead_time = 0

            # 파일 출력
            f = open('data/player_info_data.txt', 'r')
            info_data = json.load(f)
            f.close()
            if(info_data[-1]['stage'] == 1):
                info_data[-1]['score1'] = Character.player_score
            if (info_data[-1]['stage'] == 2):
                info_data[-1]['score2'] = Character.player_score
            if (info_data[-1]['stage'] == 3):
                info_data[-1]['score3'] = Character.player_score

            # 파일 쓰기
            f = open('data/player_info_data.txt', 'w')
            json.dump(info_data, f)
            f.close()

            Stair.i = 0
            Stair.num = 0
            Stair.x, Stair.y = 400, 20
            Stair.image = None
            Character.die_state = False
            delay(3.3)
            if(Character.infinity_state == False):
                game_framework.change_state(gameover_state)
            else:
                f = open('data/best_score_data.txt', 'r')
                best_score_data = json.load(f)
                f.close()

                f = open('data/infinity_player_data.txt', 'r')
                infinity_player_data = json.load(f)
                f.close()
                infinity_player_data[-1]['score'] = Character.player_score

                f = open('data/infinity_player_data.txt', 'w')
                json.dump(infinity_player_data, f)
                f.close()

                if(Character.player_score > best_score_data['best_score']):
                    f = open('data/best_score_data.txt', 'w')
                    best_score_data['best_score'] = Character.player_score
                    json.dump(best_score_data, f)
                    f.close()
                    game_framework.change_state(best_score_intro_state)
                else:
                    game_framework.change_state(best_score_state)
            #캐릭터 초기화
            self.reset(stairs)


    def moveY(self, stairs):
        self.y = stairs[Character.player_score].y + 60

    def draw(self):
        print(self.state)
        if(self.state > Character.DIE):
            self.image.clip_draw(self.frame * 96, self.state * 148, 86, 136, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 96, self.state * 145, 86, 140, self.x, self.y)
from pico2d import *
from stair import Stair

import game_framework
import gameover_state


class Character:
    image = None
    die_image = None
    jump_key = False
    player_score = 0
    die_state = False
    dead_time = 0.0

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN, RIGHT_DIE, LEFT_DIE = 0, 1, 2, 3, 4, 5
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
        self.x, self.y = stairs[0].x, stairs[0].y + 100
        self.frame = 0
        self.dir = stairs[0].dir
        if(stairs[0].dir == -1):
            self.state = Character.LEFT_STAND
        else:
            self.state = Character.RIGHT_STAND
        print(1, stairs[0].dir, self.dir)
        self.total_frames = 0.0

        if(Character.image == None):
            Character.image = load_image('resource/character_sprite_05.png')
        if(Character.die_image == None):
            Character.die_image = load_image('resource/character_die_sprite(200x214).png')

    def reset(self, stairs):
        Character.dead_time = 0.0
        Character.player_score = 0
        Character.die_state = False
        Character.jump_key = False
        self.x, self.y = stairs[0].x, stairs[0].y + 100
        self.frame = 0
        if(stairs[0].dir == -1):
            self.state = Character.LEFT_STAND
        else:
            self.state = Character.RIGHT_STAND
        self.state = Character.LEFT_STAND
        self.total_frames = 0.0
        if(Character.image == None):
            Character.image = load_image('resource/character_sprite_05.png')
        if(Character.die_image == None):
            Character.die_image = load_image('resource/character_die_sprite(200x214).png')

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
        print(self.frame)

    def change_dir(self, stairs):
            self.dir *= -1
    def jump(self, frame_time, stairs):
        if(stairs[Character.player_score].dir == self.dir):
            if(self.dir == -1):
                self.state = Character.LEFT_RUN
                self.x = stairs[Character.player_score].x
            else:
                self.state = Character.RIGHT_RUN
                self.x = stairs[Character.player_score].x

            self.y = stairs[Character.player_score].y + 100
        else:
            self.y = stairs[Character.player_score].y + 100
            Character.player_score -= 1
            if (self.dir == -1):
                Character.die_state = True
                self.state = Character.LEFT_DIE
                self.frame = 0
                self.x = (stairs[Character.player_score + 1].x) + ((self.dir * -1) * 51)
                self.die(stairs)
            else:
                Character.die_state = True
                self.state = Character.RIGHT_DIE
                self.frame = 0
                self.x = (stairs[Character.player_score + 1].x) + ((self.dir * -1) * 51)
                self.die(stairs)
    def die(self, stairs):
        if(self.frame >= 6):
            Character.dead_time = 0
            # 파일 출력
            f = open('data/score_data.txt', 'r')
            score_data = json.load(f)
            f.close()

            score_data.append({'score': Character.player_score + 1})

            # 파일 쓰기
            f = open('data/score_data.txt', 'w')
            json.dump(score_data, f)
            f.close()

            self.reset(stairs)
            Stair.i = 0
            Stair.num = 0
            Stair.x, Stair.y = 400, 20
            Stair.image = None
            Character.die_state = False
            delay(1.0)
            game_framework.change_state(gameover_state)

    def draw(self):
        if(self.state < Character.RIGHT_DIE):
            self.image.clip_draw(self.frame * 100, self.state * 214, 100, 214, self.x, self.y)
        else:
            Character.TIME_PER_ACTION = 0.2
            self.die_image.clip_draw(self.frame * 200, (self.state % 2) * 214, 200, 214, self.x, self.y,150,180)
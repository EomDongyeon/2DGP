import random
import json
import os

from pico2d import *

import game_framework
import main_state_3
import title_state



name = "MainState_2"

player = None
stair = None
bg = None
font = None
up_key = False

class Character:
    global player_score, up_key
    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = 0
        self.image = load_image('character_sprite_02.png')
    def update(self):
        self.frame = (self.frame + 1) % 7
    def draw(self):
        if stairs[player_score].dir == -1:
            self.state = 1
        else:
             self.state = 0
        self.image.clip_draw(self.frame * 100, self.state * 214,100,214,self.x,self.y)

class Background:
    image = None
    def __init__(self):
        self.x, self.y = 0, 0
        if Background.image == None:
            self.image = load_image('stage_2.png')
    def draw(self):
        self.image.clip_draw(0,0,800,600,400,300)

class Stair:
    LEFT_DIR, RIGHT_DIR = 0, 1
    i = 0
    x,y = 400, 20
    image = None
    def __init__(self):
        self.num = Stair.i
        self.x,y = Stair.x, Stair.y
        rdir = random.randint(0,1)
        if rdir == 0:
            rdir = -1
        self.dir = rdir
        self.x = self.x + ((self.dir * -1) * 51)
        self.y = self.y + 27
        if Stair.image == None:
            Stair.image = load_image('stair.png')
        Stair.i += 1
        Stair.x,Stair.y = self.x, self.y
    def update(self):
        self.x = self.x - 51
    def draw(self):
        self.image.clip_draw(0,0,50,27,self.x,self.y)


def enter():
    global player, bg, stair, stairs, player_score
    bg = Background()
    player = Character()
    stair = Stair()
    stairs = [Stair() for i in range(20)]
    running = True
    player_score = -1


def exit():
    global player, bg, stair
    del(player)
    del(bg)
    del(stair)



def pause():
    pass


def resume():
    pass



def handle_events():
    global player_score
    global up_key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == 'Q' or 'q':
                pass  # 방향전환
            if event.key == SDLK_SPACE:
                up_key = True
                player_score += 1
                if player_score >= 20:
                    game_framework.change_state(main_state_3)


def update():
    global stairs
    global player_score
    global up_key
    if up_key == True:
        player.x, player.y = stairs[player_score].x, stairs[player_score].y + 100
        player.update()
        player.frame
        if player.frame >= 6:
            up_key = False




def draw():
    global stairs
    global up_key
    global player_score
    clear_canvas()
    bg.draw()

    for stair in stairs:
        stair.draw()

    player.draw()

    font = load_font('ENCR10B.TTF', 30)
    font.draw(600, 570, "SCORE: %d" % (player_score + 1) , (0, 0, 0))

    update_canvas()
    delay(0.05)





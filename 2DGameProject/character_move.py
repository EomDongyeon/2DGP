import random
from pico2d import *

# 게임 오브젝트 클래스의 정의를 여기에

class Character:
    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = 0
        self.image = load_image('character_sprite.png')
    def update(self):
        self.frame = (self.frame + 1) % 7
        self.y = min(self.y + 5, 500)
    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,214,self.x,self.y)

class Background:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('stage_1.png')
    def draw(self):
        self.image.clip_draw(0,0,800,600,400,300)

class Stair:
    def __init__(self):
        self.x, self.y = 400, 100
        self.num = 0
        self.image = load_image('stair.png')
    def update(self):
        self.x = self.y + ((self.num % 10) * 27)
        self.y = self.y + ((self.num % 10) * 50)
    def draw(self):
        self.image.clip_draw(0,0,50,27,self.x,self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

player = Character()
bg = Background()
stair = Stair()

stairs = [Stair() for i in range(10)]
running = True

# game main loop code
i = 0
while running:
    handle_events()

    for stair in stairs:
        i += 1
        stair.update()
    player.update()


    clear_canvas()

    bg.draw()
    for stair in stairs:
        stair.draw()
    player.draw()


    update_canvas()

    delay(0.05)
# finalization code


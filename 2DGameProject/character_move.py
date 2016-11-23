import random
from pico2d import *

# 게임 오브젝트 클래스의 정의를 여기에

font = None


class Character:
    global player_score
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
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('stage_1.png')
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



def handle_events():
    global running
    global up_key
    global player_score
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            if event.key == 'Q' or 'q':
                pass # 방향전환
            if event.key == SDLK_SPACE:
                up_key = True
                player_score += 1

# initialization code
open_canvas()

bg = Background()
player = Character()
stair = Stair()

stairs = [Stair() for i in range(20)]
running = True
up_key = False
player_score = -1
# game main loop code
while running:
    handle_events()

    if up_key == True:
        player.x, player.y = stairs[player_score].x, stairs[player_score].y + 100
        player.update()
        if player.frame == 6:
            up_key = False

    clear_canvas()

    bg.draw()
    for stair in stairs:
        stair.draw()
    player.draw()

    font = load_font('ENCR10B.TTF', 30)
    font.draw(200, 200, "SCORE: %d" % player_score , (0, 0, 0))

    update_canvas()

    delay(0.05)
# finalization code


from pico2d import *

from timer import Timer

class Item:
    image_flag = True
    life_image = None
    stop_image = None
    life_state = False
    stop_state = False
    def __init__(self):
        self.w, self.h = 77, 73
        self.life_X, self.life_Y = 640, 570
        self.stop_X, self.stop_Y = 700, 570
        if Item.life_image == None:
            self.life_image = load_image('resource/Item_Life_f1.png')
        if Item.stop_image == None:
            self.stop_image = load_image('resource/Item_Stop_f2.png')


    def draw(self):
        f = open('data/player_info_data.txt', 'r')
        info_data = json.load(f)
        f.close()
        if(info_data[-1]['item_life'] == True):
            Item.life_state = True
            self.life_image.clip_draw(0, 0, 50, 47, self.life_X, self.life_Y)
        else:
            Item.life_state = False

        if (info_data[-1]['item_stop'] == True):
            Item.stop_state = True
            self.stop_image.clip_draw(0, 0, 50, 47, self.stop_X, self.stop_Y)
        else:
            Item.stop_state = False


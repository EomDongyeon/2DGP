from pico2d import *

class GameSound:
    BG,CLEAR,WIN,OVER = 0,1,2,3

    sound_state = BG

    def play(self, key_num):
        global bgm, stage_clear, game_over, game_win
        GameSound.sound_state = key_num
        if(GameSound.sound_state == GameSound.BG):
            bgm = load_music('resource/sound/bgm.mp3')
            bgm.set_volume(10)
            bgm.repeat_play()
        if(GameSound.sound_state == GameSound.CLEAR):
            bgm.stop()
            stage_clear = load_music('resource/sound/stage_clear.wav')
            stage_clear.set_volume(30)
            stage_clear.play(1)
        if(GameSound.sound_state == GameSound.WIN):
            bgm.stop()
            game_win = load_music('resource/sound/game_win.wav')
            game_win.set_volume(30)
            game_win.play(1)
        if(GameSound.sound_state == GameSound.OVER):
            bgm.stop()
            game_over = load_music('resource/sound/game_over.wav')
            game_over.set_volume(30)
            game_over.play(1)

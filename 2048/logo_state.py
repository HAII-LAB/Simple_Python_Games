# logo
from pico2d import *
import game_framework
import font
import game_state

def enter():
    global verdana
    verdana=font.load('verdana.ttf', 50)
    startedOn=get_time()

def exit():
    pass

def update():
	pass

def draw():
    global verdana
    clear_canvas()
    verdana.draw(100, 300, 'Game 2048 Logo', (0,0,0))
    update_canvas()
    pass

def handle_evets():
    events=get_events()

if __name__ == '__main__' :
    import sys
    current_module=sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()

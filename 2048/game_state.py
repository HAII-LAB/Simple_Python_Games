# game_state
from pico2d import *
import game_framework
import font

def enter():
    pass

def exit():
    pass

def update():
    pass

def draw():
	pass

def handle_evets():
    events = get_events()

if __name__ == '__main__' :
    import sys
    current_module=sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()

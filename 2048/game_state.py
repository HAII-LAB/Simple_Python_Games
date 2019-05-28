# game_state
from pico2d import *
import game_framework
import font

# 2048의 블럭을 만드는 클래스
class Block:
    # 생성자
    def __init__(self, x, y):
        self.value=0
        self.x, self.y = x,y
        self.font = font.load('verdanab.ttf', 50)
    def draw(self):
        color = (0,0,0)
        if self.value > 0:
            self.font.draw(self.x, self.y, '%d' % self.value, color)

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

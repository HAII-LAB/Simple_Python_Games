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

# 블럭 16개를 관리하는 클래스(16개의 블럭을 리스트에 저장)
class Board:
    def __init__(self):
        self.blocks[]
        for y in range(4):
            for x in range(4):
                bx=100*x+100
                by=100*y+100
                b=Block(bx,by)
                # 랜덤한 블럭
                # b.value=random.randint(10,20)
                self.blocks.append(b)
    def draw(self):
        for b in self.blocks:
            b.draw()
    def isFull(self):
        for b in self.blocks:
            if b.value==0:
                return False
        return True
    def createNew(self):
        # 숫자를 다 채우면 더 이상 채우지 않기 (무한루프 방지)
        if self.isFull():
            return False
        while True:
            index=random.randint(0,15)
            print('Index is ', index)
            if self.blocks[index].value==0:
                break
        value= 2 if random.randint(0,1)==0 else 4
        # 블럭 설정
        self.blocks[index].value=value
        return True
    def valueAt(self, x, y):
        return self.blocks[y*4+x].value
    def setValue(self, x, y, v):
        # 왼쪽부터 오다가 숫자 만나면 왼쪽으로 당겨 붙이기
        self.blocks[y*4+x].value=v

def enter():
    pass

def exit():
    pass

def update():
    pass

def draw():
	# 화면에 그리기
    clear_canvas()
    verdana.draw(500, 500, 'Game 2048', (0,0,0))
    board.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for e in events:
        # 게임 닫는 코드(Esc, 창닫기)
        if e.type==SDL_QUIT:
            game_framework.quit()
        elif e.type==SDL_KEYDOWN:
            if e.key==SDLK_ESCAPE:
                game_framework.quit()
            elif e.key==SDLK_SPACE:
                created=board.createNew()

if __name__ == '__main__' :
    import sys
    current_module=sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()

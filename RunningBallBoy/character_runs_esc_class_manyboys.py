from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image=load_image('animation_sheet.png')
        self.frame == 0
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.dx, self.dy=0,0
    def draw(self):
        sx=self.frame *100
        sy= 0 if self.dx < 0 else 100
        self.image.clip_draw(sx, sy, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dx
        self.y += self.dy

def handle_events():
    global running, b
    events = get_events()
    for e in events:
        if e.type==SDL_QUIT:
            running = False
        elif e.type == SDL_MOUSEMOTION:
            b.x, b.y=e.x, get_canvas_height() - e.y
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_UP:
                b.dy += 1
            elif e.key == SDLK_DOWN:
                b.dy -= 1
            elif e.key == SDLK_LEFT:
                b.dx -= 1
            elif e.key == SDLK_RIGHT:
                b.dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_UP:
                b.dy -= 1
            elif e.key == SDLK_DOWN:
                b.dy += 1
            elif e.key == SDLK_LEFT:
                b.dx += 1
            elif e.key == SDLK_RIGHT:
                b.dx -= 1

open_canvas()
g = Grass()
b = Boy()
boys=[Boy() for i in range(10)]
running = True
while (running):
    clear_canvas()
    g.draw()
    b.draw()
    for boy in boys:
        boy.draw()
    update_canvas()
    delay(0.005)
    handle_events()
    b.update()
    for boy in boys:
        boy.update()
close_canvas()

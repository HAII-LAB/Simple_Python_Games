from pico2d import *
import random
import game_framework
import game_world

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image=load_image('animation_sheet.png')
        self.frame = 0
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
    def fire_ball(self):
        speed = -1 if self.dx < 0 else 1
        ball = Ball(self.x, self.y, speed)
        game_world.add_object(ball, game_world.layer_obstacle)

class Ball:
    image=None
    def __init__(self, x, y, speed):
        self.x, self.y= x, y
        self.speed=speed
        if Ball.image==None:
            Ball.image=load_image('ball21x21.png')
    def update(self):
        self.x += self.speed
    def draw(self):
        Ball.image.draw(self.x, self.y)

def handle_events():
    global boy
    events = get_events()
    for e in events:
        if e.type==SDL_QUIT:
            # running = False
            game_framework.quit()
        elif e.type == SDL_MOUSEMOTION:
            boy.x, boy.y=e.x, get_canvas_height() - e.y
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_UP:
                boy.dy += 1
            elif e.key == SDLK_DOWN:
                boy.dy -= 1
            elif e.key == SDLK_LEFT:
                boy.dx -= 1
            elif e.key == SDLK_RIGHT:
                boy.dx += 1
            elif e.key == SDLK_SPACE:
                boy.fire_ball()
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_UP:
                boy.dy -= 1
            elif e.key == SDLK_DOWN:
                boy.dy += 1
            elif e.key == SDLK_LEFT:
                boy.dx += 1
            elif e.key == SDLK_RIGHT:
                boy.dx -= 1

def enter():
    grass=Grass()
    game_world.add_object(grass, game_world.layer_bg)

    global boy
    boy=Boy()
    game_world.add_object(boy, game_world.layer_player)


def exit():
    pass

def update():
    game_world.update()
    # global boy
    # boy.update()

def draw():
    # global grass, boy
    # grass.draw()
    # boy.draw()
    clear_canvas()
    game_world.draw()
    update_canvas()


if __name__ == '__main__' :
    import sys
    current_module=sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()

# # g = Grass()
# b = Boy()
# boys=[Boy() for i in range(10)]
# running = True
# while (running):
#     clear_canvas()
#     g.draw()
#     b.draw()
#     for boy in boys:
#         boy.draw()
#     update_canvas()
#     delay(0.005)
#     handle_events()
#     b.update()
#     for boy in boys:
#         boy.update()
# close_canvas()

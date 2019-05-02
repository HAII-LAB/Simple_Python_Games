from pico2d import *
def handle_events():
    global running, dx, dy
    events = get_events()
    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_UP:
                dy += 1
            elif e.key == SDLK_DOWN:
                dy -= 1
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_UP:
                dy -= 1
            elif e.key == SDLK_DOWN:
                dy += 1
            elif e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
open_canvas()
g = load_image('grass.png')
c = load_image('animation_sheet.png')
x, y = 40, 80
dx, dy = 0, 0
frame = 0
running = True
while (running):
    clear_canvas()
    g.draw(400, 30)
    # c.draw(x, y)
    sy = 0 if dx < 0 else 100
    c.clip_draw(frame * 100, sy, 100, 100, x, y)
    update_canvas()
    delay(0.005)
    handle_events()
    x += dx
    y += dy
    # x += dx
    # if x > 800: dx = -1
    # if x < 0: dx = 1
    # y += 0.2
    # if (y > 600): running = False
    frame = (frame + 1) % 8
    # frame += 1
    # if frame >= 8: frame = 0
close_canvas()

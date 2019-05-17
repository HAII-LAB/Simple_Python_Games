from pico2d import *
import game_framework
import title_state

def enter():
    global image, time
    image = load_image('kpu_credit.png')
    time=0
    print('image')

def exit():
    global image
    del(image)
    pass

def update(): # 흐른 시간을 계속 더함
    global time
    time += game_framework.frame_time # 이전 업데이트가 불린 시점부터 지금 업데이트가 불리는 시점까지의 시간
    if (time>1.0): # 누적시간 1초가 지나면
        game_framework.change_state(title_state) # exit 함수 호출
    delay(0.1)

def draw(): # 계속 화면 그림
    global image
    # print('draw', image.w, image.h)
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    pass

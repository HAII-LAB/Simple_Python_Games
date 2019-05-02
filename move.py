from pico2d import *
open_canvas(1000,1000)
grass=load_image('grass.png')
character=load_image('character.png')
x=0
grass.draw_now(500,200)
while (x<800):
    clear_canvas()
    grass.draw(500,150)
    character.draw(x, 200)
    update_canvas()
    x+=2
    delay(0.01)
close_canvas()

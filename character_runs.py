from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0

def go_left():
    x = 790
    frame = 0
    while x > 0:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.001)
        get_events()

def go_right():
    x = 0
    frame = 0
    while x < 790:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.001)
        get_events()

while True:
    go_right()
    go_left()

close_canvas()


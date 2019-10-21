from pico2d import *
import game_framework
import title_state
import main_state

name = "PauseState"

image = None

def handle_events():
    pass


def pause(): pass


def resume(): pass

def enter():
    global image
    image = load_image('pause.png')
    pass

def exit():
    global image
    del(image)
    pass

def update():
    pass

time = 0

def draw():
    global time
    clear_canvas()
    main_state.draw()
    time = time + 1
    if time % 3 == 0:
        image.draw(400, 300, 400, 200)
    update_canvas()
    pass

def resume():
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            stop = True
            game_framework.pop_state()
    pass



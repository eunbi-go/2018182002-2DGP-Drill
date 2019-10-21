import random
import json
import os

from pico2d import *
import pause_state

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None
image = None
stop = False


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('run_animation.png')

    def update(self):

        if stop == False:
            self.frame = (self.frame + 1) % 8
            self.x += self.dir
            if self.x >= 800:
                self.dir = -1
            elif self.x <= 0:
                self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass, image
    boy = Boy()
    grass = Grass()
    image = load_image('pause.png')
    pass


def exit():
    global boy, grass, image
    del(boy)
    del(grass)
    del(image)
    pass


def pause():
    pass


def resume():
    pass

stop = False
cnt = 0

def handle_events():
    events = get_events()
    global stop
    global cnt

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p and cnt % 2 == 0:
            #game_framework.push_state(pause_state)
            stop = True
            cnt = cnt + 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p and cnt % 2 == 1:
            stop = False
            cnt = cnt + 1

    pass


def update():
    boy.update()
    pass

time = 0
frame = 0

def draw():
    global time
    clear_canvas()
    if stop == True:
        time = time + 1
        clear_canvas()
        grass.draw()
        boy.draw()
        if time % 3 == 0:
            image.clip_draw(200, 200, 450, 500, 400, 400)
    grass.draw()
    boy.draw()
    update_canvas()
    pass






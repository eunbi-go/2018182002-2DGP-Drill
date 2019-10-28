import random
import json
import os
from pico2d import*
import game_framework
import title_state

name = "MainState"

mario = None
map = None
image = None

def handle_events():
    global running
    global dir
    global direction # 오른쪽 T, 왼쪽 F
    global motion # 움직이면 F, 멈추면 T
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            motion = False
            if event.key == SDLK_RIGHT:
                dir += 1
                direction = True
            elif event.key == SDLK_LEFT:
                dir -= 1
                direction = False
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            motion = True
            if event.key == SDLK_RIGHT:
                motion = True
                dir -= 1
            elif event.key == SDLK_LEFT:
                motion = True
                dir += 1
            else:
                dir = 0
    pass

class Map:
    def __init__(self):
        self.MAP = load_image('maap.png')
        self.block = load_image('blockk.png')
        self.box = load_image('tree.png')
        self.cloud = load_image('cloud.png')
        self.question_box = load_image('question_box.png')
        self.arrow = load_image('arrow.png')
        self.forest = load_image('forests.png')

    def draw(self):
        self.MAP.draw(400, 256.5)
        self.block.draw(200, 145)
        self.box.draw(320, 400)
        self.box.draw(360, 400)
        self.box.draw(400, 400)
        self.box.draw(440, 400)
        self.cloud.draw(200, 480)
        self.question_box.draw(480, 398)
        self.box.draw(517, 400)
        self.arrow.draw(400, 125)
        self.forest.draw(600, 125)

class Mario:
    def __init__(self):
        self.x, self.y = 0, 130
        self.frame = 0
        self.imageR = load_image('ma.png')
        self.imageL = load_image('mama.png')

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += 5

    def draw(self):
        if direction == True: # 오른쪽
            self.imageR.clip_draw(self.frame * 100, 0, 100, 132, self.x, self.y)
        elif direction == False:  # 왼쪽
            self.imageL.clip_draw(self.frame * 100, 0, 100, 132, self.x, self.y)

def enter():
    global mario, map
    mario = Mario()
    map = Map()
    pass

def exit():
    global mario, map
    del(mario)
    del(map)

def pause():
    pass

def resume():
    pass

def update():
    mario.update()
    pass

def draw():
    clear_canvas()
    map.draw()
    mario.draw()
    update_canvas()
    pass
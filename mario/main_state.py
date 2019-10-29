import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

mario = None
map = None
enemy = None

font = None
image = None
stop = False
dir = 0


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


des = False # 오른쪽
motion = False # 멈춤

def handle_events():
    events = get_events()
    global stop
    global dir
    global des
    global motion
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            motion = True #움직임
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_RIGHT:
                dir += 1
                des = False
            elif event.key == SDLK_LEFT:
                dir -= 1
                des = True

        elif event.type == SDL_KEYUP:
            motion = False # 멈춤
            if event.key == SDLK_RIGHT:
                dir -= 1
                des = False
            elif event.key == SDLK_LEFT:
                dir += 1
                des = True
    pass


class Mario:
    global dir
    def __init__(self):
        self.x, self.y = 0, 130
        self.frame = 0
        self.dir = 0
        self.imageR = load_image('manR.png')
        self.imageL = load_image('manL.png')
        self.stopR = load_image('stop_right.png')
        self.stopL = load_image('stop_left.png')
        self.timer = 30

    def update(self):
        if self.timer == 0:
            self.frame = (self.frame + 1) % 3
            self.timer = 50
        self.x += dir * 5
        self.timer -= 5


    def draw(self):
        if motion == True: # 움직임
            if des == False:
                self.imageR.clip_draw(self.frame * 100, 0, 100, 120, self.x, self.y)
            else:
                self.imageL.clip_draw(self.frame * 100, 0, 100, 132, self.x, self.y)

        elif motion == False:
            if des == False:
                self.stopR.draw(self.x, self.y)
            else:
                self.stopL.draw(self.x, self.y)



class Enemy:
    global dir
    def __init__(self):
        self.x, self.y = 200, 105
        self.frame = 0
        self.image = load_image('enemy.png')
        self.timer = 50
        self.des = False

    def update(self):
        self.frame = (self.frame + 1) % 2
        if self.x == 400:
            self.des = True
        elif self.x == 200:
            self.des = False

        if self.des == True:
            self.x -= 4
        elif self.des == False:
            self.x += 4

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 86, self.x, self.y)

def enter():
    global mario, map, enemy
    mario = Mario()
    map = Map()
    enemy = Enemy()
    pass


def exit():
    global mario, map, enemy
    del(mario)
    del(map)
    del(enemy)
    pass


def pause():
    pass


def resume():
    pass


def update():
    mario.update()
    enemy.update()
    pass

def draw():
    clear_canvas()
    map.draw()
    enemy.draw()
    mario.draw()
    update_canvas()
    delay(0.01)
    pass






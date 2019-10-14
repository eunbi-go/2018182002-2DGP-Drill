from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class small_ball:
    def __init__(self):
        self.x, self.y = random.randint(1, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y <= 61 or self.y >= 72:
            self.y -= random.randint(10, 14)

    def draw(self):
        for small_ball in small_team:
            self.image.draw(self.x, self.y)


class big_ball:
    def __init__(self):
        self.x, self.y = random.randint(1, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y <= 60 or self.y >= 69:
            self.y -= random.randint(5, 9)

    def draw(self):
        for big_ball in big_team:
            self.image.draw(self.x, self.y)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        for boy in team:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
running = True
team = [Boy() for i in range(11)]
small = 0
big = 0
cnt = False
while cnt == False:
    if small + big != 20:
        small = random.randint(1, 10)
        big = random.randint(1, 10)
    elif small + big == 20:
        cnt = True

small_team = [small_ball() for i in range(small)]
big_team = [big_ball() for i in range(big)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for small_ball in small_team:
        small_ball.update()
    for big_ball in big_team:
        big_ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for small_ball in small_team:
        small_ball.draw()
    for big_ball in big_team:
        big_ball.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
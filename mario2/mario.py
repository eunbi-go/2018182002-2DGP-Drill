from pico2d import *

# 이미지 크기
MAP_WIDTH, MAP_HEIGHT = 800, 513 # 원본
map2_height = 513
map1_height = 513
block_width, block_height = 90, 136
box_width, box_height = 49, 44
cloud_width, cloud_height = 74, 68
question_box_width, question_box_height = 47, 48
stop_right_width, stop_right_height = 80, 136
stop_left_width, stop_left_height = 80, 136
arrow_width, arrow_height = 95, 109
forest_width, forest_height = 325, 133


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
            self.imageR.clip_draw(frame * 100, 0, 100, 132, self.x, self.y)
        elif direction == False:  # 왼쪽
            self.imageL.clip_draw(frame * 100, 0, 100, 132, self.x, self.y)

running = True
x = 0
frame = 0
dir = 0
direction = True
motion = True

open_canvas(MAP_WIDTH, MAP_HEIGHT)
mario = Mario()
map = Map()

while running:

    handle_events()

    mario.update()

    clear_canvas()
    map.draw()
    mario.draw()
    update_canvas()

    delay(0.05)

close_canvas()

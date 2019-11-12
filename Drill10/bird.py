import game_framework
from pico2d import *
import game_world

# Bird Run Speed
BIRD_PIXEL_METER = (20.0 / 0.4)  # 20픽셀 40CM
BIRD_RUN_SPEED_KMPH = 2  # 속도
BIRD_RUN_SPEED_MPM = (BIRD_RUN_SPEED_KMPH * 1000.0 / 60.0)
BIRD_RUN_SPEED_MPS = (BIRD_RUN_SPEED_MPM / 60.0)
BIRD_RUN_SPEED_PPS = (BIRD_RUN_SPEED_MPS * BIRD_PIXEL_METER)

# Bird Action Speed
BIRD_TIMER_ACTION = 0.5
BIRD_ACTION_PER_TIME = 1.0 / BIRD_TIMER_ACTION
BIRD_FRAMES_PER_ACTION = 5


class Bird:
    def __init__(self):
        self.x, self.y = 100, 400
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + BIRD_FRAMES_PER_ACTION * BIRD_ACTION_PER_TIME * game_framework.frame_time) % 5
        # 왼쪽으로 감
        if self.x > 1600 - 200 and self.x > 200:
            self.dir = -1
            self.velocity -= BIRD_RUN_SPEED_PPS

        # 오른쪽으로 감
        elif self.x < 1600 - 200 and self.x < 200:
            self.dir = 1
            self.velocity += BIRD_RUN_SPEED_PPS

        self.dir = clamp(-1, self.velocity, 1)

        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(100, self.x, 1600 - 100)

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 183, 163, 183, 163, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * 183, 163, 183, 163,
                                           0.0, 'h', self.x, self.y, 200, 200)

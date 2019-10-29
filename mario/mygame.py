import game_framework
import pico2d

import start_state

# fill here
pico2d.open_canvas(800, 513)
game_framework.run(start_state) # 플레이하라고 알려 줌
pico2d.close_canvas()
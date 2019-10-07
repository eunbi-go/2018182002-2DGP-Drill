from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global x, y
    global cursor_x, cursor_y
    global pos_x, pos_y
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        if event.type == SDL_MOUSEBUTTONDOWN:
            x = event.x
            y = KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
cursor1 = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
show_cursor()
x = KPU_WIDTH // 2
y = KPU_HEIGHT // 2

def draw_line(p1, p2):
    for i in range(0, 100 + 1, 2):
        t = i / 100
       # x = (1 - t) * p1[0] + t * p2[0]
        #y = (1 - t) * p1[1] + t * p2[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

while running:
    clear_canvas()
    cursor1.draw(x, y)
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    draw_line(x, y)
    delay(0.05)

close_canvas()



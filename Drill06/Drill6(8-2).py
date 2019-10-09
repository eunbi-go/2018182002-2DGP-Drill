import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())




def draw_curve_3_points(p1, p2, p3):
    # fill here


    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x, y))
    draw_point(p3)
    pass


def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        draw_point((x, y))
    draw_point(p4)



cnt = 0

while True:
    prepare_turtle_canvas()
    pos1x = random.randint(-300, 300)
    pos2x = random.randint(-300, 300)
    pos3x = random.randint(-300, 300)
    pos4x = random.randint(-300, 300)
    pos5x = random.randint(-300, 300)
    pos6x = random.randint(-300, 300)
    pos7x = random.randint(-300, 300)
    pos8x = random.randint(-300, 300)
    pos9x = random.randint(-300, 300)
    pos10x = random.randint(-300, 300)

    pos1y = random.randint(-300, 300)
    pos2y = random.randint(-300, 300)
    pos3y = random.randint(-300, 300)
    pos4y = random.randint(-300, 300)
    pos5y = random.randint(-300, 300)
    pos6y = random.randint(-300, 300)
    pos7y = random.randint(-300, 300)
    pos8y = random.randint(-300, 300)
    pos9y = random.randint(-300, 300)
    pos10y = random.randint(-300, 300)

    draw_big_point((pos1x, pos1y))
    draw_big_point((pos2x, pos2y))
    draw_big_point((pos3x, pos3y))
    draw_big_point((pos4x, pos4y))
    draw_big_point((pos5x, pos5y))
    draw_big_point((pos6x, pos6y))
    draw_big_point((pos7x, pos7y))
    draw_big_point((pos8x, pos8y))
    draw_big_point((pos9x, pos9y))
    draw_big_point((pos10x, pos10y))


    draw_curve_3_points((pos1x, pos1y), (pos2x, pos2y), (pos3x, pos3y))
    draw_curve_3_points((pos4x, pos4y), (pos5x, pos5y), (pos6x, pos6y))
    draw_curve_3_points((pos7x, pos7y), (pos8x, pos8y), (pos9x, pos9y))
    draw_curve_3_points((pos1x, pos1y), (pos2x, pos2y), (pos3x, pos3y))




turtle.done()
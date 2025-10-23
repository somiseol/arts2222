import time
import os
import turtle
import math
import random

color_list = ["red", "green", "blue", "orange", "pink", "yellow"]

# classic  starting params
#A = -1.4
#B = 1.6
#C = 1.0
#D = 0.7

# number of points to calculate and draw
ITERATIONS = 20000

# scaling factor to map the attractor coordinates (-3 to 3) to the screen size

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# dot size for the plotted points
DOT_SIZE = 2

# setup
def setup_turtle():
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("white")

    # turn off automatic screen updates for high performance
    screen.tracer(0, 0)

    # create multiple turtles
    t_list = [] # list of turtles
    t_list_attr = [] # list of tuples of starting base params

    for i in range(random.randrange(4, 6)):
        t_list.append(turtle.Turtle())
        t_list[i].hideturtle()
        t_list[i].speed(1)
        t_list[i].penup()
        random_color = color_list.pop(random.randrange(0, len(color_list)))
        t_list[i].color(random_color)

        rand_A = random.uniform(-5, 5)
        rand_B = random.uniform(-5, 5)
        rand_C = random.uniform(-1, 1)
        rand_D = random.uniform(-1, 1)
        rand_Scale = random.randrange(200, 800)
        base_params = (rand_A, rand_B, rand_C, rand_D, rand_Scale, random_color)
        t_list_attr.append(base_params)
    return screen, t_list, t_list_attr

# calc and draw points
def draw_clifford_attractor():
    screen, t_list, t_list_attr = setup_turtle()

    x = 0.1
    y = 0.1

    os.system('clear') # clear screen

    for i in range(ITERATIONS):

        # 1. Clifford Attractor Equations:
        # x_n+1 = sin(a * y_n) + c * cos(a * x_n)
        # y_n+1 = sin(b * x_n) + d * cos(b * y_n)
        print(f"time: {i}")

        for j in range(len(t_list)): # for each turtle
            x_next = math.sin(t_list_attr[j][0] * y) + t_list_attr[j][2] * math.cos(t_list_attr[j][0] * x)
            y_next = math.sin(t_list_attr[j][1] * x) + t_list_attr[j][3] * math.cos(t_list_attr[j][1] * y)

            # 2. map calculated (x, y) coordinates to screen coordinates (sx, sy)
            # attractor typically spans from approx -3 to +3, so scale it
            sx = x_next * t_list_attr[j][4]
            sy = y_next * t_list_attr[j][4]

            print(f"pattern: {t_list_attr[j]}\ncoordinate: ({sx}, {sy})")

            # 3. draw the point
            t_list[j].goto(sx, sy)
            t_list[j].dot(DOT_SIZE)

            # 4. update current coord for next iteration
            x, y = x_next, y_next

        print(f"\033[{len(t_list)}A", end="")
        # update screen periodically to show progress
        if i % 1000 == 0:
            screen.update()
    # final update to show all points
    screen.update()

    turtle.done()

os.system('clear')
draw_clifford_attractor()


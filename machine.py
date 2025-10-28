import os
import turtle
import math
import random

# number of points to calculate and draw
ITERATIONS = 25000

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# dot size for points
DOT_SIZE = 1

# setup
def setup_turtle():
    color_list = ["cyan", "yellow", "magenta", "white"]
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")

    # turn off automatic screen updates for high performance
    screen.tracer(0, 0)

    # create multiple turtles
    t_list = [] # list of turtles
    t_list_attr = [] # list of tuples of starting base params

    # base parameter restrict range
    base_param_restrict = 4
    # default = 3

    for i in range(random.randrange(2, len(color_list) - 1)):
        t_list.append(turtle.Turtle())
        t_list[i].hideturtle()
        t_list[i].speed(1)
        t_list[i].penup()
        random_color = color_list.pop(random.randrange(0, len(color_list)))
        t_list[i].color(random_color)

        #cannot figure out heuristic check
        rand_A = random.uniform(-1 * base_param_restrict, base_param_restrict)
        rand_B = random.uniform(-1 * base_param_restrict, base_param_restrict)
        rand_C = random.uniform(-1 * base_param_restrict, base_param_restrict)
        rand_D = random.uniform(-1 * base_param_restrict, base_param_restrict)
        rand_Scale = random.randrange(100, 300, 100)
        rand_size = random.randrange(1, 3)

        base_params = (rand_A, rand_B, rand_C, rand_D, rand_Scale, random_color, rand_size)

        t_list_attr.append(base_params)

    os.system('i3-msg resize set width 90ppt') # i3 specific
    os.system('clear')
    msg("what do you see?")

    return screen, t_list, t_list_attr

def msg(msg):

    for i in range(50):
        new_lines = random.randrange(0, 5)
        tabs = random.randrange(3, 50)

        print((' ' * tabs) + msg + ('\n' * new_lines))
    print('\nby somi seol')

# calc and draw points
def draw_clifford_attractor():
    screen, t_list, t_list_attr = setup_turtle()

    x = 0.01
    y = 0.01

    for i in range(ITERATIONS):
        # Clifford Attractor Equations:
        # x_n+1 = sin(a * y_n) + c * cos(a * x_n)
        # y_n+1 = sin(b * x_n) + d * cos(b * y_n)
        #print(f"iteration: {i}")

        for j in range(len(t_list)): # for each turtle
            x_next = math.sin(t_list_attr[j][0] * y) + t_list_attr[j][2] * math.cos(t_list_attr[j][0] * x)
            y_next = math.sin(t_list_attr[j][1] * x) + t_list_attr[j][3] * math.cos(t_list_attr[j][1] * y)

            # map calculated (x, y) coordinates to screen coordinates (sx, sy)
            # attractor typically spans from approx -3 to +3, so scale it
            sx = x_next * t_list_attr[j][4]
            sy = y_next * t_list_attr[j][4]

            # draw point
            t_list[j].goto(sx, sy)
            #DOT_SIZE = t_list_attr[j][6] 
            t_list[j].dot(DOT_SIZE)# corresponding dot size

            # update current coord for next iteration
            x, y = x_next, y_next

        # update screen periodically to show progress
        if i % 1000 == 0:
            screen.update()

    # final update to show all points
    screen.update()

    # erase art to get ready for next one
    screen.clear()

while True:
    draw_clifford_attractor()

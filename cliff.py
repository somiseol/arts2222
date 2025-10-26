import os
import turtle
import math
import random

color_list = ["red", "green", "blue", "white"]

# starting parameters
param_restrict = 5
pr = param_restrict
A = random.uniform(pr * -1, pr)
B = random.uniform(pr * -1, pr)
C = random.uniform(pr * -1, pr)
D = random.uniform(pr * -1, pr)

# classic example
#A = -1.4
#B = 1.6
#C = 1.0
#D = 0.7

# number of points to calculate and draw
ITERATIONS = 100000

# scaling factor to map the attractor coordinates (-3 to 3) to the screen size
SCALE_FACTOR = 100

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# dot size for the plotted points
DOT_SIZE = 1

# setup screen
def setup_turtle():
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")

    # turn off automatic screen updates for high performance
    screen.tracer(0, 0)

    # TODO multiple turtles

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(1)
    t.penup()

    return screen, t

# calc and draw points
def draw_clifford_attractor():
    screen, t = setup_turtle()

    t.color('white')# random color
    # initial starting points
    x = 0.0
    y = 0.0

    # set color
    # t.color("white")

    for i in range(ITERATIONS):
        # 1. Clifford Attractor Equations:
        # x_n+1 = sin(a * y_n) + c * cos(a * x_n)
        # y_n+1 = sin(b * x_n) + d * cos(b * y_n)

        x_next = math.sin(A * y) + C * math.cos(A * x)
        y_next = math.sin(B * x) + D * math.cos(B * y)

        # 2. map calculated (x, y) coordinates to screen coordinates (sx, sy)
        # attractor typically spans from approx -3 to +3, so scale it
        sx = x_next * SCALE_FACTOR
        sy = y_next * SCALE_FACTOR
        print(f"A:{A} B:{B} C:{C} D:{D} x:{sx} y:{sy}")
        # 3. draw the point
        t.goto(sx, sy)
        t.dot(DOT_SIZE)

        # 4. update current coord for next iteration
        x, y = x_next, y_next

        # update screen periodically to show progress
        if i % 1000 == 0:
            screen.update()
    # final update to show all points
    screen.update()

    # keep window open until click
    screen.exitonclick()

os.system('clear')
draw_clifford_attractor()


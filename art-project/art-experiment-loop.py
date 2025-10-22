import turtle
from turtle import Turtle
import os
import time
import math
from random import random
from random import randrange

os.system('clear')

def out(name, color, speed, angle):
    print(f"{name} ({color})\nspeed: {speed}\nangle: {angle}")

color_list = ["red", "orange", "green", "blue", "indigo", "purple"]

t_amp = []
t_freq = []
t_offset = []
t_list = []
t_color = []

turtle.Screen().bgcolor("white")

for i in range(randrange(3, 6)):
    t_list.append(Turtle())
    t_list[i].hideturtle()
    t_list[i].speed(randrange(5, 9))

    t_color.append(color_list.pop(randrange(0, len(color_list))))
    t_list[i].color(t_color[i])
    t_list[i].width(randrange(1, 10))
    t_amp.append(random() * 10)
    t_freq.append(random())
    t_offset.append(randrange(1, 5))
    t_list[i].right(randrange(0, 360))

angle = 0.0
curr_time = 0.0
angle_offset = randrange(10, 20)
lines_to_clr = len(t_list) * 4 + 1
while True:
    time.sleep(0.01)
    curr_time += 1
    print(f"time: {curr_time}")
    for i in range(len(t_list)):
        angle = t_offset[i] + (t_amp[i] * math.sin(t_freq[i] * curr_time))
        angle = angle * angle_offset
        speed = randrange(3, 10) + curr_time
        t_list[i].forward(speed * 3)
        t_list[i].right(angle / 3)
        name = f"turtle {i}"
        color = t_color[i]
        out(name, color, speed, angle)
    print(f"\033[{lines_to_clr}F", end = "")

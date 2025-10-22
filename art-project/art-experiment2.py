import sys
import os
import time

from turtle import Turtle

os.system('clear')

color_list = ["red", "green", "blue"]

t_list = []

for i in range(3):
    t_list.append(Turtle())
    t_list[i].hideturtle()
    t_list[i].color(color_list[i])
    t_list[i].width(i * 2)

for t in range(100):
    for i in range(len(t_list)):
        t_list[i].forward(1)
        t_list[i].right(i + 1)

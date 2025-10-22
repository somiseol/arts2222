import sys
import os
import time

from turtle import Turtle
from random import random # use in the future some way

os.system('clear')

try:
    a = sys.argv[1]
except IndexError:
    a = "indexerror"

t = Turtle()
t.hideturtle()
t.width(3)
t.color('red')

def output_scr(i, speed, angle, lines_to_clr):
    print(f"{a}\ni = {i}\nspeed = {speed}\nangle = {angle:.2f}", end='')
    print(f"\033[{lines_to_clr}F", end='')


for i in range(1, 50):
    time.sleep(0.01) # seconds

    speed = i * 2
    angle = 100 / i

    t.forward(speed)
    t.right(angle)

    output_scr(i, speed, angle, 4)

import sys
import os
import time

from turtle import Turtle
from random import random

a = sys.argv[1]

print(a)

t = Turtle()
t.hideturtle()
t.width(3)
t.color('red')

i = 1
while True:
    t.forward(i * 2)
    t.right(100 / i)

    i += 1 # i is 1/10th of a second
    print(f"\ri = {i}", end='', flush=True)
    time.sleep(0.01)

    if i >= 50:
        break

t.done()

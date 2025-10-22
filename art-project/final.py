# input randomness seed?
# draw
    # white background
    # several turtles
        # each turtle has its own color
        # each turtle has its own speed
            # thickness is based on speed (thicker == slower)
        # each turtle has its own angle

    # need to control tightness of spirals
    # need to control speed

import turtle
import math
from random import randrange
import time
turtle.Screen().bgcolor("white")

# starting attr
speed = 10
angle = 1

t_list = [] # new list of turtles

for i in range(randrange(3, 6)): # random between 3 and 6 turtles
    t_list.append(turtle.Turtle()) # make new turtle
    t_list[i].hideturtle() # hide turtles
    t_list[i].right(randrange(3, 180)) # starting offset at least 3 degrees
    t_list[i].width(randrange(1, 10)) # random thickness, at least 3, less than 10

t_list_len = len(t_list) # length of turtle list

for i in range(10000): # main loop
    time.sleep(1/1000) # miliseconds

    for j in range(t_list_len): # iterate through turtle list
        t_list[j].forward(speed) # move forward
        angle = sin_funct(amp) #TODO
        t_list[j].right(angle) # move right

def sin_funct(amp, freq, curr_time):
    return amp * math.sin(freq * curr_time)

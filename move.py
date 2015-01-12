#!/usr/bin/env python
import math

def move(x, y, step, angel=0):
    nx = x + step * math.cos(angel)
    ny = y - step * math.sin(angel)
    return nx, ny

x = move(100, 100, 60, math.pi/6)
print x[0] 

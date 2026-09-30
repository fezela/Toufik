#!/usr/bin/env python3

import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def set(self,x,y):
        self.x = x
        self.y = y

    def center(self):
        #this function sucks and is probably unecessary
        if (self.x == 0 and self.y == 0):
            return self.get()
        else:
            return (self.x / 2, self.y /2)
        pass
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


def point_hex_corner(center, i):
    angle_deg = 60 * i - 30
    angle_rad = math.pi / 180 * angle_deg 
    return (angle_deg, angle_rad)

def flat_hex_corner(center, i):
    angle_deg = 60 * i
    angle_rad = (math.pi / 180) * angle_deg
    return (angle_deg, angle_rad)

pos = Vector2(0,0)
x = point_hex_corner(pos, 6)
y = flat_hex_corner(pos, 6)

dev = Vector2(1,1)

print(dev)
print(dev.get())
print("point_hex_corner: {}".format(x))
print("flat_hex_corner: {}".format(y))

from math import *

def posCalc(velocity, angle, pos, dt, gravity):
    pos[0] = pos[0] + velocity[0] * dt
    pos[1] = pos[1] + velocity[1] * dt + 1/2 * gravity * dt**2
    velocity = [velocity[0],velocity[1]+ 1/2 * gravity * dt]
    return [pos, velocity]
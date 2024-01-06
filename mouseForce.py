import pygame
from pygame.locals import *
from distanceFormula import distAB

springConst = 0.12

def mouseForcePush(springConst, start, end):
    x = start[0]
    y = start[1]

    force = springConst * (distAB(start,end))

    return force
    
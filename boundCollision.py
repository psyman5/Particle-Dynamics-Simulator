import numpy as np

def wallCollision(velocity, mass, coeffRestitution,x,y):

    if x == True and y == False:
        velocity[0] *= -coeffRestitution

    elif y == True and x == False:
        velocity[1] *= -coeffRestitution

    elif y == True and x == True:
        velocity[0] *= -coeffRestitution
        velocity[1] *= -coeffRestitution

    return velocity
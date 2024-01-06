from math import pi, atan, degrees

def propertyFinder(velocity, gravity, pos, radius, density):
    mass = density/(pi*(radius**2))
    kineticE = 1/2 * mass * velocity[0]**2 + 1/2 * mass * velocity[1]**2
    potentialE = mass * gravity * pos[1]
    momentum = mass * velocity[0] + mass * velocity[1]

    if velocity[0] != 0:
        angle = degrees(atan(velocity[1]/velocity[0]))
    else:
        angle = 90

    return kineticE,potentialE, momentum, mass, angle


import numpy as np
from math import *
from ParticleClass import Particle


'''coeffRestitution = 0.8'''

'''particleA = Particle(velocity=[0,-3], angle = 270, 
                         kineticE=None, potentialE=None, momentum = None, 
                         mass = 2, pos = [0,0], collFlag = False, radius= 50, density= 1)'''

'''particleB = Particle(velocity=[1.73,1], angle = 30, 
                         kineticE=None, potentialE=None, momentum = None, 
                         mass = 1, pos = [0,0], collFlag = False, radius= 50, density= 1)'''

def veloMatrixSolver(particleA, particleB, coeffRestitution):

    from visualPygame import coeffRestitution

    velocityA = sqrt((particleA.velocity[0]**2)+(particleA.velocity[1]**2))
    velocityB = sqrt((particleB.velocity[0]**2)+(particleB.velocity[1]**2))

    velocityATangent = velocityA * cos(radians(90-particleB.angle))
    velocityBTangent = velocityB * cos(radians(90-particleB.angle))

    velocityATangent = -velocityA * sin(radians(90-particleB.angle))
    velocityANormal = velocityA * cos(radians(90-particleB.angle))

    velocityBTangent = 0
    velocityBNormal = velocityB

    velocityATangentAfter = velocityATangent
    velocityBTangentAfter = velocityBTangent

    normalMomentumSum = particleA.mass * velocityANormal + particleB.mass * velocityBNormal

    relVelocities = relVelocities = -coeffRestitution * (velocityATangent - velocityBTangent)

    leftSide = np.array([[particleA.mass, particleB.mass],[1,-1]])
    rightSide = np.array([[normalMomentumSum],[relVelocities]])

    result = np.matmul(np.linalg.inv(leftSide), rightSide)


    velocityANormalAfter = result[0][0]

    velocityBNormalAfter = result[1][0]



    particleA.velocity[0] = velocityANormalAfter
    particleA.velocity[1] = velocityATangentAfter

    particleB.velocity[0] = -velocityBNormalAfter
    particleB.velocity[1] = velocityBTangentAfter
        
    return particleA.velocity,particleB.velocity


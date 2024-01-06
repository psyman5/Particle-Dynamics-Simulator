import math

def isItInside(particleCenter,otherParticleCenter,radius1,radius2):
    
    distanceCenters = (particleCenter-otherParticleCenter)**2 + (particleCenter-otherParticleCenter)**2

    if distanceCenters < (radius1+radius2)**2
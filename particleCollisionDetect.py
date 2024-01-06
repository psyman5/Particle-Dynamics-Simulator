from posCalc import posCalc
from math import sqrt


def particleColl(particleList):
   from velocityMatrixSolver import veloMatrixSolver
   from visualPygame import dt, gravity, coeffRestitution
   for particle in particleList:
       otherParticles = [diffParticle for diffParticle in particleList if diffParticle != particle]

       for diffParticle in otherParticles:
           distance = sqrt((diffParticle.pos[0]-particle.pos[0])**2+(diffParticle.pos[1]-particle.pos[1])**2)
           if distance < (particle.radius + diffParticle.radius):
               newVelo = veloMatrixSolver(particleA = particle, particleB = diffParticle, coeffRestitution = coeffRestitution)
               particle.velocity = newVelo[0]
               diffParticle.velocity = newVelo[1]
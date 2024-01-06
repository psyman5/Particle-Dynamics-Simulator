import pygame
from ParticleClass import Particle
from propertyCalc import propertyFinder
from posCalc import posCalc
from collisionDetect import collisionDetect
from particleCollisionDetect import particleColl
import random as r

clock = pygame.time.Clock()

fps = 60 #limits the clock

width,height = 250,250

screen = pygame.display.set_mode((width, height))

black = (0,0,0)
red = (50,0,255)
gravity = 9.81

coeffRestitution = 1

'''particleList = [Particle(velocity=[100,0], angle = None, 
                         kineticE=None, potentialE=None, momentum = None, 
                         mass = None, pos = [30,250], collFlag = False, radius= 10, density= 2),
                         Particle(velocity=[0,0], angle = None, 
                         kineticE= None, potentialE=None, momentum = None, 
                         mass = None, pos = [325,250], collFlag = False, radius= 25, density= 5),
                         Particle(velocity=[10,400], angle = None, 
                         kineticE= None, potentialE=None, momentum = None, 
                         mass = None, pos = [30,95], collFlag = False, radius= 25, density= 5)]'''

'''particleList = [Particle(velocity=[0,100], angle = None, 
                         kineticE=None, potentialE=None, momentum = None, 
                         mass = None, pos = [width/2,height /2], collFlag = False, radius= 10, density= 55),
                         Particle(velocity=[0,-100], angle = None, 
                         kineticE= None, potentialE=None, momentum = None, 
                         mass = None, pos = [width/2, height - 100], collFlag = False, radius= 10, density= 5)]'''

particleList = [Particle(velocity=[r.randint(-100,100),r.randint(-100,100)], angle = 30, 
                         kineticE=None, potentialE=None, momentum = None, 
                         mass = 5, pos = [r.randint(10,height-(height/10)),r.randint(10,height-(height/10))], collFlag = False, density= 5, radius= 10) for x in range(20)]

'''particleList = [Particle(velocity=[50,x], angle = 270, 
                         kineticE=None, potentialE=None, momentum = None, 
                         mass = None, pos = [50,250+x/5], collFlag = False, radius = 50, density= 5) for x in range(1,300)]'''

for particle in particleList:
    propertyTuple = propertyFinder(particle.velocity, gravity, particle.pos, radius= particle.radius, density = particle.density)
    particle.kineticE, particle.potentialE, particle.momentum, particle.mass, particle.angle = propertyTuple[0], propertyTuple[1],propertyTuple[2], propertyTuple[3], propertyTuple[4] 


dt = 1/fps
t = 0
posList = []
timeList = []
dBugList = []
veloList = []
running = True

while running is True:

    t += dt
    timeList.append(t)

    #pygame.display.flip()
    screen.fill(color = black)
    keys = pygame.key.get_pressed()
    
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    '''for particle in particleList:

        if particle.velocity[0] > 10**-7 and particle.velocity[0] < 10**-4:
            particle.velocity[0] = 0

        elif particle.velocity[1] > 10**-7 and particle.velocity[1] < 10**-4:
            particle.velocity[1] = 0'''
        


    particleColl(particleList)
    collisionDetect(particleList, width, height, coeffRestitution, dt, gravity)

    for particle in particleList:

        propertyTuple = propertyFinder(particle.velocity, gravity, particle.pos, radius= particle.radius, density = particle.density)
        particle.kineticE, particle.potentialE, particle.momentum, particle.mass, particle.angle = propertyTuple[0], propertyTuple[1],propertyTuple[2], propertyTuple[3], propertyTuple[4]

        #pygame.draw.circle(screen,black, particle.pos, 5)
        pC = posCalc(particle.velocity, particle.angle, particle.pos, dt, gravity)
        particle.pos, particle.velocity = pC[0], pC[1]
        #posList.append(-particle.pos[1])
        veloList.append(particle.velocity[1])
        pygame.draw.circle(screen, red, particle.pos, radius= particle.radius)
        #print(particle.velocity)


    
    pygame.display.flip()

pygame.quit()

#plt.plot(timeList,posList)
#plt.plot(veloList)
#plt.show()
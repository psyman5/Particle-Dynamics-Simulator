from posCalc import posCalc
from boundCollision import wallCollision

def collisionDetect(particleList, width, height, coeffRestitution, dt, gravity):

    '''for particle in particleList:
        pC = posCalc(particle.velocity, particle.angle, particle.pos, dt, gravity)
        
        if pC[0][0] + 5 >= width or pC[0][0] - 5 <= 0:
            x = True
            y= False
            wallCollision(velocity=particle.velocity, mass = particle.mass, 
                          coeffRestitution= coeffRestitution,x=x,y=y)

        elif pC[0][1] - 5 <= 0 or pC[0][1] + 5 >= height:
            x = False
            y = True
            wallCollision(velocity=particle.velocity, mass = particle.mass, 
                          coeffRestitution= coeffRestitution,x=x,y=y)'''
    

    for particle in particleList:

        if particle.collFlag == False:
            pC = posCalc(particle.velocity, particle.angle, particle.pos, dt, gravity)
            
            if pC[0][0] + particle.radius > width or pC[0][0] - particle.radius < 0:
                x = True
                y= False
                wallCollision(velocity=particle.velocity, mass = particle.mass, 
                            coeffRestitution= coeffRestitution,x=x,y=y)
                particle.collFlag = True

            elif pC[0][1] - particle.radius < 0 or pC[0][1] + particle.radius > height:
                x = False
                y = True
                wallCollision(velocity=particle.velocity, mass = particle.mass, 
                            coeffRestitution= coeffRestitution,x=x,y=y)
                particle.collFlag = True
            
                
        elif particle.collFlag == True:
            particle.collFlag = False
            return
        
'''particle.pos[0], particle.pos[1], pC[0][0], pC[0][1] '''

        

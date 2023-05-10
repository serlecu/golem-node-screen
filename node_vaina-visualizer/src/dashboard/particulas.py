import pygame, sys, random
 
# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time
# [loc, velocity, timer]
particles = []
 
# Loop ------------------------------------------------------- #
def dib_particulas(ventana, pos:tuple[int,int], size:tuple[int,int], stroke:int, newParticle:tuple[float,float,float,int] = (-1.0,-1.0,-1.0,-1)):
    global particles

    centerY = pos[1] + size[1]*0.5
    centerX = pos[0] + size[0]*0.5
    colorAxis = (255,255,255)

    if newParticle[0] != -1.0:
        mx = newParticle[0]
        my = newParticle[1]
        vel = newParticle[2]
        lifeTime = newParticle[3]
        particles.append([[mx, my], [vel - 1, -2], lifeTime])

    # horizont
    for i in range(stroke):
        pygame.draw.aaline(ventana,(100,100,100),
                           (pos[0], centerY), #(ventana.get_width()/2+250,ventana.get_height()/2-150),
                           (pos[0]+size[0], centerY), #(ventana.get_width()-200,ventana.get_height()/2-150),
                           1)
   
    # boundaries
    len = 50
    for i in range(stroke):
        # verticals
        pygame.draw.aaline(ventana,(colorAxis), (pos[0], centerY-len*0.5), (pos[0], centerY+len*0.5), 1)
        pygame.draw.aaline(ventana,(colorAxis), (pos[0]+size[0], centerY-len*0.5), (pos[0]+size[0], centerY+len*0.5),1)
        # horizontals
        pygame.draw.aaline(ventana,(colorAxis), (centerX-len*0.5, pos[1]), (centerX+len*0.5, pos[1]),1)
        pygame.draw.aaline(ventana,(colorAxis), (centerX-len*0.5, pos[1]+size[1]), (centerX+len*0.5, pos[1]+size[1]),1)
    

    # pygame.draw.aaline(ventana,(colorAxis),(ventana.get_width()/2+250,ventana.get_height()/2-165),(ventana.get_width()/2+250,ventana.get_height()/2-135),1)
    # #pygame.draw.aaline(ventana,(colorAxis),(ventana.get_width()/2+475,ventana.get_height()/2-210),(ventana.get_width()/2+475,ventana.get_height()/2-190),1)
    # pygame.draw.aaline(ventana,(colorAxis),(ventana.get_width()/2+465,ventana.get_height()/2-210),(ventana.get_width()/2+485,ventana.get_height()/2-210),1)
    # pygame.draw.aaline(ventana,(colorAxis),(ventana.get_width()/2+465,ventana.get_height()/2-100),(ventana.get_width()/2+485,ventana.get_height()/2-100),1)
    # pygame.draw.aaline(ventana,(colorAxis),(ventana.get_width()-200,ventana.get_height()/2-165),(ventana.get_width()-200,ventana.get_height()/2-135),1)

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][0] += particle[1][1]
        """particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]"""
        particle[2] -= 0.03
        particle[1][1] += 0.03
        pygame.draw.circle(ventana, (128, 128, 128), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
  
    



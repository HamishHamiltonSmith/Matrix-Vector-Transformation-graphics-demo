import pygame
import math

import quamash
import operations as op
import time

pygame.init()
clock = pygame.time.Clock()

print("Welcome to this quick demo on matrix tranformation graphics!")
print("Edit the points, basis vectors and other said parts of the code to edit output\n")
print("To play the transformation, click anywhere in the window.")
x = input("Press enter to begin: ")

screenWidth = 1800
screenHeight = 900
originX = screenWidth/2
originY = screenHeight/2-24
dif = 28
color = "black"
paused = -1

#BASIS VECTORS - edit to change overall transformation
baseM = {
    "i":[1,0.1],
    "j":[-0.1,1]
}

#POINTS - edit to add or remove vectors
points = [
    [3,0],
    [0,3],
    [0,-3],
    [-3,0]
]

screen = pygame.display.set_mode((screenWidth,screenHeight))

def drawVector(basis,fullPoint,pointX,pointY):
    global points
    global color

    if basis == "i":
        color = "green"
    elif basis == "j":
        color = "red"
    else:
        color = "purple"
    
    pointY = pointY*-1
    start = (originX,originY)
    end = (originX+(pointX*dif),originY+pointY*dif)
    
    #LINE JOINING - uncomment to connect vector endpoints

    #if basis != "i" and basis != "j":
    #    if points.index(fullPoint) != len(points)-1:
    #        nPoint = points[points.index(fullPoint)+1]
    #        pY = nPoint[1]*-1
    #        pX = nPoint[0]
    #        nEnd = (originX+(pX*dif),originY+pY*dif) 
    #        pygame.draw.line(screen,color,end,nEnd,5)


    #VECTORS - uncomment to view full vectors
    pygame.draw.line(screen,color,start,end,5)
    

def drawGrid():
    global screen

    img = pygame.image.load("/home/kali/Software/Python/Matrix-Transformations/assets/grid.png")
    screen.blit(img,(0,0))

print("Determinent: " + str(op.get_determinent(baseM.get("i"),baseM.get("j"))))

while True:
    clock.tick(120)

    #BACKGROUND - comment if using the grid
    #screen.fill((100,100,100))

    #GRID - ccomment to remove the grid
    drawGrid()

    for p in points:
        drawVector(None,p,p[0],p[1])

    #VIEW BASIS VECTORS,- uncomment to view
    drawVector("j",None,baseM.get("j")[0],baseM.get("j")[1])
    drawVector("i",None,baseM.get("i")[0],baseM.get("i")[1])

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print("Bye")
            pygame.quit()
            quit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            #You can use a while loop here to continuously transform your structures
            newPoints = op.multiple(baseM.get("i"),baseM.get("j"),points)
            points.clear()
            for p in newPoints:
                points.append(p)

    


    pygame.display.update()
from imports import *

DEAD   = 0
ALIVE  = 1
TO_BORN= 2
TO_DIE = 3

GREY = (93,93,93)
WHITE = (255,255,255)
DARK_GREY = (50,50,50)

class Cell:
    def __init__(self, gotStatus, gotSize, gotCoords):
        self.rect = pygame.Rect(gotCoords, gotSize)
        self.coords = gotCoords
        self.status = gotStatus

        self.alivePic = pygame.Surface(gotSize)
        self.alivePic.fill(GREY)

        alivePic1 = pygame.Surface((gotSize[0] * .9, gotSize[1] * .9))
        alivePic1.fill(WHITE)
        self.alivePic.blit(alivePic1, (gotSize[0] * 0.05, gotSize[1] * 0.05))

        self.deadPic = pygame.Surface(gotSize)
        self.deadPic.fill(GREY)

        deadPic1 = pygame.Surface((gotSize[0] * .9, gotSize[1] * .9))
        deadPic1.fill(DARK_GREY)
        self.deadPic.blit(deadPic1, (gotSize[0] * 0.05, gotSize[1] * 0.05))

    def setStatus(self, gotStatus):
        self.status = gotStatus

    def getStatus(self):
        return self.status
    
    def render(self, drawSurface):
        if self.status == ALIVE:
            drawSurface.blit(self.alivePic, self.coords)
        else:
            drawSurface.blit(self.deadPic, self.coords)

from imports import *
from cellFile import *

class Game:
    #Initialize game grid
    def __init__(self, gotPos, gotSize, gotXcount, gotYcount):
        self.rect = pygame.Rect(gotPos, gotSize)
        self.xCount = gotXcount
        self.yCount = gotYcount
        self.canvas = pygame.Surface((gotSize[0], gotSize[1]))
        self.polygon = []
        for i in range(int(self.yCount)):
            self.polygon.append([])
            for j in range(int(self.xCount)):
                calculatedSize = ( gotSize[0] / self.xCount, gotSize[1] / self.yCount )
                calculatedPos  = ( j * calculatedSize[0], i * calculatedSize[1] )

                self.polygon[i].append( Cell( DEAD, calculatedSize, calculatedPos ) )
        self.isGameStarted = False

    #Render of each cell
    def render(self, where):
        for each in self.polygon:
            for every in each:
                every.render(self.canvas)
        where.blit(self.canvas, self.rect.topleft)

    #Method to clean the game surface
    def cleanPolygon(self):
        for each in self.polygon:
            for every in each:
                every.setStatus(DEAD)

    #Update status of cell (alive\dead) by got coordinates
    def updateCellStatus(self, gotX, gotY, gotStatus):
        self.polygon[gotY][gotX].setStatus(gotStatus);

    #Get cell status (dead\alive) by got coordinates
    def getCellStatus(self, gotXIndex, gotYIndex):
        return self.polygon[gotYIndex][gotXIndex].getStatus()

    #Predicat of correct clicked position
    def theClickPosIsCorrect(self, coords):
        for each in self.polygon:
            for every in each:
                if every.rect.collidepoint(( coords[0] - self.rect.left, coords[1] - self.rect.top )):
                    return True
        return False

    #Get cell object by got coords
    def getCellByCoords(self, coords):
        for each in self.polygon:
            for every in each:
                if every.rect.collidepoint(( coords[0] - self.rect.left, coords[1] - self.rect.top )):
                    return every

    #Update an generation of game polygon
    def updateFrame(self):
        #PART 1 #Calculation of borning or dying cells
        for y in range(int(self.yCount)):
            for x in range(int(self.xCount)):
                neighbours = self.getCellNeighbours(x, y)
                if self.getCellStatus(x, y) == ALIVE:
                    if self.getCellNeighbours(x, y) < 2:
                        self.updateCellStatus(x, y, TO_DIE)
                    if self.getCellNeighbours(x, y) > 3:
                        self.updateCellStatus(x, y, TO_DIE)
                if self.getCellStatus(x, y) == DEAD:
                    if self.getCellNeighbours(x, y) == 3:
                        self.updateCellStatus(x, y, TO_BORN)

        #PART 2 #Make clean in order to render cells correctly
        for y in range(int(self.yCount)):
            for x in range(int(self.xCount)):
                if self.getCellStatus(x, y) == TO_DIE:
                    self.updateCellStatus(x, y, DEAD)
                if self.getCellStatus(x, y) == TO_BORN:
                    self.updateCellStatus(x, y, ALIVE)

    #Get count of cell's neighbours
    def getCellNeighbours(self, gotXIndex, gotYIndex):
        count = 0
        #to gotYIndex (last one not included)
        for y in range(gotYIndex - 1, gotYIndex + 2):
            #to gotXIndex (last one not included)
            for x in range(gotXIndex - 1, gotXIndex + 2):
                #Pass an iteration to prevent itself counting as neighbour
                if x == gotXIndex and y == gotYIndex or x < 0 or y < 0 or x > self.xCount - 1 or y > self.yCount - 1:
                    continue 
                #if cell of polygon exists
                if self.getCellStatus(x, y) == ALIVE or self.getCellStatus(x, y) == TO_DIE:
                    count += 1
        return count

    #Check if all cells are dead
    def checkForGameEnds(self):
        for y in range(int(self.yCount)):
            for x in range(int(self.xCount)):
                if self.getCellStatus(x, y) == TO_BORN or self.getCellStatus(x, y) == TO_DIE or self.getCellStatus(x, y) == ALIVE:
                    return False
        return True

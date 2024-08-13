from imports import *

WHITE = (255,255,255)
LIGHT_GREY = (150, 150, 150)
BLACK = (0,0,0)

class Control:
    def __init__(self, coords, size): #init by got tuple of coords (x, y) and tuple of size (width, height)
        self.rect = pygame.Rect(coords, size)
        
        self.myFont = pygame.sysfont.SysFont("Comic Sans MS", 30)

        self.button1 = pygame.Rect(10, 10, 100, 40)
        self.button1Text = self.myFont.render("Start", False, BLACK)
        self.button1Pic = pygame.Surface(self.button1.size)
        self.button1Pic.fill(LIGHT_GREY)
        self.button1Pic.blit(self.button1Text, (10, 10))

        self.button2 = pygame.Rect(10, 60, 100, 40)
        self.button2Text = self.myFont.render("Restart", False, BLACK)
        self.button2Pic = pygame.Surface(self.button1.size)
        self.button2Pic.fill(LIGHT_GREY)
        self.button2Pic.blit(self.button2Text, (10, 10))

        self.mainSurf = pygame.Surface(size)
        self.mainSurf.fill(WHITE)
    def checkClick(self, gotCoords): #Check what button is clicked
        if self.button1.collidepoint(gotCoords):
            return "start"
        if self.button2.collidepoint(gotCoords):
            return "restart"
        else:
            return ""
    def render(self, gotSurfaceToRender): #Where to render
        self.mainSurf.blit(self.button1Pic, self.button1.topleft)
        self.mainSurf.blit(self.button2Pic, self.button2.topleft)
        gotSurfaceToRender.blit(self.mainSurf, self.rect.topleft)

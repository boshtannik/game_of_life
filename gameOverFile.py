from imports import *
from sys import exit

DARK_GREY = (50, 50, 50)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

class Window:
    def __init__(self, coords, size): #Init by got tuple of coords (leftTop) and tuple of size (width, height)
        pygame.font.init()

#       Make font init
        self.myFont = pygame.sysfont.SysFont("Comic Sans MS", 30)

#       Make rect
        self.rect = pygame.Rect(coords, size)

#       Make Base surface
        self.surf = pygame.Surface(self.rect.size)
        self.surf.fill(DARK_GREY)

#       Make add surface
        self.surf1 = pygame.Surface((int(size[0]*.95), int(size[1]*.95)))
        self.surf1.fill(WHITE)

#       Blit add surface on Base surface
        self.surf.blit(self.surf1, (size[0]*.02, size[1]*.02))

#       Make text and blit on base
        self.textPic = self.myFont.render("Game over", False, BLACK)
        self.surf.blit(self.textPic, (self.rect.width/8, self.rect.height/3))

#       Make crossRect, fill crossRect with BLACK
        self.crossRect = pygame.Rect((self.rect.right-20, self.rect.top), (20, 20))
        self.crossPic  = pygame.Surface((20, 20))
        self.crossPic.fill(BLACK)

#       Make crossText, blit crossText on crossRect
        self.crossText = self.myFont.render("X", False, WHITE)
        self.crossPic.blit(self.crossText, (1, 1))

#       Blit crossRect on base
        self.surf.blit(self.crossPic, (self.rect.width - 20, 2))

    def closeClick(self, mouseCoords): #(if close is clicked)
        if self.crossRect.collidepoint(mouseCoords):
            return True
        return False

    def run(self):
        menu = True
        while menu:
            for each in pygame.event.get():
                if each.type == pygame.QUIT:
                    exit()
                if each.type == pygame.MOUSEBUTTONDOWN:
                    msX, msY = each.pos
                    if self.closeClick((msX, msY)):
                        menu = False
            pygame.display.flip()

    def render(self, where): #Where to render
        where.blit(self.surf, self.rect.topleft)

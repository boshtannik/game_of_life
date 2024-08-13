#!/usr/bin/env python
from imports import *

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

# can change ammount of cells by changing cellSize
cellSize = 10

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

controlObject = Control((0,0), (120, SCREEN_HEIGHT))
gameObject = Game( ( 120, 0 ), ( SCREEN_WIDTH - controlObject.rect.width ,
            SCREEN_HEIGHT ), (SCREEN_WIDTH - controlObject.rect.width) / cellSize, SCREEN_HEIGHT / cellSize)

game = True
while game:
    for each in pygame.event.get():
        if each.type == pygame.QUIT:
            game = False

        if each.type == pygame.KEYDOWN:
            if each.key == pygame.K_c:
                gameObject.cleanPolygon()
            if each.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            if each.key == pygame.K_SPACE:
                gameObject.isGameStarted = not gameObject.isGameStarted

        if each.type == pygame.MOUSEBUTTONDOWN:
            msX, msY = each.pos

            if controlObject.rect.collidepoint((msX, msY)):
                if controlObject.checkClick((msX, msY)) == "start":
                    gameObject.isGameStarted = True

                if controlObject.checkClick((msX, msY)) == "restart":
                    gameObject.cleanPolygon()
                    gameObject.isGameStarted = False

            if gameObject.rect.collidepoint((msX, msY)):
                if gameObject.theClickPosIsCorrect((msX, msY)):
                    obj = gameObject.getCellByCoords((msX, msY))
                    obj.setStatus(not obj.status)

    if gameObject.isGameStarted:
        gameObject.updateFrame()

    controlObject.render(window)
    gameObject.render(window)

    if gameObject.checkForGameEnds() and gameObject.isGameStarted:
        gameObject.isGameStarted = False
        gameObject.cleanPolygon()
        menu = Window((SCREEN_WIDTH/2 - SCREEN_WIDTH/4, SCREEN_HEIGHT/2 - SCREEN_HEIGHT/4), (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))
        menu.render(window)
        menu.run()

    pygame.display.flip()

import pygame 
import sys



SCREEN_HEIGHT = 800
SCREEN_WIDTH = 500


pygame.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
timer = pygame.time.Clock()

gameRunning = True

while gameRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            gameRunning = False
            pygame.quit()  
            sys.exit() 

    screen.fill((100, 100, 5))

    pygame.display.update()
    timer.tick(60)




import pygame, sys, math, random
from mob import *
from player import *
from Level import *

pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

balls = []
level = loadLevel("Levels/1.lvl")


pb = PlayerBall(3, [width/2,height/2])



bgColor = 0,0,0


while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_t:
                                    paused = False
                if event.key == pygame.K_UP:
                    pb.face("up")
                if event.key == pygame.K_w:
                    pb.go("up")
                if event.key == pygame.K_DOWN:
                    pb.face("down")
                if event.key == pygame.K_s:
                    pb.go("down")
                if event.key == pygame.K_LEFT:
                    pb.face("left")
                if event.key == pygame.K_a:
                    pb.go("left")
                if event.key == pygame.K_RIGHT:
                    pb.face("right")
                if event.key == pygame.K_d:
                    pb.go("right")
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_LEFT or pygame.K_Right:
                    pb.face("check")
                if event.key == pygame.K_w:
                    pb.go("sup")
                if event.key == pygame.K_s:
                    pb.go("sdown")
                if event.key == pygame.K_a:
                    pb.go("sleft")
                if event.key == pygame.K_d:
                    pb.go("sright")
                
            
    for ball in balls:
        # ~ print str(ball)
        ball.update(size)
    pb.update(size)
    
    
    for hitter in balls:
        for hittie in balls:
            hitter.collide(hittie)
        for tile in level:
            hitter.collide(tile)
    for tile in level:
        pb.collide(tile)\
        
        
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for tile in level:
        screen.blit(tile.image, tile.rect)
    screen.blit(pb.image, pb.rect)
    pygame.display.flip()
    clock.tick(60)
    # ~ print clock.get_fps()

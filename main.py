import pygame, sys, math, random
from mob import *
from player import *
from Level import *
from enemy import *
from bolt import *
pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)


levelnum = 1
level = loadLevel("Levels/1.lvl")
blocks = level["blocks"]
mobs = level["enemies"]
pb = Player(5, level["player"]) 


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
                #for facing directions
                if event.key == pygame.K_UP:
                    pb.face("face up")
                if event.key == pygame.K_DOWN:
                    pb.face("face down")
                if event.key == pygame.K_LEFT:
                    pb.face("face left")
                if event.key == pygame.K_RIGHT:
                    pb.face("face right")
                #for moving directions
                if event.key == pygame.K_w:
                    pb.go("up")
                if event.key == pygame.K_s:
                    pb.go("down")
                if event.key == pygame.K_a:
                    pb.go("left")
                if event.key == pygame.K_d:
                    pb.go("right")
                #for schooting
                if event.key == pygame.K_SPACE:
                    pb.shooting("yes")
        if event.type == pygame.KEYUP:
                #for not going directions
                if event.key == pygame.K_w:
                    pb.go("sup")
                if event.key == pygame.K_s:
                    pb.go("sdown")
                if event.key == pygame.K_a:
                    pb.go("sleft")
                if event.key == pygame.K_d:
                    pb.go("sright")
                #for not facing directions
                if event.key == pygame.K_UP:
                    pb.face("stop up")
                if event.key == pygame.K_DOWN:
                    pb.face("stop down")
                if event.key == pygame.K_LEFT:
                    pb.face("stop left")
                if event.key == pygame.K_RIGHT:
                    pb.face("stop right")
                #for not shooting
                if event.key == pygame.K_SPACE:
                    pb.shooting("no")
                
            
    for mob in mobs:
        mob.update(size)
    for mob in mobs:
        pb.collide(mob)
    pb.update(size)
    
    
    for hitter in mobs:
        for hittie in mobs:
            hitter.collide(hittie)
        for tile in blocks:
            hitter.collide(tile)
    for tile in blocks:
        if pb.collide(tile):
            if tile.kind == "warp":
                levelnum += 1
                level = loadLevel("Levels/"+str(levelnum)+".lvl")
                blocks = level["blocks"]
                mobs = level["enemies"]
                #add delay here
                pb = Player(5, level["player"])
        
        
    screen.fill(bgColor)
    for mob in mobs:
        screen.blit(mob.image, mob.rect)
    for tile in blocks:
        screen.blit(tile.image, tile.rect)
    screen.blit(pb.image, pb.rect)
    
    pygame.display.flip()
    clock.tick(60)

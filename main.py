import pygame, sys, math, random
from mob import *
from player import *
from Level import *
from enemy import*

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
                if event.key == pygame.K_UP:
                    pb.go("", "up")
                if event.key == pygame.K_w:
                    pb.go("up", "")
                if event.key == pygame.K_DOWN:
                    pb.go("", "down")
                if event.key == pygame.K_s:
                    pb.go("down", "")
                if event.key == pygame.K_LEFT:
                    pb.go("", "left")
                if event.key == pygame.K_a:
                    pb.go("left", "")
                if event.key == pygame.K_RIGHT:
                    pb.go("", "right")
                if event.key == pygame.K_d:
                    pb.go("right", "")
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    pb.go("sup", "")
                if event.key == pygame.K_s:
                    pb.go("sdown", "")
                if event.key == pygame.K_a:
                    pb.go("sleft", "")
                if event.key == pygame.K_d:
                    pb.go("sright", "")
                
            
    for mob in mobs:
        mob.update(size)
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
                pb = Player(5, level["player"])
        
        
    screen.fill(bgColor)
    for mob in mobs:
        screen.blit(mob.image, mob.rect)
    for tile in blocks:
        screen.blit(tile.image, tile.rect)
    screen.blit(pb.image, pb.rect)
    
    pygame.display.flip()
    clock.tick(60)
    # ~ print clock.get_fps()

import pygame, sys, math, random, time
from mob import *
from player import *
from Level import *
from enemy import *
from Imposter import *
from bolt import *


raw_input("press any key to continue")
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
pb = Player(3, level["player"]) 
bullets = []

bgColor = 0,0,0


while True:
    #raw_input(">>>")
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
                    pb.go("go up")
                if event.key == pygame.K_s:
                    pb.go("go down")
                if event.key == pygame.K_a:
                    pb.go("go left")
                if event.key == pygame.K_d:
                    pb.go("go right")
                #for schooting
                if event.key == pygame.K_SPACE:
                    bullets += [pb.shoot()]
        if event.type == pygame.KEYUP:
                #for not going directions
                if event.key == pygame.K_w:
                    pb.go("s up")
                if event.key == pygame.K_s:
                    pb.go("s down")
                if event.key == pygame.K_a:
                    pb.go("s left")
                if event.key == pygame.K_d:
                    pb.go("s right")
                #for not facing directions
                if event.key == pygame.K_UP:
                    pb.face("stop up")
                if event.key == pygame.K_DOWN:
                    pb.face("stop down")
                if event.key == pygame.K_LEFT:
                    pb.face("stop left")
                if event.key == pygame.K_RIGHT:
                    pb.face("stop right")
                
                
            
    for mob in mobs:
        mob.update(size, pb.rect.center)
        if not mob.alive:
            mobs.remove(mob)
    for mob in mobs:
        pb.collide(mob)
        for bullet in bullets:
            bullet.collide(mob)
    if not pb.alive:
        levelnum = 0
        level = loadLevel("Levels/"+str(levelnum)+".lvl")
        bullets = []
        pb = Player(7, level["player"])
        blocks = level["blocks"]
        mobs = level["enemies"]
    for bullet in bullets:
        bullet.update(size, pb.rect.center)
        for mob in mobs:
            mob.collide(bullet)
        if not bullet.alive:
            bullets.remove(bullet)
    pb.update(size)
    
    
    for hitter in mobs:
        for hittie in mobs:
            hitter.collide(hittie)
        for tile in blocks:
            hitter.collide(tile)
    for tile in blocks:
        for bullet in bullets:
            bullet.collide(tile)
        if pb.collide(tile):
            if tile.kind == "warp":
                levelnum += 1
                bullets = []
                level = loadLevel("Levels/"+str(levelnum)+".lvl")
                blocks = level["blocks"]
                mobs = level["enemies"]
                #add delay here
                pb = Player(3, level["player"])
        
        
    screen.fill(bgColor)
    for mob in mobs:
        screen.blit(mob.image, mob.rect)
    for tile in blocks:
        screen.blit(tile.image, tile.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    screen.blit(pb.image, pb.rect)
    
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()

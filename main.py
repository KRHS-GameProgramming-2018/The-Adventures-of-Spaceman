import pygame, sys, math, random, time
from mob import *
from player import *
from Level import *
from enemy import *
from Imposter import *
from bolt import *
from Button import *

from boltPower import *
from healthUp import *
from speedBoost import *

# ~ raw_input("press any key to continue")
pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

enemies = pygame.sprite.Group()

bolts = pygame.sprite.Group()

powers = pygame.sprite.Group()

all = pygame.sprite.RenderUpdates()

SpaceZombie.containers = (enemies, all)
Imposter.containers = (enemies, all)
Greenie.containers = (enemies, all)
Bolt.containers = (bolts, all)
speedBoost.containers = (powers, all)
boltPower.containers = (powers, all)
healthUp.containers = (powers, all)
Player.containers = (all)

hasPowers = []
boltPower = False
levelnum = 1
level = loadLevel("Levels/1.lvl")
blocks = level["blocks"]
mobs = level["enemies"]
powerUps = level["power-ups"]
pb = Player(3, level["player"], hasPowers) 
bullets = []

bgColor = 0,0,0
mode = "menu"
shooting = False

while True:
    while mode == "menu":
        menuimage = pygame.image.load ("PNG/backgrounds/Title.png")
        menurect = menuimage.get_rect()
        # ~ startimage = pygame.image.load ("Screens/backroundStartScreen.png")
        # ~ startrect = startimage.get_rect()
        # ~ print 'f'
        for event in pygame.event.get():
                    #print event.type
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                mode = "inGame"
                            if event.key == pygame.K_ESCAPE:
                                sys.exit()
        screen.fill(bgColor)
        screen.blit(menuimage, menurect)
        pygame.display.flip()

    #menuimage = pygame.image.load ("backgrounds/Titlescreen.png")
    #menurect = menuimage.get_rect()
    #startimage = pygame.image.load ("backgrounds/backroundStartScreen.png")
    #startrect = startimage.get_rect()
    

    while mode == "inGame":
        while pb.alive:
            for event in pygame.event.get():
                #print event.type
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()
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
                            shooting = True
                            
                                    
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
                        #     for not facing directions
                        if event.key == pygame.K_UP:
                            pb.face("stop up")
                        if event.key == pygame.K_DOWN:
                            pb.face("stop down")
                        if event.key == pygame.K_LEFT:
                            pb.face("stop left")
                        if event.key == pygame.K_RIGHT:
                            pb.face("stop right")
                        if event.key == pygame.K_SPACE:
                            shooting = False
                        
            if shooting:
                bullet = pb.shoot()
                if bullet:
                    bullets += [bullet]
                    print bullet
                    if boltPower == True:
                        print 'yes'
                        bullets += [bullet]
                        bullets += [bullet]            
                    
            for mob in mobs:
                mob.update(size, pb.rect.center)
                if not mob.alive:
                    mobs.remove(mob)
                pb.collide(mob)
                if mob.kind == "greenie" and len(mobs) < 20:
                    if mob.checkDuplicate():
                        mobs += [mob.duplicate()]
                for bullet in bullets:
                    bullet.collide(mob)
            
            for bullet in bullets:
                bullet.update(size, pb.rect.center)
                for mob in mobs:
                    mob.collide(bullet)
                    
                if not bullet.alive:
                    bullets.remove(bullet)
            pb.update(size)
            
            for power in powerUps:
                if pb.collide(power):
                    hasPowers += [power.kind]
                    powerUps.remove(power)
                    print hasPowers
                   
                    
            boltPower = False
            if "speedBoost" in hasPowers:
                pb.maxSpeed = 7
            if "healthUp" in hasPowers:
                pb.lives = pb.extraLives
                hasPowers.remove("healthUp")
                print pb.lives
            if "boltPower" in hasPowers:
                boltPower = True
                
                
                    
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
                        if levelnum == 10:
                            mode = "victory"
                        else:
                            levelnum += 1
                            bullets = []
                            level = loadLevel("Levels/"+str(levelnum)+".lvl")
                            blocks = level["blocks"]
                            mobs = level["enemies"]
                            powerUps = level["power-ups"]
                            #add delay here
                            pb = Player(3, level["player"], hasPowers)
                            print levelnum
            
                
            screen.fill(bgColor)
            for mob in mobs:
                screen.blit(mob.image, mob.rect)
            for power in powerUps:
                screen.blit(power.image, power.rect)
            for tile in blocks:
                screen.blit(tile.image, tile.rect)
            for bullet in bullets:
                screen.blit(bullet.image, bullet.rect)
            screen.blit(pb.image, pb.rect)
            pygame.display.flip()
            clock.tick(60)
            
        while not pb.alive:
            hasPowers = []
            endimage = pygame.image.load ("PNG/backgrounds/endscreen.png")
            endrect = menuimage.get_rect()
        # ~ startimage = pygame.image.load ("Screens/backroundStartScreen.png")
        # ~ startrect = startimage.get_rect()
        # ~ print 'f"
        
            for event in pygame.event.get():
                #print event.type
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            levelnum = 1
                            bullets = []
                            level = loadLevel("Levels/"+str(levelnum)+".lvl")
                            blocks = level["blocks"]
                            mobs = level["enemies"]
                            powerUps = level["power-ups"]
                            #add delay here
                            pb = Player(3, level["player"], hasPowers)
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()
                        if event.key == pygame.K_t:
                            paused = True
                            while paused:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT: sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_t:
                                            paused = False
            screen.fill(bgColor)
            screen.blit(endimage, endrect)
            pygame.display.flip()
            clock.tick(60)
    while mode == "victory":
        print "pog"
        menuimage = pygame.image.load ("PNG/backgrounds/winendgame.png")
        menurect = menuimage.get_rect()
        for event in pygame.event.get():
                    #print event.type
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                mode = "menu"
                            if event.key == pygame.K_ESCAPE:
                                sys.exit()
        screen.fill(bgColor)
        screen.blit(menuimage, menurect)
        pygame.display.flip()

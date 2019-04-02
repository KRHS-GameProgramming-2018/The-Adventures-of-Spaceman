import pygame, sys, math, random, time
from mob import *
from player import *
from Level import *
from enemy import *
from Imposter import *
from bolt import *
from Button import *

from warp import *
from HUD import *

from boltPower import *
from healthUp import *
from speedBoost import *

pygame.init()
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    controller =  pygame.joystick.Joystick(0)
    controller.init()
else:
    controller = None

clock = pygame.time.Clock()

width = 1000
height = 800
size = width, height
screen = pygame.display.set_mode(size)

enemies = pygame.sprite.Group()
bolts = pygame.sprite.Group()
blocks = pygame.sprite.Group
powers = pygame.sprite.Group()
HUD = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()

SpaceZombie.containers = (enemies, all)
Imposter.containers = (enemies, all)
Greenie.containers = (enemies, all)
Bolt.containers = (bolts, all)
Block.containers = (blocks, all)
Warp.containers = (blocks, all)
speedBoost.containers = (powers, all)
boltPower.containers = (powers, all)
healthUp.containers = (powers, all)
HUD.containers = (HUD, all)
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
bulletMag = 100

bgColor = 0,0,0
mode = "menu"
shooting = False

startTime = time.clock()

while True:
    while mode == "menu":
        menuimage = pygame.image.load ("PNG/backgrounds/Title.png")
        menurect = menuimage.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        mode = "inGame"
                    if event.key == pygame.K_ESCAPE:
                        mode = "menu"
                    if event.type == pygame.QUIT:
                        sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    mode = "inGame"
        screen.fill(bgColor)
        screen.blit(menuimage, menurect)
        pygame.display.flip()
        
    while mode == "inGame":
        while pb.alive:
            print int((time.clock() - startTime)*1000)
            for event in pygame.event.get():
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
                        if event.key == pygame.K_r:
                            bulletMag = 25
                            
                                    
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
                
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 3:
                        if event.value > .85:
                            pb.face("face down")
                            pb.y = "down"
                        if event.value < -.85:
                            pb.face("face up")
                            pb.y = "up"
                            
                    if event.axis == 4:
                        if event.value > .85:
                            pb.face("face right")
                            pb.y = "right"
                        if event.value < -.85:
                            pb.face("face left")
                            pb.y = "left"
                            
                    

                    if event.axis == 0:
                        if event.value > .7:
                            pb.go("go right")
                            
                        elif event.value > 0: 
                            pb.go("s right")
                            pb.go("s left")
                            pb.speed = 0
                        elif event.value > -.7:
                            pb.go("s left")
                            pb.go("s right")
                            pb.speed = 0
                        else:
                            pb.go("go left")
                           
                    if event.axis == 1:
                        if event.value > .7:
                            pb.go("go down") 
                        elif event.value > 0: 
                            pb.go("s down")
                            pb.go("s up")
                            pb.speed = 0
                        elif event.value > -.7:
                            pb.go("s up")
                            pb.go("s down")
                            pb.speed = 0
                        else:
                            pb.go("go up")
                                
                    
                    if not event.axis == 3:
                        if event.value <.7:
                            if event.value >0:
                                if event.axis == 1:
                                    if event.value > .7:
                                        pb.face("face down")
                        if event.value > -.7:
                            if event.value <0:
                                if event.axis == 1:                
                                    if event.value < -.7:
                                        pb.face("face up")
                                        
                    if not event.axis == 4:
                        if event.value <.7:
                            if event.value >0:
                                if event.axis == 0:
                                    if event.value > .7:
                                        pb.face("face right")
                        if event.value > -.7:
                            if event.value <0:
                                if event.axis == 1:                                
                                    if event.value < -.7:
                                        pb.face("face left")
                                 
                            
                    
                        
                    if event.axis == 2:
                        if event.value < -.3:
                            shooting = True
                        else:
                            shooting = False
                            
                            
                    
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 2:
                        bulletMag = 12
                    
            
            
            if shooting:
                bullet = pb.shoot()
                if bullet:
                    if bulletMag > 0:
                        bullets += [bullet]
                        bulletMag += -1
                        print bulletMag
                        if boltPower == True:
                            print 'yes'
                            bullets += [bullet]
                            bullets += [bullet]            
                    

            # ~ for mob in mobs:
                # ~ mob.update(size, pb.rect.center)
                

            for mob in mobs:

                if not mob.alive:
                    mobs.remove(mob)
                pb.collide(mob)
                if mob.kind == "greenie" and len(mobs) < 20:
                    if mob.checkDuplicate():
                        mobs += [mob.duplicate()]
                for bullet in bullets:
                    bullet.collide(mob)
            
            for bullet in bullets:
                for mob in mobs:
                    mob.collide(bullet)
                if not bullet.alive:
                    bullets.remove(bullet)
            # ~ pb.update(size)
            all.update(size, pb.rect.center)
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
            
            all.update(size, pb.rect.center)
            
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
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        mode = "menu"
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            levelnum = 1
                            bullets = []
                            level = loadLevel("Levels/"+str(levelnum)+".lvl")
                            blocks = level["blocks"]
                            mobs = level["enemies"]
                            powerUps = level["power-ups"]
                            pb = Player(3, level["player"], hasPowers)
                            bulletMag = 12
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

import pygame, sys, math, random, time
from mob import *
from player import *
from Level import *
from enemy import *
from Imposter import *
from merchant import *
from bolt import *
from Button import *
from Background import *

from warp import *
from ShopItem import *

from Lifebar import *
from magazine import *
from CoinCounter import *

from boltPower import *
from healthUp import *
from speedBoost import *
from Coin import *

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

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
blocks = pygame.sprite.Group()
powerUps = pygame.sprite.Group()
hud = pygame.sprite.Group()
shopItems = pygame.sprite.Group()
coins = pygame.sprite.Group()
npcs = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, all)
SpaceZombie.containers = (mobs, all)
Imposter.containers = (mobs, all)
Greenie.containers = (mobs, all)
Merchant.containers = (npcs, all)
Bolt.containers = (bullets, all)
Warp.containers = (blocks, all)
speedBoost.containers = (powerUps, all)
boltPower.containers = (powerUps, all)
healthUp.containers = (powerUps, all)
Lifebar.containers = (hud, all)
magazine.containers = (hud, all)
CoinCounter.containers = (hud, all)
ShopItem.containers = (shopItems, all)
Player.containers = (all)
Background.containers = (all)
Coin.containers = (coins, all)
Button.containers = (all)

hasPowers = []
boltPower = False
levelnum = 1
playerLives = 5

#blocks = level["blocks"]
#mobs = level["enemies"]
#powerUps = level["power-ups"]
#bullets = []
bulletMag = 40
PlayerCoins = 1
startCoins = 0

bgColor = 0,0,0
mode = "menu"
shooting = False

startTime = time.clock()

isX = False;
isY = False;

while True:
    bg = Background("PNG/backgrounds/Title.png")
    startButton = Button("start", [width/2,3*height/8])
    controlButton = Button("controls", [width/2, height/2])
    quitButton = Button("quit", [width/2, 5*height/8])
    
    while mode == "menu":
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
            
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 0:
                    startButton.checkHover(event.pos)
                    controlButton.checkHover(event.pos)
                    quitButton.checkHover(event.pos)
                else:
                    startButton.checkClick(event.pos)
                    controlButton.checkClick(event.pos)
                    quitButton.checkClick(event.pos)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                if event.button == 1:
                    startButton.checkClick(event.pos)
                    controlButton.checkClick(event.pos)
                    quitButton.checkClick(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.collidePt(event.pos):
                    mode = "inGame"
                if controlButton.collidePt(event.pos):
                   bg =  Background("PNG/backgrounds/controls.png")
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_RETURN:
                            mode = "inGame"
                if quitButton.collidePt(event.pos):
                    sys.exit()
       
        
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
    
    
    while mode == "inGame":
        for s in all.sprites():
            s.kill()
        
        bg.kill()
        bg = Background("PNG/backgrounds/Black.png")
        level = loadLevel("Levels/1.lvl")
        pb = Player(3, level["player"], hasPowers, playerLives) 
        Lifebar(size, bulletMag, playerLives, "PNG/backgrounds/spacemansheart.png")#playerLives
        magazine(size, bulletMag, "PNG/Bolt/bulletmag20.png")
        CoinCount= CoinCounter(PlayerCoins, [980, 150])
        print PlayerCoins

        while pb.alive:
            for event in pygame.event.get():
                #print event
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()
                        if event.key == pygame.K_t:
                            pb.keys = []
                            paused = True
                            while paused:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT: sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_t:
                                            paused = False
                    ###~PLAYER MERCHANT INERACTION~###
                        if event.key == pygame.K_e:
                            for mob in npcs:
                                if mob.kind == "merchant":
                                    # ~ print ">>>>>>>>>>>>>>>>>>>"
                                    if mob.checkPlayer(pb.rect.center):
                                        pb.keys = []
                                        paused = True
                                        ## ~SHOP MENU CODE~ ##
                                        menu = Background("PNG/backgrounds/shopMenu.png")
                                        items = [ShopItem("health plus", [270,400]),
                                                 ShopItem("mag", [490,400]),
                                                 ShopItem("health", [740,400])]
                                        itemIndex = 0
                                        keyPressed = False
                                        while paused:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT: sys.exit()
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_e:
                                                        paused = False
                                                        menu.kill()
                                                        for item in items:
                                                            item.kill()
                                                    if event.key == pygame.K_LEFT:
                                                        if itemIndex > 0:
                                                            itemIndex -= 1
                                                    if event.key == pygame.K_RIGHT:
                                                        if itemIndex < len(items)-1:
                                                            itemIndex += 1
                                                    ###~ITEM SELECT~###
                                                    if event.key == pygame.K_RETURN:
                                                        if itemIndex == 0:
                                                            hasPowers += [items[itemIndex].kind]
                                                        items[itemIndex].kill()
                                                        items[itemIndex] = ShopItem("purchased", items[itemIndex].rect.center)
                                                            
                                                        
                                            
                                            for i,item in enumerate(items):
                                                if i == itemIndex:
                                                    item.doSelect()
                                                else:
                                                    item.stopSelect()
                                            
                                            menu.update()
                                                        
                                            dirty = all.draw(screen)
                                            pygame.display.update(dirty)
                                            pygame.display.flip()
                                            clock.tick(60)
                                            
                                                
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
                            bulletMag = 40
                            
                                    
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
                            pb.speed = (event.value + 1)**3
                            pb.go("go right")
                           # isX = True
                        elif event.value >= -.7:
                            pb.go("s left")
                            pb.go("s right")
                            pb.speed = 0
                           # isX = False
                        elif event.value < -.7:
                            pb.go("go left")
                          #  isX = True
                           
                            
                            
                    if event.axis == 1:
                        if event.value > .7:
                            
                            pb.go("go down")
                        #    isY = True
                        elif event.value >= -.7:
                            pb.go("s up")
                            pb.go("s down")
                            pb.speed = 0
                           # isY = False
                        elif event.value < -.7:
                            pb.go("go up")
                           # isY = True
                                
                    
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
                        bulletMag = 40
                    
            if shooting:
                bullet = pb.shoot()
                if bullet:
                    if bulletMag > 0:
                        bulletMag -= 1
                        if boltPower == True:
                            # ~ print 'yes'
                            pb.shoot(False)  
                if bulletMag == 0:
                    shooting = False
            
            ###~ENEMY WITH PLAYER COLLISIONS~###
            playerHitMobs = pygame.sprite.spritecollide(pb, mobs, False)#, pygame.sprite.collide_mask)   
            for mob in playerHitMobs:
                pb.collide(mob)
                mob.collide(pb)
                if pb.collide(mob):
                    playerLives = pb.lives
            
            ###~BULLET KILL ENEMIES~###
            bulletsHitMobs = pygame.sprite.groupcollide(bullets, mobs, True, False)#, pygame.sprite.collide_mask)
            for bullet in bulletsHitMobs:
                for mob in bulletsHitMobs[bullet]:
                    if mob.collide(bullet): 
                        if mob.lives == 0:
                            if random.randint(0, mob.dropRate) == 0:
                                Coin(mob.rect.center)
                        
            
            ###~POWER UP COLLECTION~###
            playerHitPowerUps = pygame.sprite.spritecollide(pb, powerUps, True)#, pygame.sprite.collide_mask)   
            for power in playerHitPowerUps:
                if pb.collide(power):
                    hasPowers += [power.kind]
                    print hasPowers
            
            ###~COIN COLLECTION~###
            playerHitCoins = pygame.sprite.spritecollide(pb, coins, True)#, pygame.sprite.collide_mask)   
            for coin in playerHitCoins:
                if pb.collide(coin):
                    PlayerCoins += 1
                    # ~ print PlayerCoins
                
            # ~ mobsHitMobs = pygame.sprite.groupcollide(mobs, mobs, False, False, pygame.sprite.collide_mask)
            # ~ for hitter in mobsHitMobs:
                # ~ for hittee in mobsHitMobs[hitter]:

                    # ~ hitter.collide(hittee)
            
            mobsHitBlocks = pygame.sprite.groupcollide(mobs, blocks, False, False)
            for mob in mobsHitBlocks:
                for block in mobsHitBlocks[mob]:
                    mob.collide(block)
                    #mob.bounceBlock(block)
                    
            bulletsHitBlocks = pygame.sprite.groupcollide(bullets, blocks, True, False)
            
            playerHitBlocks = pygame.sprite.spritecollide(pb, blocks, False)
            if len(playerHitBlocks) > 0: 
                print len(playerHitBlocks)
                for block in playerHitBlocks:
                    if pb.collide(block):
                        if block.kind == "warp":
                            if levelnum == 10:
                                mode = "victory"

                            if levelnum == 11:
                                bg = "PNG/backgrounds/end.PNG"

                            else:
                                currentCoins = CoinCount.coin
                                for s in all.sprites():
                                    s.kill()
                                levelnum += 1
                                bg = Background("PNG/backgrounds/Black.png")
                                level = loadLevel("Levels/"+str(levelnum)+".lvl")
                                pb = Player(3, level["player"], hasPowers, playerLives)
                                print pb.lives
                                magazine(size, bulletMag, "PNG/Bolt/bulletmag20.png", "mag" in hasPowers)
                                Lifebar(size, bulletMag, pb.lives, "PNG/backgrounds/spacemansheart.png")#playerLives
                                CoinCount= CoinCounter(currentCoins, [980, 150])



                                    # ~ print levelnum
                                    #blocks = level["blocks"]
                                    #mobs = level["enemies"]
                                    #powerUps = level["power-ups"]\
                                    #bullets = []
                                    #add delay here
            
            all.update(size, pb.rect.center, pb.lives, bulletMag, PlayerCoins, CoinCounter)
                   
                    
            ###~POWER UPS~###
            boltPower = False
            if "speedBoost" in hasPowers:
                pb.maxSpeed = 60
            if "healthUp" in hasPowers:
                playerLives = 8
                pb.lives = playerLives
                hasPowers.remove("healthUp")
                print pb.lives
            if "boltPower" in hasPowers:
                boltPower = True
                
            ###~UPGRADES~###
            if "mag" in hasPowers:
                magPlus = True
                
                    
            for mob in mobs.sprites():
                #~ MOB LIMIT
                if mob.kind == "greenie" and len(mobs.sprites()) < 15:
                    if mob.checkDuplicate():
                        mob.duplicate()
                
            dirty = all.draw(screen)
            pygame.display.update(dirty)
            pygame.display.flip()
            clock.tick(60)
            
        while not pb.alive:
            for s in all.sprites():
                s.kill()
            hasPowers = []
            PlayerCoins = 0
            bg = Background("PNG/backgrounds/endscreen.png")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        mode = "menu"
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            levelnum = 1
                            #bullets = []
                            level = loadLevel("Levels/"+str(levelnum)+".lvl")
                            # ~ blocks = level["blocks"]
                            # ~ mobs = level["enemies"]
                            # ~ powerUps = level["power-ups"]
                            playerLives = 5
                            pb = Player(3, level["player"], hasPowers, playerLives)
                            magazine(size, bulletMag, "PNG/Bolt/bulletmag20.png")
                            Lifebar(size, bulletMag, playerLives, "PNG/backgrounds/spacemansheart.png")#playerLives
                            

                            bulletMag = 40
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
                    
            dirty = all.draw(screen)
            pygame.display.update(dirty)
            pygame.display.flip()
            clock.tick(60)

    
    while mode == "victory":
        bg = Background("PNG/backgrounds/winendgame.png")
        for event in pygame.event.get():
                    #print event.type
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                mode = "menu"
                            if event.key == pygame.K_ESCAPE:
                                sys.exit()
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

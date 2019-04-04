import pygame, sys, math, random
from mob import *


class Imposter(Mob):
    def __init__(self, speed=5, startPos=[0,0]):
        Mob.__init__(self, "PNG/Enemy2/Imposter-Down.png", [0,0], startPos)
        self.rightImages = [pygame.image.load("PNG/Enemy2/Imposter-Right1.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Right2.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Right3.png"),
                        ]
        self.leftImages = [pygame.image.load("PNG/Enemy2/Imposter-Left1.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Left2.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Left3.png"),
                        ]
        self.upImages = [pygame.image.load("PNG/Enemy2/Imposter-Up.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Up.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Up.png"),
                        ]
        self.downImages = [pygame.image.load("PNG/Enemy2/Imposter-Down.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Down.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Down.png"),
                        ]
        self.seen = False
        self.kind = "imposter"
        self.images = self.upImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        self.maxspeed = speed
        self.goal = [0,0]
        self.tracking = True
        self.compass = 0
        self.directMove()
        
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.detectionRadius = 96
        
    
        
        self.lives = 6
        
        
    def setPos(self, pos):
        self.rect.center = pos0
        
    def directMove(self, pCenter=None):
        if pCenter and self.getDist(pCenter) < 250:
            self.tracking = True
            xDif = abs(self.rect.centerx - pCenter[0])
            yDif = abs(self.rect.centery - pCenter[1])
            
            # print xDif, yDif, self.rect.center, pCenter
            
            if xDif > yDif:
                if self.rect.centerx < pCenter[0]:
                    self.compass = 1
                    # print "Player Right"
                else:
                    self.compass = 3
                    # print "Player Left"
            else:
                if self.rect.centery > pCenter[1]:
                    self.compass = 0
                    # print "Player Above"
                else:
                    self.compass = 2
                    # print "Player Below"
                
        else:
            if self.tracking: 
                self.tracking = False
                self.compass = random.randint(0, 3)
            elif random.randint (0, 60) == 0:
                self.compass = random.randint(0, 3)
            

        
        
        
        if self.compass == 0:
            self.moving = "Y"
            self.speedy = -self.maxspeed
            self.speedx = 0
            self.images = self.upImages
        elif self.compass == 1:
            self.moving = "X"
            self.speedx = self.maxspeed
            self.speedy = 0
            self.images = self.rightImages
        elif self.compass == 2:
            self.moving = "Y"
            self.speedy = self.maxspeed
            self.speedx = 0
            self.images = self.downImages
        elif self.compass == 3:
            self.moving = "X"
            self.speedx = -self.maxspeed
            self.speedy = 0
            self.images = self.leftImages
        # ~ self.image = self.images[self.frame]
        # ~ self.rect = self.image.get_rect()
            
        self.rect = self.rect.move(self.speed)
            
    def update(self, size, pCenter):
        # ~ print self.rect.center
        self.didBounceX = False
        self.didBounceY = False
        self.directMove(pCenter)
        self.move()
        self.bounceWall(size)
        self.animate()
        self.live(self.lives)


    def collide(self, other):
        if other.kind == "bolt":
            self.lives += -1
        if not self.didBounceX:
            if self.speedx > 1: #right
                if self.rect.centerx < other.rect.centerx:
                    self.speedx = -self.speedx
                    self.move()
                    self.directMove()
                    self.didBounceX = True
                   
            if self.speedx < 1: #left
                if self.rect.centerx > other.rect.centerx:
                    self.speedx = -self.speedx
                    self.move()
                    self.directMove()
                    self.didBounceX = True
                    
        if not self.didBounceY:
            if self.speedy > 1: #down
                if self.rect.centery < other.rect.centery:
                    self.speedy = -self.speedy
                    self.move()
                    self.directMove()
                    self.didBounceY = True
                    # ~ if self.rect.bottom > other.rect.top:
                        # ~ self.rect.centery = other.rect.centery - ((self.rect.height)/2 + (other.rect.height)/2)

            if self.speedy < 1: #up
                if self.rect.centery > other.rect.centery:
                    self.speedy  = -self.speedy
                    self.move()
                    self.directMove()
                    self.didBounceY = True
                    # ~ if self.rect.top < other.rect.bottom:
                        # ~ self.rect.centery = other.rect.centery + (self.rect.height)/2 + (other.rect.height)/2

        return True
        
    def bounceBlock(self, other):
        if self.rect.left < other.rect.right or self.rect.right > other.rect.left:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
        if self.rect.top < other.rect.bottom or self.rect.bottom > other.rect.top:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True

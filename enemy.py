import pygame, sys, math, random
from mob import *


class SpaceZombie(Mob):
    def __init__(self, speed=5, startPos=[0,0]):
        Mob.__init__(self, "PNG/Enemy/Zombie-Down.png", [0,0], startPos)
        self.rightImages = [pygame.image.load("PNG/Enemy/Zombie-Right1.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Right2.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Right3.png"),
                        ]
        self.leftImages = [pygame.image.load("PNG/Enemy/Zombie-Left1.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Left2.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Left3.png"),
                        ]
        self.upImages = [pygame.image.load("PNG/Enemy/Zombie-Up.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Up.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Up.png"),
                        ]
        self.downImages = [pygame.image.load("PNG/Enemy/Zombie-Down.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Down.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Down.png"),
                        ]
        
        self.kind = "enemy"
        self.maxspeed = speed
        self.images = self.downImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        #self.maxspeed = speed
        self.goal = [0,0]
        self.directMove()
        self.dropRate = 15
        self.lives = 3
        
    def setPos(self, pos):
        self.rect.center = pos0
        
    #Random Movement
        
    def directMove(self):
        compass = random.randint(0, 3)
        if compass == 0:
            self.moving = "Y"
            self.speedy = -self.maxspeed
            self.speedx = 0
            self.images = self.upImages
        elif compass == 1:
            self.moving = "X"
            self.speedx = self.maxspeed
            self.speedy = 0
            self.images = self.rightImages
        elif compass == 2:
            self.moving = "Y"
            self.speedy = self.maxspeed
            self.speedx = 0
            self.images = self.downImages
        elif compass == 3:
            self.moving = "X"
            self.speedx = -self.maxspeed
            self.speedy = 0
            self.images = self.leftImages
        # ~ self.image = self.images[self.frame]
        # ~ self.rect = self.image.get_rect()
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        # ~ print self.rect.centerx%50-25, self.rect.centery%50-25
        if self.speedx != 0:  #mov'n x
            if self.rect.centerx%50-25 == 0:
                # ~ print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                if random.randint(0,3) == 0:
                    self.directMove()
        
        if self.speedy != 0:
            if  self.rect.centery%50-25 == 0:
                # ~ print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                if random.randint(0,3) == 0:
                    self.directMove()
                    
        self.rect = self.rect.move(self.speed)




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
                
    

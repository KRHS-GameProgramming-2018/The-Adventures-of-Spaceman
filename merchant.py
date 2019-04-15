import sys, math, pygame
from mob import *

class Merchant(Mob):
    def __init__(self, speed=0, startPos=[0,0]):
        Mob.__init__(self, "PNG/Merchant/merchant-down.png", [0,0], startPos)
        self.rightImages = [pygame.image.load("PNG/Merchant/merchant-right.png")
                        ]
        self.leftImages = [pygame.image.load("PNG/Merchant/merchant-left.png")
                        ]
        self.upImages = [pygame.image.load("PNG/Merchant/merchant-up.png")
                        ]
        self.downImages = [pygame.image.load("PNG/Merchant/merchant-down.png"),
                        ]
    
        self.seen = False
        self.kind = "merchant"
        self.images = self.upImages
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        self.goal = [0,0]
        self.tracking = True
        self.compass = 0
        self.directMove()
    
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.detectionRadius = 96
    
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
                    
                    
            if self.compass == 0:
                self.images = self.upImages
            elif self.compass == 1:
                self.images = self.rightImages
            elif self.compass == 2:
                self.images = self.downImages
            elif self.compass == 3:
                self.images = self.leftImages
                
    def update(self, size, pCenter):
        # ~ print self.rect.center
        self.directMove(pCenter)
        self.animate()
        
    def checkPlayer(self, point):
        if self.getDist(point) < self.detectionRadius:
            return True
        else:
            return False

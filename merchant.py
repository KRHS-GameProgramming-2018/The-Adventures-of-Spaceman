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
    
    self.kind = "merchant"
    self.images = self.upImages
    self.image = self.images[self.frame]
    self.rect = self.image.get_rect(center = startPos)
    
    self.goal = [0,0]
    self.tracking = True
    self.compass = 0
    self.directMove()
    
    
    
    
    
    
    
    
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

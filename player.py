import sys, math, pygame
from mob import *
#https://opengameart.org/content/space-man-space-bot-rework
class PlayerBall(Ball):
    def __init__(self, speed=10, startPos=[0,0]):
        Ball.__init__(self, "PNG/Player/spaceman.png", [0,0], startPos)
        self.upImages = [pygame.image.load("PNG/Player/spaceman-up.png"),
                        pygame.image.load("PNG/Player/spaceman-up.png"),
                        pygame.image.load("PNG/Player/spaceman-up.png"),
                        ]
        self.downImages = [pygame.image.load("PNG/Player/spaceman.png"),
                          pygame.image.load("PNG/Player/spaceman.png"),
                          pygame.image.load("PNG/Player/spaceman.png"),
                          ]
        self.leftImages = [pygame.image.load("PNG/Player/spaceman-left-1.png"),
                          pygame.image.load("PNG/Player/spaceman-left-2.png"),
                          pygame.image.load("PNG/Player/spaceman-left-3.png"),
                          ]
        self.rightImages = [pygame.image.load("PNG/Player/spaceman-right-1.png"),
                           pygame.image.load("PNG/Player/spaceman-right-2.png"),
                           pygame.image.load("PNG/Player/spaceman-right-3.png"),
                           ]
        self.images = self.downImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        self.maxSpeed = speed
        self.boostSpeed = speed*2
        self.normalSpeed = speed
        self.keys = []
        self.goal = [0,0]
        
        self.didBounceX = False
        self.didBounceY = False
            
    def go(self, d, f):
        
        if d == "":
            return
        if d == "up":
            self.speedy = -self.maxSpeed
        if d == "down":
            self.speedy = self.maxSpeed
        if d == "left":
            self.speedx = -self.maxSpeed
        if d == "right":
            self.speedx = self.maxSpeed
            
        if d == "sup":
            self.speedy = 0
        if d == "sdown":
            self.speedy = 0
        if d == "sleft":
            self.speedx = 0
        if d == "sright":
            self.speedx = 0
        
        if f == "":
            f = d
        
        if f == "up":
            self.images = self.upImages
        if f == "down":
            self.images = self.downImages
        if f == "left":
            self.images = self.leftImages
        if f == "right":
            self.images = self.rightImages
        else:
            f = d
            print f
            
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if not self.didBounceX:
                            if self.speedx > 1: #right
                                if self.rect.centerx < other.rect.centerx:
                                    self.speedx = -self.speedx
                                    self.move()
                                    self.speedx = 0
                                    self.didBounceX = True
                                   
                            if self.speedx < 1: #left
                                if self.rect.centerx > other.rect.centerx:
                                    self.speedx = -self.speedx
                                    self.move()
                                    self.speedx = 0
                                    self.didBounceX = True
                                    
                        if not self.didBounceY:
                            if self.speedy > 1: #down
                                if self.rect.centery < other.rect.centery:
                                    self.speedy = -self.speedy
                                    self.move()
                                    self.speedy = 0
                                    self.didBounceY = True
                                    # ~ if self.rect.bottom > other.rect.top:
                                        # ~ self.rect.centery = other.rect.centery - ((self.rect.height)/2 + (other.rect.height)/2)

                            if self.speedy < 1: #up
                                if self.rect.centery > other.rect.centery:
                                    self.speedy  = -self.speedy
                                    self.move()
                                    self.speedy = 0
                                    self.didBounceY = True
                                    # ~ if self.rect.top < other.rect.bottom:
                                        # ~ self.rect.centery = other.rect.centery + (self.rect.height)/2 + (other.rect.height)/2

                        return True
        return False
    
    def bounceBlock(self, other):
        if self.rect.left < other.rect.right or self.rect.right > other.rect.left:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
        if self.rect.top < other.rect.bottom or self.rect.bottom > other.rect.top:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True
                
    

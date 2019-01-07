import sys, math, pygame
from mob import *
from bolt import *
#https://opengameart.org/content/space-man-space-bot-rework
class Player(Mob):
    def __init__(self, speed=10, startPos=[0,0]):
        Mob.__init__(self, "PNG/Player/spaceman.png", [0,0], startPos)
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
        self.kind = "player"
        self.health = 3
        
        self.didBounceX = False
        self.didBounceY = False
        
        
        self.fireTimer = 0
        self.fireTimerMax = 60/15
        # ~ self.facing = "down"
        
        self.invincTimer = 0
        self.invincTimerMax = 120
        
        
    def go(self, d):
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
        
    def face(self, y):
        mode, direction = y.split(" ")
        if mode == "face":
            self.keys += [direction]
        elif mode == "stop":
            self.keys.remove(direction)
        
        
        if self.keys:
            if self.keys[-1] == "left":
                self.images = self.leftImages
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.keys[-1] == "right":
                self.images = self.rightImages
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.keys[-1] == "up":
                self.images = self.upImages
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.keys[-1] == "down":
                self.images = self.downImages
                self.rect = self.image.get_rect(center = self.rect.center)
                
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if other.kind == "enemy":
                            self.health += -1
                            if self.invincTimer < self.invincTimerMax:
                                  self.invincTimer += 1
                                  if self.invincTimer == self.invincTimerMax:
                                      self.invincTimer = 0
              
                            print self.health
                        elif not self.didBounceX:
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
            if self.rect.top < other.rect.bottom or self.rect.bottom > other.rect.top:
                if other.kind == "block":
                    if not self.didBounceX:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                    if not self.didBounceY:
                        self.speedy = -self.speedy
                        self.didBounceY = True
                return True
        return False
        
    def shooting(self, firing):
        if firing == "yes":
            if self.fireTimer < self.fireTimerMax:
                self.fireTimer += 1
            print 'blasting'
        else:
            self.fireTimer = 0
            return bolt()
        if firing == "no":
            return
            
    def update(self, size):
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
        self.animate()
        if len(self.keys) == 0:
            if self.speedx < 0:
                self.images = self.leftImages
            if self.speedx > 0:
                self.images = self.rightImages
            if self.speedx == 0:
                if self.speedy < 0:
                    self.images = self.upImages
                if self.speedy >= 0:
                    self.images = self.downImages
                    
    
    

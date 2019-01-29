import sys, math, pygame
from mob import *
from bolt import *
#https://opengameart.org/content/space-man-space-bot-rework
class Player(Mob):
    def __init__(self, speed=6, startPos=[0,0]):
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
        self.y = "down"
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        self.maxSpeed = speed
        self.boostSpeed = speed*2
        self.normalSpeed = speed
        self.faceKeys = []
        self.keys = []
        self.goal = [0,0]
        self.kind = "player"
        self.lives = 3
        
        self.didBounceX = False
        self.didBounceY = False
        
        
        self.fireTimer = 0
        self.fireTimerMax = 60/15
        self.bullets = []
        self.firing = False
        # ~ self.facing = "down"
        
        self.alive = True
        self.invincTimer = 0
        self.invincTimerMax = 1
        
        
    # ~ def go(self, d):
        # ~ if d == "go up":
            # ~ self.speedy = -self.maxSpeed
        # ~ if d == "go down":
            # ~ self.speedy = self.maxSpeed
        # ~ if d == "go left":
            # ~ self.speedx = -self.maxSpeed
        # ~ if d == "go right":
            # ~ self.speedx = self.maxSpeed
            
        # ~ if d == "s up":
            # ~ self.speedy = 0
        # ~ if d == "s down":
            # ~ self.speedy = 0
        # ~ if d == "s left":
            # ~ self.speedx = 0
        # ~ if d == "s right":
            # ~ self.speedx = 0
        
        
    def go(self, d):
        mode, direction = d.split(" ")
        if mode == "go":
            self.keys += [direction]
        elif mode == "s":
            try:
                self.keys.remove(direction)
                if direction == "left" or "right":
                    self.speedx = 0
                if direction == "up" or "down":
                    self.speedy = 0
            except:
                return
        if self.keys:
            if self.keys[-1] == "left":
                self.speedx = -self.maxSpeed
                
            elif self.keys[-1] == "right":
                self.speedx = self.maxSpeed
            
            elif self.keys[-1] == "up":
                self.speedy = -self.maxSpeed
                
            elif self.keys[-1] == "down":
                self.speedy = self.maxSpeed
            
    def face(self, y):
        mode, direction = y.split(" ")
        if mode == "face":
            self.faceKeys += [direction]
        elif mode == "stop":
            try:
                self.faceKeys.remove(direction)
            except:
                return
        
        
        if self.faceKeys:
            if self.faceKeys[-1] == "left":
                self.images = self.leftImages
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.faceKeys[-1] == "right":
                self.images = self.rightImages
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.faceKeys[-1] == "up":
                self.images = self.upImages
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.faceKeys[-1] == "down":
                self.images = self.downImages
                self.rect = self.image.get_rect(center = self.rect.center)
                
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if other.kind == "enemy":
                            self.lives += -1
                            print self.lives
                            if self.invincTimer < self.invincTimerMax:
                                  self.invincTimer += 1
                                  if self.invincTimer == self.invincTimerMax:
                                      self.invincTimer = 0
                        if not other.kind == "enemy":
                  
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
                                       

                                if self.speedy < 1: #up
                                    if self.rect.centery > other.rect.centery:
                                        self.speedy  = -self.speedy
                                        self.move()
                                        self.speedy = 0
                                        self.didBounceY = True
                                        

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
    
    def facingDirection(self):
        if self.images == self.downImages:
            self.y = "down"
        if self.images == self.upImages:
            self.y = "up"
        if self.images == self.leftImages:
            self.y = "left"
        if self.images == self.rightImages:
            self.y = "right"
            
    def shoot(self):
        if self.firing:
            pass
        else:
            self.firing = True
            self.fireTimer = 0
            print self.rect.center, self.y
            if self.y == "down":
                speed = [0,9]
                image = "PNG/Bolt/spacemanbolt-down.png"
            if self.y == "up":
                speed = [0,-9]
                image = "PNG/Bolt/spacemanbolt-up.png"
            if self.y == "left":
                speed = [-9,0]
                image = "PNG/Bolt/spacemanbolt-left.png"
            if self.y == "right":
                speed = [9,0]
                image = "PNG/Bolt/spacemanbolt-right.png"
            
            return Bolt(image, speed, self.rect.center)
            
            
            
    def update(self, size):
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.live(self.lives)
        self.bounceWall(size)
        self.animate()
        self.facingDirection()
        if len(self.faceKeys) == 0:
            if self.speedx < 0:
                self.images = self.leftImages
            if self.speedx > 0:
                self.images = self.rightImages
            if self.speedx == 0:
                if self.speedy < 0:
                    self.images = self.upImages
                if self.speedy >= 0:
                    self.images = self.downImages
        
        if self.firing:
            if self.fireTimer < self.fireTimerMax:
                self.fireTimer += 1
            else:
                self.fireTimer = 0
                self.firing = False

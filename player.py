import sys, math, pygame
from mob import *
from bolt import *

from boltPower import *
from healthUp import *
from speedBoost import *
from Coin import *
#https://opengameart.org/content/space-man-space-bot-rework
class Player(Mob):
    def __init__(self, speed=6, startPos=[0,0], powers=[], playerLives=6):
        Mob.__init__(self, "PNG/Player/spaceman.png", [0,0], startPos)
        self.notMoving = [pygame.image.load("PNG/Player/spaceman.png"),
                        pygame.image.load("PNG/Player/spaceman.png"),
                        pygame.image.load("PNG/Player/spaceman.png"),
                        ]
        self.upImages = [pygame.image.load("PNG/Player/spacemanFoward1.png"),
                        pygame.image.load("PNG/Player/spacemanFoward2.png"),
                        pygame.image.load("PNG/Player/spacemanFoward3.png"),
                        ]
        self.downImages = [pygame.image.load("PNG/Player/spaceman.png"),
                          pygame.image.load("PNG/Player/spaceman2.png"),
                          pygame.image.load("PNG/Player/spaceman3.png"),
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
        self.faceKeys = []
        self.keys = []
        self.goal = [0,0]
        self.kind = "player"
        self.lives = playerLives
        
        
        self.didBounceX = False
        self.didBounceY = False
        
        
        self.fireTimer = 0
        self.fireTimerMax = 60/3
        self.bullets = []
        self.firing = False
        # ~ self.facing = "down"
        
        self.alive = True
        self.invincible = False
        self.invincTimer = 0
        self.invincTimerMax = 60
        
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
        if other.kind == "warp":
            pass
        if not self.invincible and (other.kind == "enemy" or other.kind == "greenie" or other.kind == "imposter"): #get hurt
            self.lives += -1
            print "gets hurt"
            self.invincible = True
            if self.lives == 0:
                self.alive = False
        if not (other.kind == "warp" or other.kind == "Coin"):
            Mob.collide(self, other)
        return True
    
   
    
    
    def facingDirection(self):
        if self.images == self.downImages or self.images == self.notMoving:
            self.y = "down"
        if self.images == self.upImages:
            self.y = "up"
        if self.images == self.leftImages:
            self.y = "left"
        if self.images == self.rightImages:
            self.y = "right"
            
    def shoot(self, testingFire=True):
        if testingFire and self.firing:
            if self.fireTimer < self.fireTimerMax:
                self.fireTimer += 1
            else:
                self.fireTimer = 0
                self.firing = False
        else:
            self.firing = True
            if self.y == "down":
                speed = [0,10]
                image = "PNG/Bolt/spacemanbolt-down.png"
            if self.y == "up":
                speed = [0,-10]
                image = "PNG/Bolt/spacemanbolt-up.png"
            if self.y == "left":
                speed = [-10,0]
                image = "PNG/Bolt/spacemanbolt-left.png"
            if self.y == "right":
                speed = [10,0]
                image = "PNG/Bolt/spacemanbolt-right.png"
            
            return Bolt(image, speed, self.rect.center)
            
            
            
    def update(*args):
        self = args[0]
        size = args[1]
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
                
        if self.invincible:
            if self.invincTimer < self.invincTimerMax:
                self.invincTimer += 1
            else:
                self.invincTimer = 0
                self.invincible = False
                
        if self.lives < 0:
            self.alive = False
    
    
    

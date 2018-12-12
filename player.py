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
        self.aniTimerMax = 60/20
        
        self.maxSpeed = speed
        self.boostSpeed = speed*2
        self.normalSpeed = speed
        self.keys = []
        self.goal = [0,0]
        
        self.didBounceX = False
        self.didBounceY = False
            
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
        
    def face(self, f):
        
        if f == "up":
            self.images = self.upImages
        if f == "down":
            self.images = self.downImages
        if f == "left":
            self.images = self.leftImages
        if f == "right":
            self.images = self.rightImages
        # ~ if f == "check":
            # ~ self.face(f)

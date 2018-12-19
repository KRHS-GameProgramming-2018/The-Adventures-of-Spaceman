import pygame, sys, math
from mob import *


class SpaceZombie(Mob):
    def __init__(self, speed=5, startPos=[0,0]):
        Mob.__init__(self, "PNG/Enemy/Zombie-Down.png", [0,0], startPos)
        self.rightImages = [pygame.image.load("PNG/Enemy/Zombie-Right1.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Right2.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Right3.png"),]
        self.leftImages = [pygame.image.load("PNG/Enemy/Zombie-Left1.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Left2.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Left3.png"),]
        self.upImages = [pygame.image.load("PNG/Enemy/Zombie-Up.png")]
        self.downImages = [pygame.image.load("PNG/Enemy/Zombie-Down.png"),]
        
        
        self.images = self.downImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        self.maxspeed = speed
        self.boostSpeed = speed*2
        self.normalSpeed = speed
        self.goal = [0,0]
        
    def setPos(self, pos):
        self.rect.center = pos0
        
    def directMove(self):
        compass = random.randint(0, 3)
        if compass == 0:
            self.speedy = -self.speedy
        elif compass == 1:
            self.speedx = self.speedx
        elif compass == 2:
            self.speedy = self.speedy
        elif compass == 3:
            self.speedx = -self.speedx
    
    # ~ def go(self, d, y):
        
        # ~ if d == "":
            # ~ return
        # ~ if d == "up":
            # ~ self.speedy = -self.maxSpeed
        # ~ if d == "down":
            # ~ self.speedy = self.maxSpeed
        # ~ if d == "left":
            # ~ self.speedx = -self.maxSpeed
        # ~ if d == "right":
            # ~ self.speedx = self.maxSpeed
            
        # ~ if d == "sup":
            # ~ self.speedy = 0
        # ~ if d == "sdown":
            # ~ self.speedy = 0
        # ~ if d == "sleft":
            # ~ self.speedx = 0
        # ~ if d == "sright":
            # ~ self.speedx = 0
        
        # ~ if y == "":
            # ~ if self.speedy < 0:
                # ~ self.images = self.upImages
                # ~ if self.speedx < 0:
                    # ~ self.images = self.leftImages
                # ~ if self.speedx > 0:
                    # ~ self.images = self.rightImages
            # ~ if self.speedy >= 0:
                # ~ self.images = self.downImages
                # ~ if self.speedx < 0:
                    # ~ self.images = self.leftImages
                # ~ if self.speedx > 0:
                    # ~ self.images = self.rightImages
            
        # ~ if y == "up":
            # ~ self.images = self.upImages
        # ~ if y == "down":
            # ~ self.images = self.downImages
        # ~ if y == "left":
            # ~ self.images = self.leftImages
        # ~ if y == "right":
            # ~ self.images = self.rightImages
            
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

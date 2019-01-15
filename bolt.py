import sys, math, pygame
from mob import *
from player import *

class Bolt(Mob):
    def __init__(self, image="PNG/Bolt/bolt-1.png", speed=10, startPos=[0,0]):
        Mob.__init__(self,  image, speed, startPos)
        # ~ print self.rect.center, speed
        self.kind = "bolt"
        self.lives = 1
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if self.radius + other.radius > self.getDist(other.rect.center):
                            self.alive = False
        return False

import sys, math, pygame
from mob import *
from player import *

class Tripleshot(Mob):
    def __init__(self, startPos=[0,0]):
        Mob.__init__(self,  "PNG/Power-ups/Tripleshot.png", [0,0], startPos)
        # ~ print self.rect.center, speed
        self.kind = "tripleShot"
        self.lives = 1
        self.alive = True
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if self.radius + other.radius > self.getDist(other.rect.center):
                            if other.kind == "player":
                                self.lives = 0
                                self.alive = False
        return False


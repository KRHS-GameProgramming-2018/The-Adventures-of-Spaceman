import sys, math, pygame
from mob import *
from player import *

class Bolt(Mob):
    def __init__(self, image="PNG/Bolt/bolt-1.png", speed=10, startPos=[0,0]):
        Mob.__init__(self,  image, speed, startPos)
        # ~ print self.rect.center, speed
        self.kind = "bolt"
        self.lives = 1
        
    

import sys, math, pygame
from mob import *
from player import *

class Bolt(Mob):
    def __init__(self, speed=10, startPos=[0,0]):
        Mob.__init__(self,  "PNG/Player/spaceman.png", speed, startPos)
        print self.rect.center, speed

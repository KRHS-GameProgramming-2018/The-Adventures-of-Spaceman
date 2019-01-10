import sys, math, pygame
from mob import *
from player import *

class Bolt(Mob):
    def __init__(self, image, speed=10, startPos=[0,0]):
        Mob.__init__(self,  "PNG/Player/spaceman.png", [-7,0], startPos)

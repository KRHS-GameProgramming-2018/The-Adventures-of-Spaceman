import sys, math, pygame
from mob import *
from player import *

class Bolt(Mob):
    def __init__(self, direction, speed=10, startPos=[0,0]):
        Mob.__init__(self, direction, "PNG/Player/spaceman.png", [0,0], startPos)

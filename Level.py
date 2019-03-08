import pygame, sys, math, random
from player import *
from Block import *
from warp import *
from enemy import *
from Imposter import *
from tripleShot import *
from Greenie import *

def loadLevel(levelFile):
    f = open(levelFile, 'r')
    lines = f.readlines()
    f.close()
    
    level = {"blocks":[],
             "player":[0,0],
             "enemies":[],
             "power-ups":[]
             }
    
    #Block Size is 50x50
    
    newLines = []
    for line in lines:
        newLine = ""
        for character in line:
            if not (character == '\n'):
                newLine += character
        newLines += [newLine]
    lines = newLines
    
    for line in lines:
        print line
        
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            if character == '#':
                level["blocks"] += [Block([x*50+25, y*50+25])]
            if character == '@':
                level["blocks"] += [Warp([x*50+25, y*50+25])]
            if character == "%":
                level["player"] = [x*50+25, y*50+25]
            if character == 'x':
                level["enemies"] += [SpaceZombie(4, [x*50+25, y*50+25])]
            if character == 'm':
                level["enemies"] += [Imposter(1.5, [x*50+25, y*50+25])]
            if character == 'g':
                level["enemies"] += [Greenie(3, [x*50+25, y*50+25])]
            if character == '!':
                level["power-ups"] += [boltPower([x*50+25, y*50+25])]
            if character == '[':
                level["power-ups"] += [speedBoost([x*50+25, y*50+25])]
            if character == '<':
                level["power-ups"] += [healthUp([x*50+25, y*50+25])]
    return level
    
    
    
# ~ loadLevel("Levels/1.lvl")

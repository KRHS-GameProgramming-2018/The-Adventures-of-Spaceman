import pygame, sys, math, random
from player import *
from Block import *
from warp import *
from enemy import *

def loadLevel(levelFile):
    f = open(levelFile, 'r')
    lines = f.readlines()
    f.close()
    
    level = {"blocks":[],
             "player":[0,0],
             "enemies":[]
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
                level["enemies"] += [SpaceZombie(2, [x*50+25, y*50+25])]
            
    return level
    
    
    
# ~ loadLevel("Levels/1.lvl")

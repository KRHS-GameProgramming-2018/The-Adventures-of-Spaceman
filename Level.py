import pygame, sys, math, random
from player import *
from Block import *
from warp import *
from enemy import *
from Imposter import *
from merchant import *
from tripleShot import *
from Greenie import *
# from fishy import *

def loadLevel(levelFile):
    f = open(levelFile, 'r')
    lines = f.readlines()
    f.close()
    
    level = {"blocks":[],
             "player":[0,0],
             "enemies":[],
             "merchant":[],
             "power-ups":[],
             "fish":[]
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
                level["blocks"] += [Block("PNG/Blocks/br1.png",[x*50+25, y*50+25])]
            if character == '=':
                level["blocks"] += [Block("PNG/Blocks/br2.png",[x*50+25, y*50+25])]
            if character == 'v':
                level["blocks"] += [Block("PNG/Blocks/br3.png",[x*50+25, y*50+25])]
            if character == '^':
                level["blocks"] += [Block("PNG/Blocks/br4.png",[x*50+25, y*50+25])]
            if character == '&':
                level["blocks"] += [Block("PNG/Blocks/br5.png",[x*50+25, y*50+25])]
            if character == '/':
                level["blocks"] += [Block("PNG/Blocks/br6.png",[x*50+25, y*50+25])]
            if character == '?':
                level["blocks"] += [Block("PNG/Blocks/br7.png",[x*50+25, y*50+25])]
            if character == '+':
                level["blocks"] += [Block("PNG/Blocks/br8.png",[x*50+25, y*50+25])]
            if character == '*':
                level["blocks"] += [Block("PNG/Blocks/br9.png",[x*50+25, y*50+25])]
            if character == '}':
                level["blocks"] += [Block("PNG/Blocks/br10.png",[x*50+25, y*50+25])]
            if character == '{':
                level["blocks"] += [Block("PNG/Blocks/br11.png",[x*50+25, y*50+25])]
            if character == 'W':
                level["blocks"] += [Block("PNG/Blocks/br12.png",[x*50+25, y*50+25])]
            if character == 'A':
                level["blocks"] += [Block("PNG/Blocks/br13.png",[x*50+25, y*50+25])]
            if character == '-':
                level["blocks"] += [Block("PNG/Blocks/br14.png",[x*50+25, y*50+25])]
            if character == '|':
                level["blocks"] += [Block("PNG/Blocks/br15.png",[x*50+25, y*50+25])]
            if character == '@':
                level["blocks"] += [Warp([x*50+25, y*50+25])]
            if character == "%":
                level["player"] = [x*50+25, y*50+25]
            if character == 'x':
                level["enemies"] += [SpaceZombie(3, [x*50+25, y*50+25])]
            if character == 'm':
                level["enemies"] += [Imposter(1.5, [x*50+25, y*50+25])]
            if character == 'g':
                level["enemies"] += [Greenie(2, [x*50+25, y*50+25])]
            if character == '$':
                level["merchant"] += [Merchant(0, [x*50+25, y*50+25])]
            if character == '!':
                level["power-ups"] += [boltPower([x*50+25, y*50+25])]
            if character == '[':
                level["power-ups"] += [speedBoost([x*50+25, y*50+25])]
            if character == '<':
                level["power-ups"] += [healthUp([x*50+25, y*50+25])]
            if character == 'c':
                level["power-ups"] += [Coin([x*50+25, y*50+25])]
            if character == 'f':
                level["fish"] = [Block("PNG/fish/fish.png", [x*50+25, y*50+25])]
    return level
    
    
    

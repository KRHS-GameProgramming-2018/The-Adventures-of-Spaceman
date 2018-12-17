import pygame, sys, math
from mob import *


class SpaceZombie(Mob):
    def __init__(self, maxSpeed, startPos=[0,0]):
        self.rightImages = [pygame.image.load("PNG/Enemy/Zombie-Right1.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Right2.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Right3.png"),]
        self.leftImages = [pygame.image.load("PNG/Enemy/Zombie-Left1.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Left2.png"),
                        pygame.image.load("PNG/Enemy/Zombie-Left3.png"),]
        self.upImages = [pygame.image.load("PNG/Enemy/Zombie-Back.png")]
        self.downImages = [pygame.image.load("PNG/Enemy/Zombie-Front.png"),]
        
        
        self.frame = 0;
        self.images = self.rightImages
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        self.maxSpeed = maxSpeed
        self.boostSpeed = speed*2
        self.normalSpeed = speed
        self.keys = []
        self.goal = [0,0]
        
    def setPos(self, pos):
        self.rect.center = pos

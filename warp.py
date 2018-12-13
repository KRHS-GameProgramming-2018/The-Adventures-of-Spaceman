#test Owen
import pygame, sys, math

class Warp():
    def __init__(self,  pos=[0,0]):
        self.image = pygame.image.load("PNG/Blocks/warp.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

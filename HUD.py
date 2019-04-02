import pygame, sys, math
from HUDobject import *

#HealthBar and Power Ups 
class GameDisplay(pygame.sprite.Sprite):
        def __init__(self, size, bullets, lives):
            self.rect = self.image.get_rect()
            
        def update(self, size, bullets, lives):
            for bullet in bullets:
                GameDisplayObject(image = "spacemansheat.png", pos = [0,0])
    

#test Owen
import pygame, sys, math

class Warp(pygame.sprite.Sprite):
    def __init__(self,  pos=[0,0]):
        self.images = [ pygame.image.load("PNG/Blocks/warp.png"),
                        pygame.image.load("PNG/Blocks/warp2.png"),
                        pygame.image.load("PNG/Blocks/warp3.png"),
                        pygame.image.load("PNG/Blocks/warp4.png"),
                        pygame.image.load("PNG/Blocks/warp5.png"),
                        pygame.image.load("PNG/Blocks/warp6.png"),
                        pygame.image.load("PNG/Blocks/warp7.png"),
                        pygame.image.load("PNG/Blocks/warp8.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.kind = "warp"
        self.aniTimer = 0
        self.aniTimerMax = 60/15
        
        currentImage = 0
        lastImage = len(self.images)-1
        self.image = self.images [currentImage]
    
    
    
    def update(self,image):
        #self.animate()
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            self.image = self.images[currentImage]
        
        

import pygame, sys, math

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=pos)
        #self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.kind = "block"
    
    def update(*args):
            pass


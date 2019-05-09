import pygame, sys, math


#HealthBar and Power Ups 
class CoinCounter(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives, image):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.coinImages = [pygame.image.load("PNG/backgrounds/h1.png"),
                       pygame.image.load("PNG/backgrounds/h2.png"),
                       pygame.image.load("PNG/backgrounds/h3.png"),
                       pygame.image.load("PNG/backgrounds/h4.png"),
                       pygame.image.load("PNG/backgrounds/h5.png"),
                       pygame.image.load("PNG/backgrounds/h6.png")
                       ]
        self.image = self.coinImages[lives]
        self.rect = self.image.get_rect(center=[975,100])
        
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        coins = args[4]
        
        
        if coins > 0:
            coins = 0
        self.image = self.coinImages[lives+1]
        

        pass

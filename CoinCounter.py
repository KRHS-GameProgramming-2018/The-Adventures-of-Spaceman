import pygame, sys, math


#HealthBar and Power Ups 
class CoinCounter(pygame.sprite.Sprite):
    def __init__(self, size, bullets, coins, image):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.coinImages = [pygame.image.load("PNG/Power-ups/goldCoin.png")
                       
                       ]
        self.image = self.coinImages[coins]
        self.rect = self.image.get_rect(center=[975,100])
        
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        coins = args[5]
        print coins
        
        
        if (coins) < 0:
            coins = 0
        self.image = self.coinImages[coins]
        

        pass

import pygame, sys, math


#HealthBar and Power Ups 
class CoinCounter(pygame.sprite.Sprite):
    
        
    def __init__(self,  coins=0, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.coin = coins
        self.font = pygame.font.Font("8-Bit Madness.ttf", 48)
        # ~ self.shellImage = pygame.image.load("PNG/Power-ups/c0.png")
        # ~ self.shellRect = self.image.get_rect(center = [980, 150])
        self.image = self.font.render(str(self.coin), True, (255,255,255))
        self.rect = self.image.get_rect(center = pos)
        
    def update(*args):
        self = args[0]
        coins = args[5]
        self.coin = coins
        self.image = self.font.render(str(self.coin), True, (255,255,255))
        self.rect = self.image.get_rect(center = self.rect.center)
      
        
        
    

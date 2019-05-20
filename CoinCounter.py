import pygame, sys, math


#HealthBar and Power Ups 
class CoinCounter(pygame.sprite.Sprite):
    # ~ def __init__(self, size, bullets, coins, image):
        # ~ self.coinImages = [pygame.image.load("PNG/Power-ups/c0.png"),
                           # ~ pygame.image.load("PNG/Power-ups/c1.png"),
                           # ~ pygame.image.load("PNG/Power-ups/c2.png"),
                           # ~ pygame.image.load("PNG/Power-ups/c3.png"),
                           # ~ pygame.image.load("PNG/Power-ups/c4.png"),
                           # ~ pygame.image.load("PNG/Power-ups/c5.png"),
                       # ~ ]
        # ~ self.image = self.coinImages[coins]
        # ~ self.rect = self.image.get_rect(center=[978,165])
        
        
        
    # ~ def update(*args):
        # ~ self = args[0]
        # ~ size = args[1]
        # ~ coins = args[5]
        # ~ print coins
        
        
        # ~ if (coins) < 0:
            # ~ coins = 0
        # ~ self.image = self.coinImages[coins]
        
    def __init__(self,  coins=0, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.coin = coins
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(str(self.coin), True, (255,255,255))
        self.rect = self.image.get_rect(center = pos)
        
    def update(*args):
        self = args[0]
        coins = args[1]
        pos = args[2]
        # ~ self.score = newScore
        # ~ self.image = self.font.render(str(self.score), True, (255,255,255))
        # ~ self.rect = self.image.get_rect(center = self.rect.center)
        
        
    

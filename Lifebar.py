import pygame, sys, math


#HealthBar and Power Ups 
class Lifebar(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives, image):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.healthImages = [pygame.image.load("PNG/backgrounds/spacemansheart.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart2.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart3.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart4.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart5.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart6.png")
                       ]
        self.image = self.healthImages[lives]
        self.rect = self.image.get_rect(center=[975,500])
        
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        # ~ bullets = args[4]
        
        if lives > 6:
            lives = 6
        self.image = self.healthImages[lives-1]
        

        pass

import pygame, sys, math


#HealthBar and Power Ups 
class GameDisplay(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.image.load("PNG/backgrounds/spacemansheart.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart2.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart3.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart4.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart5.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart6.png")
                       ]
        self.image = self.images[lives]
        self.rect = self.image.get_rect(center=[175,775])
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        bullets = args[4]
        
        if lives > 6:
            lives = 6
        self.image = self.images[lives-1]

        pass

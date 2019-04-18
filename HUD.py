import pygame, sys, math


#HealthBar and Power Ups 
class GameDisplay(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives):
        self.images = [pygame.image.load("PNG/backgrounds/spacemansheart.png"),([175,975]),
                       pygame.image.load("PNG/backgrounds/spacemansheart2.png"),([175,975]),
                       pygame.image.load("PNG/backgrounds/spacemansheart3.png"),([175,975]),
                       pygame.image.load("PNG/backgrounds/spacemansheart4.png"),([175,975]),
                       pygame.image.load("PNG/backgrounds/spacemansheart5.png"),([175,975]),
                       pygame.image.load("PNG/backgrounds/spacemansheart6.png"),([175,975])]
        self.image = self.images[lives]
        self.rect = self.image.get_rect(center=(175,975))
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        bullets = args[4]
        
        self.image = self.images[health]
        self.rect = self.image.get_rect()
        pass

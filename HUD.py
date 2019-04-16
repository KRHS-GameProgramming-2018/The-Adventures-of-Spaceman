import pygame, sys, math


#HealthBar and Power Ups 
class GameDisplay(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives):
        self.rect = self.image.get_rect()
        self.images = [pygame.image.load("background/spacemansheart.png"),([175,975]),
                       pygame.image.load("background/spacemansheart.png"),([175,975]),
                       pygame.image.load("background/spacemansheart.png"),([175,975]),
                       pygame.image.load("background/spacemansheart.png"),([175,975]),
                       pygame.image.load("background/spacemansheart.png"),([175,975]),
                       pygame.image.load("background/spacemansheart.png"),([175,975])]
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        bullets = args[4]
        self.image = self.images[health]
        pass

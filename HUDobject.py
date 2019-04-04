import pygame, sys, math

#HealthBar and Power Ups 
class GameDisplayObject(pygame.sprite.Sprite):
        def __init__(self, image, pos):
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()

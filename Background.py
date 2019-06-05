import pygame, sys, math

class Background(pygame.sprite.Sprite):
    def __init__(self,  image, pos = [500, 400]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = pos)
        self.layer = 0
        self.name = image

    def update(*args):
        pass

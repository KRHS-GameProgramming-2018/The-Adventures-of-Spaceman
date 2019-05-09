import pygame, sys, math

class ShopItem(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if kind == "health":
            self.basicImage = pygame.image.load("PNG/Buttons/healthShop.png")
            self.hoverImage = pygame.image.load("PNG/Buttons/healthShop-selected.png")
        self.image = self.basicImage
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

    def stopSelect(self):
        self.image = self.basicImage
        
    def doSelect(self):
        self.image = self.hoverImage

    def update(*args):
        pass

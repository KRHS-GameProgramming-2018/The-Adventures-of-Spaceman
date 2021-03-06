import pygame, sys, math

class ShopItem(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if kind == "healthUp":
            self.basicImage = pygame.image.load("PNG/Buttons/healthShop.png")
            self.hoverImage = pygame.image.load("PNG/Buttons/healthShop-selected.png")
            self.kind = "healthUp"
        if kind == "mag":
            self.basicImage = pygame.image.load("PNG/Buttons/magShop.png")
            self.hoverImage = pygame.image.load("PNG/Buttons/magShop-selected.png")
            self.kind = "mag"
        if kind == "health plus":
            self.basicImage = pygame.image.load("PNG/Buttons/healthBoostShop.png")
            self.hoverImage = pygame.image.load("PNG/Buttons/healthBoostShop-selected.png")
            self.kind = "health plus"
        
        if kind == "purchased":
            self.basicImage = pygame.image.load("PNG/Buttons/purchased.png")
            self.hoverImage = pygame.image.load("PNG/Buttons/purchased.png")
            self.kind = "empty"
            
        self.image = self.basicImage
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

    def stopSelect(self):
        self.image = self.basicImage
        
    def doSelect(self):
        self.image = self.hoverImage

    def update(*args):
        pass

import pygame, sys, math

class ShopItem(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if kind == "start":
            self.basicImage = pygame.image.load("PNG/Buttons/controlButton.png")
            self.hoverImage = pygame.image.load("PNG/Buttons/controlHoverButton.png")
            self.clickImage = pygame.image.load("PNG/Buttons/controlClickButton.png")
        self.image = self.basicImage
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        
    def collidePt(self, pt):
        if self.rect.right > pt[0]:
            if self.rect.left < pt[0]:
                if self.rect.top < pt[1]:
                    if self.rect.bottom > pt[1]:
                        return True
        return False
        
    def checkHover(self, pt):
        if self.collidePt(pt):
            self.image = self.hoverImage
        else:
            self.image = self.basicImage
            
    def checkClick(self, pt):
        if self.collidePt(pt):
            self.image = self.clickImage
        else:
            self.image = self.basicImage

    def update(self, size):
        pass

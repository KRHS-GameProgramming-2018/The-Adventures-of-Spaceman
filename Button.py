import pygame, sys, math

class Button(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if kind == "start":
            self.basicImage = pygame.image.load("PNG/buttons/startButton.png")
            self.hoverImage = pygame.image.load("PNG/buttons/startHover.png")
            self.clickImage = pygame.image.load("PNG/buttons/StartClick.png")
        if kind == "controls":
            self.basicImage = pygame.image.load("PNG/buttons/controlsButton.png")
            self.hoverImage = pygame.image.load("PNG/buttons/controlsHover.png")
            self.clickImage = pygame.image.load("PNG/buttons/controlsClick.png")
        if kind == "levels":
            self.basicImage = pygame.image.load("PNG/buttons/quitButton.png")
            self.hoverImage = pygame.image.load("PNG/buttons/quitButton.png")
            self.clickImage = pygame.image.load("PNG/buttons/quitButton.png")
        if kind == "quit":
            self.basicImage = pygame.image.load("PNG/buttons/quitButton.png")
            self.hoverImage = pygame.image.load("PNG/buttons/quitHover.png")
            self.clickImage = pygame.image.load("PNG/buttons/quitClick.png")
        if kind == "useless":
            self.basicImage = pygame.image.load("PNG/buttons/quitButton.png")
            self.hoverImage = pygame.image.load("PNG/buttons/quitHover.png")
            self.clickImage = pygame.image.load("PNG/buttons/quitClick.png")
        
            
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

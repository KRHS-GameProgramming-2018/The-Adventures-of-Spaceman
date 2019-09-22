import pygame, sys, math


#HealthBar and Power Ups 
class Lifebar(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives, image):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.healthImages = [pygame.image.load("PNG/backgrounds/h1.png"),
                       pygame.image.load("PNG/backgrounds/h2.png"),
                       pygame.image.load("PNG/backgrounds/h3.png"),
                       pygame.image.load("PNG/backgrounds/h4.png"),
                       pygame.image.load("PNG/backgrounds/h5.png"),
                       pygame.image.load("PNG/backgrounds/h6.png"),
                       pygame.image.load("PNG/backgrounds/h7.png"),
                       pygame.image.load("PNG/backgrounds/h8.png")]
                       
                       
        self.image = self.healthImages[lives]
        self.rect = self.image.get_rect(center=[979,460])
        
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        
        if lives > 8:
            lives = 8
        if lives < 0:
            print "lives:" + str(lives)
            lives = 0
        self.image = self.healthImages[lives-1]
        

        pass

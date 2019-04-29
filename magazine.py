import pygame, sys, math


#HealthBar and Power Ups 
class magazine(pygame.sprite.Sprite):
    def __init__(self, bullets, lives, init):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.images = [pygame.image.load("PNG/Bolt/bulletmag0.png"),
                             pygame.image.load("PNG/Bolt/bulletmag1.png"),
                             pygame.image.load("PNG/Bolt/bulletmag2.png"),
                             pygame.image.load("PNG/Bolt/bulletmag3.png"),
                             pygame.image.load("PNG/Bolt/bulletmag4.png"),
                             pygame.image.load("PNG/Bolt/bulletmag5.png"),
                             pygame.image.load("PNG/Bolt/bulletmag6.png"),
                             pygame.image.load("PNG/Bolt/bulletmag7.png"),
                             pygame.image.load("PNG/Bolt/bulletmag8.png"),
                             pygame.image.load("PNG/Bolt/bulletmag9.png"),
                             pygame.image.load("PNG/Bolt/bulletmag10.png"),
                             pygame.image.load("PNG/Bolt/bulletmag11.png"),
                             pygame.image.load("PNG/Bolt/bulletmag12.png"),
                             pygame.image.load("PNG/Bolt/bulletmag13.png"),
                             pygame.image.load("PNG/Bolt/bulletmag14.png"),
                             pygame.image.load("PNG/Bolt/bulletmag15.png"),
                             pygame.image.load("PNG/Bolt/bulletmag16.png"),
                             pygame.image.load("PNG/Bolt/bulletmag17.png"),
                             pygame.image.load("PNG/Bolt/bulletmag18.png"),
                             pygame.image.load("PNG/Bolt/bulletmag19.png"),
                             pygame.image.load("PNG/Bolt/bulletmag20.png")]
        self.image = self.images[bullets - 1]
        self.rect = self.image.get_rect(center=[770,265])
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        bullets = args[4]
        

        pass


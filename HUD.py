import pygame, sys, math


#HealthBar and Power Ups 
class GameDisplay(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.HealthImages = [pygame.image.load("PNG/backgrounds/spacemansheart.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart2.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart3.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart4.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart5.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart6.png")
                       ]
        self.HealthImage = self.HealthImages[lives]
        self.Healthrect = self.image.get_rect(center=[175,775])
        
        self.BulletImage = [pygame.image.load("PNG/Bolt/bulletmag"+str(bullets)+".png")]
       # self.BulletImage = self.BulletImages[bullets - 1]
        self.Bulletrect = self.image.get_rect(center=[770,265])
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        bullets = args[4]
        
        if lives > 6:
            lives = 6
        self.HealthImage = self.HealthImages[lives-1]
        if bullets > 20:
            bullets = 20
       # self.BulletImage = self.BulletImages[bullets-1]

        pass

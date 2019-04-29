import pygame, sys, math


#HealthBar and Power Ups 
class Lifebar(pygame.sprite.Sprite):
    def __init__(self, size, bullets, lives, image1, image2):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.healthImages = [pygame.image.load("PNG/backgrounds/spacemansheart.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart2.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart3.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart4.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart5.png"),
                       pygame.image.load("PNG/backgrounds/spacemansheart6.png")
                       ]
        self.healthImage = self.healthImages[lives]
        self.healthrect = self.healthImage.get_rect(center=[175,775])
        
        self.BulletImages = [pygame.image.load("PNG/Bolt/bulletmag20.png"),
                            pygame.image.load("PNG/Bolt/bulletmag19.png"),
                            pygame.image.load("PNG/Bolt/bulletmag18.png"),
                            pygame.image.load("PNG/Bolt/bulletmag17.png"),
                            pygame.image.load("PNG/Bolt/bulletmag16.png"),
                            pygame.image.load("PNG/Bolt/bulletmag15.png"),
                            pygame.image.load("PNG/Bolt/bulletmag14.png"),
                            pygame.image.load("PNG/Bolt/bulletmag13.png"),
                            pygame.image.load("PNG/Bolt/bulletmag12.png"),
                            pygame.image.load("PNG/Bolt/bulletmag11.png"),
                            pygame.image.load("PNG/Bolt/bulletmag10.png"),
                            pygame.image.load("PNG/Bolt/bulletmag9.png"),
                            pygame.image.load("PNG/Bolt/bulletmag8.png"),
                            pygame.image.load("PNG/Bolt/bulletmag7.png"),
                            pygame.image.load("PNG/Bolt/bulletmag6.png"),
                            pygame.image.load("PNG/Bolt/bulletmag5.png"),
                            pygame.image.load("PNG/Bolt/bulletmag4.png"),
                            pygame.image.load("PNG/Bolt/bulletmag3.png"),
                            pygame.image.load("PNG/Bolt/bulletmag2.png"),
                            pygame.image.load("PNG/Bolt/bulletmag1.png"),
                            pygame.image.load("PNG/Bolt/bulletmag0.png"),
                            ]
       # self.BulletImage = self.BulletImages[bullets - 1]
        self.BulletImage = self.BulletImages[bullets]
        self.Bulletrect = self.BulletImage.get_rect(center=[770,265])
        
        
    def update(*args):
        self = args[0]
        size = args[1]
        lives = args[3]
        bullets = args[4]
        
        if lives > 6:
            lives = 6
        self.healthImage = self.healthImages[lives-1]
        
        if bullets > 20:
            lives = 20
        self.BulletImage = self.BulletImages[bullets-1]

        pass

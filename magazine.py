import pygame, sys, math


#HealthBar and Power Ups 
class magazine(pygame.sprite.Sprite):
    def __init__(self, size, bullets, image):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.bulletImages = [pygame.image.load("PNG/Bolt/bulletmag0.png"),
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
                             pygame.image.load("PNG/Bolt/bulletmag20.png"),
                             pygame.image.load("PNG/Bolt/bulletmag21.png"),
                             pygame.image.load("PNG/Bolt/bulletmag22.png"),
                             pygame.image.load("PNG/Bolt/bulletmag23.png"),
                             pygame.image.load("PNG/Bolt/bulletmag24.png"),
                             pygame.image.load("PNG/Bolt/bulletmag25.png"),
                             pygame.image.load("PNG/Bolt/bulletmag26.png"),
                             pygame.image.load("PNG/Bolt/bulletmag27.png"),
                             pygame.image.load("PNG/Bolt/bulletmag28.png"),
                             pygame.image.load("PNG/Bolt/bulletmag29.png"),
                             pygame.image.load("PNG/Bolt/bulletmag30.png"),
                             pygame.image.load("PNG/Bolt/bulletmag31.png"),
                             pygame.image.load("PNG/Bolt/bulletmag32.png"),
                             pygame.image.load("PNG/Bolt/bulletmag33.png"),
                             pygame.image.load("PNG/Bolt/bulletmag34.png"),
                             pygame.image.load("PNG/Bolt/bulletmag35.png"),
                             pygame.image.load("PNG/Bolt/bulletmag36.png"),
                             pygame.image.load("PNG/Bolt/bulletmag37.png"),
                             pygame.image.load("PNG/Bolt/bulletmag38.png"),
                             pygame.image.load("PNG/Bolt/bulletmag39.png"),
                             pygame.image.load("PNG/Bolt/bulletmag40.png"),]
        self.image = self.bulletImages[bullets]
        self.rect = self.image.get_rect(center=[975,265])
   
        
    def update(*args):
        self = args[0]
        size = args[1]
        bullets = args[4]
        

        if bullets > 40:
            bullets = 40
        self.image = self.bulletImages[bullets-1]
       
        
        if bullets <= 0:
            self.image = self.bulletImages[0]
        
        pass


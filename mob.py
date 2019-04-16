import pygame, sys, math


class Mob(pygame.sprite.Sprite):
    def __init__(self, image, speed=[5,5], startPos=[0,0], power=[]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #print image
        self.image = pygame.image.load(image)
        self.alive = True
        self.rect = self.image.get_rect(center = startPos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        #self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
        
        #for animation
        self.images = [self.image]
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/20
        
    def live(self, lives):
        if self.lives <= 0:
            self.kill()
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
    def animate(self):
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
            
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
                
            self.image = self.images[self.frame]
            
    def update(*args):
        self = args[0]
        size = args[1]
        pCenter = args[2]
        # ~ print self.rect.center
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
        self.animate()
        self.live(self.lives)
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True
            
    def bounceBlock(self, other):
        if other.kind == "block":
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True
            return True
        return False
            
    def collide(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.didBounceX = True
        self.speedy = 0
        self.didBounceY = True
        
        return True


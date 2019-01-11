import pygame, sys, math, random
from mob import *

class SpaceZombie(Mob):
    def __init__(self, speed=1, startPos=[0,0]):
        Mob.__init__(self, "PNG/Enemy2/Imposter-Down.png", [0,0], startPos)
        self.rightImages = [pygame.image.load("PNG/Enemy2/Imposter-Right1.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Right2.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Right3.png"),
                        ]
        self.leftImages = [pygame.image.load("PNG/Enemy2/Imposter-Left1.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Left2.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Left3.png"),
                        ]
        self.upImages = [pygame.image.load("PNG/Enemy2/Imposter-Up.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Up.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Up.png"),
                        ]
        self.downImages = [pygame.image.load("PNG/Enemy2/Imposter-Down.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Down.png"),
                        pygame.image.load("PNG/Enemy2/Imposter-Down.png"),
                        ]

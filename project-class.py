import pygame
import random

class Target:
    def __init__(self):
        self.x = random.randit(0, 600)
        self.y = random.randit(0, 600)
        self.score = 10
    
    def show(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 20)
    
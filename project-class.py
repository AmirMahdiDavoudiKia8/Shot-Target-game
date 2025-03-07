import pygame
import random

class Target:
    def __init__(self):
        self.x = random.randit(0, 88) * 10
        self.y = random.randit(0, 58) * 10
        self.score = 10
    
    def show(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y), 40,40)
    
    
class Item:
    class ExtraAmmo(Target):
        def __init__(self):
            super().__init__()
            self.score =0 
            self.ammo_bonus= 5
        def show(self, screen):
            pygame.draw.rect(screen, (50, 150, 0), (self.x -20, self.y -10, 50, 20))
            pygame.draw.line(screen, (50, 200, 0), (self.x +20, self.y), (self.x +20, self.y), 7)
            

    class SlowEnemy(Target):
        def __init__(self):
            super().__init__()
            self.score = 5
            self.slow = 5
        def show(self, screen):
            pygame.draw.polygon(screen, (200, 0, 200), [
                (self.x, self.y-30),
                (self.x +30, self.y),
                (self.x, self.y-30),
                (self.x-30 , self.y)
            ])
        
    class ExtraTime(Target):
        def __init__(self):
            super().__init__()
            self.time_bonus= 10
            self.score = 0
        
        def show(self, screen):
            pygame.draw.circle(screen, (0, 45, 225), (self.x, self.y), 30)
            pygame.draw.line(screen, (self.x, self.y), (self.x+15 , self.y-15), 2)
            pygame.draw.line(screen, (self.s , self.y), (self.x , self.y+25), 2)
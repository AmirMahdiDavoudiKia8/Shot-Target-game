import random
import pygame

pygame.init()

class Pleyer:

    def __init__(self, name, score=0, time=300, Ammo=20):
        self.name = name
        self.score = score
        self.time = time
        self.Ammo = Ammo
        self.pos_x = random.randint(1, 90) * 10
        self.pos_y = random.randint(1, 60) * 10

    def move_up(self):
        self.pos_y += 10
        if self.pos_y > 600 :
            self.pos_y - 600

    def move_down(self):
        self.pos_y -= 10
        if self.pos_y < 0 :
            self.pos_y + 600

    def move_right(self):
        self.pos_x += 10
        if self.pos_x > 900 :
            self.pos_x -= 900

    def move_left(self):
        self.pos_x -= 10
        if self.pos_x < 0 :
            self.pos_x += 900


    def shoot(self, player):
        if self.Ammo > 0 :
            self.Ammo -= 1
            

    def hit(self, target):
        targets = []
        for i in range(3):
            targets.append(Target())
        for t in targets[:]:
                if target.x - 20 < self.pos_x < target.x + 20 and target.y - 20 < self.pos_y < target.y + 20 :
                    targets.remove(t) 
                    targets.append(Target())

            
class Target:
    def __init__(self):
        self.x = random.randint(0, 88) * 10
        self.y = random.randint(0, 58) * 10
        self.score = 10
    
    def show(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y ,20, 20))
    
    
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
                (self.x, self.y-20),
                (self.x +20, self.y),
                (self.x, self.y-20),
                (self.x-20 , self.y)
            ])
        
    class ExtraTime(Target):
        def __init__(self):
            super().__init__()
            self.time_bonus= 10
            self.score = 0
        
        def show(self, screen):
            pygame.draw.circle(screen, (0, 45, 225), (self.x, self.y), 20)
            pygame.draw.line(screen, (self.x, self.y), (self.x+15 , self.y-15), 2)
            pygame.draw.line(screen, (self.x , self.y), (self.x , self.y+25), 2)
            

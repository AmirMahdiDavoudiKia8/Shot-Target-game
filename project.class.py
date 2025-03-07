import pygame,sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import random


pygame.init()
window=pygame.display.set_mode((900, 600))
window.fill((10, 18, 18))
pygame.display.set_caption('Shot-Target')

while True:
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


class pleyer:

    def __init__(self, name, score=0, time=300, Ammo=20):
        self.name = name
        self.score = score
        self.time = time
        self.Ammo = Ammo
        self.pos_x = random.randiat(1, 90) * 10
        self.pos_y = random.randiat(1, 60) * 10

    def move_up(self):
        self.pos_y += 10
        if self.pos_y > 600 :
            self.pos_y - 600

    def move_done(self):
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



    def Hit(self, target):
        if target.x - 20 < self.pos_x < target.x + 20 and target.y - 20 < self.pos_y < target.y + 20 :
            target.rest()




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
            pygame.draw.rect(screen, (50, 150, 0), (self.x -20, self.y -10, 30, 10))
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
            pygame.draw.circle(screen, (0, 45, 225), (self.x, self.y), 10)
            pygame.draw.line(screen, (self.x, self.y), (self.x+5 , self.y-5), 2)
            pygame.draw.line(screen, (self.s , self.y), (self.x , self.y+8), 2)





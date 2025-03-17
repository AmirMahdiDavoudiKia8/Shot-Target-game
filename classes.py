import random
import pygame
import math

pygame.init()
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound("media/shoot.wav")

class ScoreSystem:
    def __init__(self):
        self.consecutive_hits = 0
        
    def calculate_score(self, player_x, player_y, target_x, target_y):
        distance = math.sqrt((player_x - target_x) **2 + (player_y - target_y) ** 2)
        if distance < 100:
            base_score =1 
        elif distance <200:
            base_score= 2
        elif distance< 300:
            base_score= 3
        elif distance< 400:
            base_score= 4
        else:
            base_score= 5 
        bonus_score =0
        self.consecutive_hits += 1
        if self.consecutive_hits >= 2:
            bonus_score = 3 
            self.consecutive_hits = 0
        return base_score+ bonus_score
    
    def reset_consecutive(self):
        self.consecutive_hits = 0
                     
class Player:

    def __init__(self, name, score=0, time=180, Ammo=20):
        self.name = name
        self.score = score
        self.time = time
        self.Ammo = Ammo
        self.pos_x = random.randint(1, 90) * 10
        self.pos_y = random.randint(8, 68) * 10
        self.last_shot_pos = None 
        self.score_system = ScoreSystem()
        self.timer_started = False

    def move_up(self):
        self.pos_y -= 10
        if self.pos_y <= 80:
            self.pos_y += 600

    def move_down(self):
        self.pos_y += 10
        if self.pos_y >= 680:
            self.pos_y -= 600


    def move_right(self):
        self.pos_x += 10
        if self.pos_x > 900 :
            self.pos_x -= 900

    def move_left(self):
        self.pos_x -= 10
        if self.pos_x < 0 :
            self.pos_x += 900


    def shoot(self, player, targets, screen):
        if self.Ammo > 0:
            self.Ammo -= 1
            self.last_shot_pos = (self.pos_x, self.pos_y)
            shoot_sound.play()
            if not self.timer_started:
                self.timer_started = True
            self.show_Crosshair(screen)
            self.hit(player, targets)


    def show_Crosshair(self, screen):
    
        if self.last_shot_pos:
            x, y = self.last_shot_pos
            pygame.draw.rect(screen, (255, 0, 0), (x - 5, y - 5, 10, 10))
            pygame.draw.circle(screen, (0, 0, 0), (x, y), 3)


    def hit(self, opponent, targets):
        if not self.last_shot_pos:
            return False

        shot_x, shot_y = self.last_shot_pos 
    
        for t in targets[:]:

            if t.x  < shot_x <= t.x + 40  and t.y  <= shot_y < t.y + 40:
                print(f"Hit target at {t.x}, {t.y}")
                targets.remove(t)

                if isinstance(t, ExtraTime):
                    self.time += 30
                    targets.append(ExtraTime())
                    self.score_system.reset_consecutive()

                elif isinstance(t, ExtraAmmo):
                    self.Ammo += 5
                    targets.append(ExtraAmmo())
                    self.score_system.reset_consecutive()

                elif isinstance(t, loseAmmo):
                    if opponent.Ammo > 0:
                        opponent.Ammo -= 2
                    targets.append(loseAmmo())
                    self.score_system.reset_consecutive()

                else:
                    score = self.score_system.calculate_score(self.pos_x, self.pos_y, t.x, t.y)
                    self.score += score
                    targets.append(Target())
                return True
        self.score_system.reset_consecutive()
            
            
class Target:
    def __init__(self):
        self.x = random.randint(0, 88) * 10
        self.y = random.randint(10, 58) * 10
        self.score = 10
        self.image = pygame.image.load("media/target.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
    
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    

class ExtraAmmo(Target):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/ammo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

class loseAmmo(Target):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/decrease.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class ExtraTime(Target):
    def __init__(self):    
        super().__init__()
        self.image = pygame.image.load("media/clock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
pygame.init()
import random
import pygame,sys
from costom import *

pygame.init()



class Player:

    def __init__(self, name, score=0, time=60, Ammo=20):
        self.name = name
        self.score = score
        self.time = time
        self.Ammo = Ammo
        self.pos_x = random.randint(1, 90) * 10
        self.pos_y = random.randint(1, 60) * 10
        self.last_shot_pos = None 

    def move_up(self):
        self.pos_y -= 10
        if self.pos_y < 80:
            self.pos_y = 600

    def move_down(self):
        self.pos_y += 10
        if self.pos_y > 600:
            self.pos_y = 80


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
            self.show_Crosshair(screen)
            self.hit(player, targets)

    def show_Crosshair(self, screen):
    
        if self.last_shot_pos:
            x, y = self.last_shot_pos
            pygame.draw.rect(screen, (255, 0, 0), (x - 5, y - 5, 10, 10))
            pygame.draw.circle(screen, (0, 0, 0), (x, y), 3)


    def hit(self, opponent, targets):
        for t in targets[:]:
<<<<<<< HEAD
                if target.x - 20 < self.pos_x < target.x + 20 and target.y - 20 < self.pos_y < target.y + 20 :
                    targets.remove(t) 
                    targets.append(Target())
=======
            if t.x - 20 < self.pos_x < t.x + 20 and t.y - 20 < self.pos_y < t.y + 20:
                print(f"Hit target at {t.x}, {t.y}")  # نمایش لاگ برای تست
                targets.remove(t)
>>>>>>> ea3e7105e17aee6ad6a236e656765cc305dfa528

                if isinstance(t, ExtraTime):
                    self.time += 10
                    targets.append(ExtraTime())

                elif isinstance(t, ExtraAmmo):
                    self.Ammo += 5
                    targets.append(ExtraAmmo())

                elif isinstance(t, lowAmmo):
                    opponent.Ammo -= 2
                    targets.append(lowAmmo())

                else:
                    self.score += 10
                    targets.append(Target())
                return True
                               
            
class Target:
    def __init__(self):
        self.x = random.randint(0, 88) * 10
        self.y = random.randint(0, 58) * 10
        self.score = 10
    
    def show(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y ,20, 20))
    
    

class ExtraAmmo(Target):
    def __init__(self):
        super().__init__()
    def show(self, screen):
        pygame.draw.rect(screen, (50, 150, 0), (self.x -20, self.y -10, 50, 20))
        pygame.draw.line(screen, (50, 200, 0), (self.x +20, self.y), (self.x +20, self.y), 7)       

class lowAmmo(Target):
    def __init__(self):
        super().__init__()
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
        
    def show(self, screen):
        pygame.draw.circle(screen, (0, 45, 225), (self.x, self.y), 20)
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x+15 , self.y-15), 2)
        pygame.draw.line(screen, WHITE, (self.x , self.y), (self.x , self.y+25), 2)



pygame.init()



def draw_text(text, pos, font, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def show_welcome_screen():
    draw_text("welcome to game!", (200, 100), font_l, RED)
    draw_text("Press the key to start the game ...", (350, 200), font_s, 'green')
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

    
def draw_header(player1, score1, time1, Ammo1, player2, score2, time2, Ammo2):
    pygame.draw.rect(screen, fever, (0, 0, WIDTH, HEADER_HEIGHT))  
    pygame.draw.line(screen, WHITE, (0, HEADER_HEIGHT), (WIDTH, HEADER_HEIGHT), 3)
    
    draw_text(f"{player1}", (WIDTH - 300, 30), font_s1)
    draw_text(f"score: {score1}  | time:  {time1}s  |  Ammo:  {Ammo1}", (WIDTH - 300, 50), font_s1)
    draw_text(f"{player2}", (20, 30), font_s1)
    draw_text(f"score: {score2}  | time:  {time2}s  |  Ammo:  {Ammo2}", (20, 50), font_s1)



def get_player_names():
    player1 = ""
    player2 = ""
    active_player = 1
    running = True
    
    while running:
        screen.fill(BLACK)
        draw_text("Player One, please enter your name:", (50, 50), font_2, GRAY)
        draw_text(player1, (50, 100), font, RED)
        draw_text("Player Two, please enter your name:", (50, 250), font_2, GRAY)
        draw_text(player2, (50, 300), font, RED)
        draw_text("Press Enter to confirm ...", (50, 550), font_s, 'green')
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None, None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if active_player == 1 and player1:
                        active_player = 2
                    elif active_player == 2 and player2:
                        return player1, player2
                elif event.key == pygame.K_BACKSPACE:
                    if active_player == 1:
                        player1 = player1[:-1]
                    else:
                        player2 = player2[:-1]
                else:
                    if active_player == 1:
                        player1 += event.unicode
                    else:
                        player2 += event.unicode

show_welcome_screen()


player1_name, player2_name = get_player_names() 
if not player1_name or not player2_name:
    pygame.quit()
    sys.exit()




player1 = Player(player1_name)
player2 = Player(player2_name)

Target1 = Target()
Target2 = Target()
Target3 = Target()
item1 = ExtraAmmo()
item2 = ExtraTime()
item3 = lowAmmo()

Targets = [Target1, Target2, Target3, item1, item2, item3]

num_shoot1 = 0
num_shoot2 = 0

running = True
while running:
    screen.fill(GRAY)
    draw_header(player1.name, player1.score, player1.time, player1.Ammo, player2.name, player2.score, player2.time, player2.Ammo)
    pygame.draw.rect(screen, BLACK, (0, HEADER_HEIGHT, GAME_WIDTH, GAME_HEIGHT), 0)
    for target in Targets:
        target.show(screen)

    if num_shoot1 > 0:
        player1.show_Crosshair(screen)

    if num_shoot2 > 0:
        player2.show_Crosshair(screen)

    
    pygame.display.flip()
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                player1.shoot(player2, Targets, screen)
                num_shoot1 += 1
                for target in Targets:
                    target.show(screen)

                    pygame.display.flip()


            if event.key == pygame.K_w:
                player1.move_up()

            if event.key == pygame.K_a:
                player1.move_left()

            if event.key == pygame.K_d:
                player1.move_right()

            if event.key == pygame.K_s:
                player1.move_down()


            if event.key == pygame.K_KP7:
                player2.shoot(player1, Targets, screen)
                num_shoot2 += 1
                for target in Targets:
                    target.show(screen)

                    pygame.display.flip()


            if event.key == pygame.K_KP8:
                player2.move_up()

            if event.key == pygame.K_KP4:
                player2.move_left()

            if event.key == pygame.K_KP6:
                player2.move_right()

            if event.key == pygame.K_KP5:
                player2.move_down()

            

<<<<<<< HEAD
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
            
=======

>>>>>>> ea3e7105e17aee6ad6a236e656765cc305dfa528

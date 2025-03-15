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
        for t in targets:
            if t.x - 20 < self.pos_x < t.x + 20 and t.y - 20 < self.pos_y < t.y + 20:
                targets.remove(t)
                targets.append(Target())
                if isinstance(t, ExtraTime):
                    self.time += 10
                elif isinstance(t, ExtraAmmo):
                    self.Ammo += 5
                elif isinstance(t, lowAmmo):
                    opponent.Ammo -= 2
                else:
                    self.score += 10
                return True
                               
            
class Target:
    def __init__(self):
        self.x = random.randint(0, 88) * 10
        self.y = random.randint(0, 58) * 10
        self.score = 10
    
    def show(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y ,40,40))
    
    

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
        pygame.draw.line(screen, (self.x, self.y), (self.x+15 , self.y-15), 2)
        pygame.draw.line(screen, (self.x , self.y), (self.x , self.y+25), 2)



pygame.init()



def draw_text(text, pos, font, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def show_welcome_screen():
    screen
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


running = True
while running:
    screen.fill(GRAY)
    draw_header(player1.name, player1.score, player1.time, player1.Ammo, player2.name, player2.score, player2.time, player2.Ammo)
    pygame.draw.rect(screen, BLACK, (0, HEADER_HEIGHT, GAME_WIDTH, GAME_HEIGHT), 0)

    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

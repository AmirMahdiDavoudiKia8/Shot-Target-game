import random
import pygame,sys
from custom import *
import math
import cv2

pygame.init()
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound("shoot.wav")

cap = cv2.VideoCapture("background.mp4") 
if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()

def get_frame():
    ret, frame = cap.read()
    if not ret: 
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (GAME_WIDTH, GAME_HEIGHT))
        return pygame.surfarray.make_surface(frame.transpose((1, 0, 2)))
    return None

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

    def __init__(self, name, score=0, time=60, Ammo=20):
        self.name = name
        self.score = score
        self.time = time
        self.Ammo = Ammo
        self.pos_x = random.randint(1, 90) * 10
        self.pos_y = random.randint(1, 60) * 10
        self.last_shot_pos = None 
        self.score_system = ScoreSystem()

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
            shoot_sound.play()
            self.show_Crosshair(screen)
            self.hit(player, targets)

    def show_Crosshair(self, screen):
    
        if self.last_shot_pos:
            x, y = self.last_shot_pos
            pygame.draw.rect(screen, (255, 0, 0), (x - 5, y - 5, 10, 10))
            pygame.draw.circle(screen, (0, 0, 0), (x, y), 3)


    def hit(self, opponent, targets):
        for t in targets[:]:
            if t.x - 20 < self.pos_x < t.x + 20 and t.y - 20 < self.pos_y < t.y + 20:
                print(f"Hit target at {t.x}, {t.y}") 
                targets.remove(t)
                if isinstance(t, ExtraTime):
                    self.time += 10
                    targets.append(ExtraTime())
                    self.score_system.reset_consecutive()

                elif isinstance(t, ExtraAmmo):
                    self.Ammo += 5
                    targets.append(ExtraAmmo())
                    self.score_system.reset_consecutive()

                elif isinstance(t, loseAmmo):
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
        self.x = random.randint(4, 86) * 10
        self.y = random.randint(10, 58) * 10
        self.score = 10
        self.image = pygame.image.load("target.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
    
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    

class ExtraAmmo(Target):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ammo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

class loseAmmo(Target):
    def __init__(self):
        self.image = pygame.image.load("decrease.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        super().__init__()
        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class ExtraTime(Target):
    def __init__(self):    
        super().__init__()
        self.image = pygame.image.load("clock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))



pygame.init()



def draw_text(text, pos, font, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def show_welcome_screen():
    pygame.mixer.music.load("login.wav")
    draw_text("welcome to game!", (200, 100), font_l, RED)
    draw_text("Press the key to start the game ...", (350, 200), font_s, 'green')
    pygame.mixer.music.play(-1)
    
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
        screen.blit(get_frame(), (0, 0))
        draw_text("Player One, please enter your name:", (50, 50), font_2, BLACK)
        draw_text(player1, (50, 100), font, RED)
        draw_text("Player Two, please enter your name:", (50, 250), font_2, BLACK)
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

pygame.mixer.music.stop()
pygame.mixer.music.load("game.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)



player1 = Player(player1_name)
player2 = Player(player2_name)

Target1 = Target()
Target2 = Target()
Target3 = Target()
item1 = ExtraAmmo()
item2 = ExtraTime()
item3 = loseAmmo()

Targets = [Target1, Target2, Target3, item1, item2, item3]

num_shoot1 = 0
num_shoot2 = 0

running = True
while running:
    screen.blit(get_frame(), (0, 0))
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

cap.release()
pygame.quit()
            

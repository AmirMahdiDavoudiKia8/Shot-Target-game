import pygame,sys
from custom import *
from classes import *

pygame.init()
pygame.mixer.init()


def draw_text(text, pos, font, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def show_welcome_screen():
    pygame.mixer.music.load("media/login.wav")
    pygame.mixer.music.play(-1)
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


def show_winner_screen(winner):
    screen.fill((0, 0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.music.load("media/winer.mp3")
    pygame.mixer.music.play()

    if winner:
        draw_text(f"Winner", (280, 130), font_ll, 'gold')
        draw_text(f"{winer.name}", (350, 300), font_3, 'gold')
    else:
        draw_text("Draw!", (300, ), font_ll, 'gold')

    pygame.display.flip()
    pygame.time.delay(15000)





def draw_header(player1, score1, time1, Ammo1, player2, score2, time2, Ammo2):
    pygame.draw.rect(screen, fever, (0, 0, WIDTH, HEADER_HEIGHT))  
    pygame.draw.line(screen, WHITE, (0, HEADER_HEIGHT), (WIDTH, HEADER_HEIGHT), 3)
    
    draw_text(f"{player2}", (WIDTH - 300, 30), font_s1)
    draw_text(f"score: {score2}  | time:  {time2}s  |  Ammo:  {Ammo2}", (WIDTH - 300, 50), font_s1)
    draw_text(f"{player1}", (20, 30), font_s1)
    draw_text(f"score: {score1}  | time:  {time1}s  |  Ammo:  {Ammo1}", (20, 50), font_s1)



def get_player_names():
    player1 = ""
    player2 = ""
    active_player =1
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
pygame.mixer.music.load("media/game.wav")
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

last_time_update = pygame.time.get_ticks()

running = True
while running:
    screen.blit(background_image, (0, 0))
    draw_header(player1.name, player1.score, player1.time, player1.Ammo, player2.name, player2.score, player2.time, player2.Ammo)
    
    for target in Targets:
        target.show(screen)

    if num_shoot1 > 0:
        player1.show_Crosshair(screen)

    if num_shoot2 > 0:
        player2.show_Crosshair(screen)

    
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - last_time_update >= 1000:
        last_time_update = current_time

        if player1.timer_started and player1.time > 0:
            player1.time -= 1

        if player2.timer_started and player2.time > 0:
            player2.time -= 1


    if player1.time <= 0 and player2.time <= 0:
        running = False
        break

    if player1.Ammo <= 0 and player2.Ammo <= 0:
        running = False
        break

    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                if player1.time > 0:
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
                if player2.time > 0:
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




winer = None

if player1.score > player2.score :            
    winer = player1

elif player2.score > player1.score :
    winer = player2

show_winner_screen(winer)

cap.release()
pygame.quit()
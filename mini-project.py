import pygame,sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS


pygame.init()

""" 
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 36)

player1_name= ""
player2_name= ""
INPUT = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if INPUT == 1:
                    INPUT =2
                else:
                    INPUT=0
            elif event.key == pygame.K_BACKSPACE:
                if INPUT ==1:
                    player1_name = player1_name[:-1]
                elif INPUT==2:
                    player2_name = player2_name[:-1]
            else:
                if INPUT==1:
                    player1_name += event.unicode
                elif INPUT==2:
                    player2_name += event.unicode
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))

    label1 = font.render(f"Player 1:", True ,(255, 255, 255))
    label2 = font.render(f"Player 2:", True, (255, 255, 255))
    name1 = font.render(player1_name, True, (0, 0, 255))
    name2 = font.render(player2_name , True , (255, 0 ,0))

    screen.blit(label1, (50, 50))
    screen.blit(name1, (60 + label1.get_width(), 50))
    screen.blit(label2, (50, 100))
    screen.blit(name2, (60+ label2.get_width() , 100))

    pygame.display.flip()

print(f"Player 1: {player1_name}, Player 2: {player2_name}")
pygame.quit()

 """

window=pygame.display.set_mode((900, 600))
window.fill((10, 18, 18))
pygame.display.set_caption('Shot-Target')

while True:
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
import pygame,sys
pygame.init()



GAME_WIDTH, GAME_HEIGHT = 900, 600
HEADER_HEIGHT = 80 
WIDTH, HEIGHT = GAME_WIDTH, GAME_HEIGHT + HEADER_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHOT - TARGET")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
fever = (10, 18, 32)

font = pygame.font.Font(None, 36)
font_s = pygame.font.Font(None, 18)
font_s1 = pygame.font.Font(None, 22)
font_l = pygame.font.Font(None, 80)
font_1 = pygame.font.Font(None, 28)
font_2 = pygame.font.Font(None, 32)

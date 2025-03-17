import random
import pygame,sys
import cv2
import math
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


cap = cv2.VideoCapture("media/background.mp4")
if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()
    
def get_frame():
    ret, frame = cap.read()
    if not ret: 
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    frame = cv2.resize(frame, (GAME_WIDTH, GAME_HEIGHT)) 
    return pygame.surfarray.make_surface(frame.transpose((1, 0, 2)))

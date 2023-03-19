import pygame
import random
import sys



WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Solar_Storm_Logo.bmp
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40)

hex_1 = pygame.image.load('img/QueenWhite.png').convert_alpha()
hex_1_rect = hex_1.get_rect(bottomright=(100, 100))

hex_2 = pygame.image.load('img/Hex_2.png').convert_alpha()
hex_2_rect = hex_2.get_rect(bottomright=(200, 100))

hex_3 = pygame.image.load('img/Hex_3.png').convert_alpha()
hex_3_rect = hex_3.get_rect(bottomright=(300, 100))

hex_1_green = pygame.image.load('img/Hex_1_green.png').convert_alpha()
hex_1_rect_green = hex_1.get_rect(bottomright=(300, 100))

screen.fill(WHITE)



screen.blit(hex_1, hex_1_rect)
screen.blit(hex_2, hex_2_rect)
screen.blit(hex_3, hex_3_rect)
running = True
pygame.display.update()

while running:
    clock.tick(FPS)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen.fill(BLUE)
                print(event.pos)
                print("x = ", event.pos[0])
                if(event.pos[0] < 100, event.pos[1] < 100):
                    hex_1_rect_green = hex_1.get_rect(bottomright=(100, 100))
                    screen.blit(hex_1_green, hex_1_rect)
                    screen.blit(hex_2, hex_2_rect)
    
    pygame.display.update()

pygame.quit()
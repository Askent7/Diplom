from random import randint
import pygame
import sys
import os
import math
from player_hive import Player_Hive
from player_hive import Player_Hive_Beatle
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from model.state import State

state = State()
state.initial_state()
 
W = 1200
H = 1050
WHITE = (255, 255, 255)

class Hex(pygame.sprite.Sprite):
    def __init__(self, x_center, y_center, filename, mas):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x_center, y_center))
        self.mas = mas
        self.x_center = x_center
        self.y_center = y_center
    
screen = pygame.display.set_mode((W, H))

pi = 3.14159265358979323846;

a = 57

# queen_hex = pygame.image.load('img/QueenWhite.png').convert_alpha()
# queen_hex_rect = queen_hex.get_rect(bottomright=(100, 86))
# screen.blit(queen_hex, queen_hex_rect)
 

#50,43
# queen_white = Queen(100, 50)
hexs_group = pygame.sprite.Group()

group_hive_white = pygame.sprite.Group()
group_hive_white.add(Player_Hive(90, 70, "Queen", "img/QueenWhite.png"))
group_hive_white.add(Player_Hive(90, 160, "Grasshopper", "img/GrasshopperWhite.png"))
group_hive_white.add(Player_Hive(90, 250, "Grasshopper", "img/GrasshopperWhite.png"))
group_hive_white.add(Player_Hive(90, 340, "Grasshopper", "img/GrasshopperWhite.png"))
group_hive_white.add(Player_Hive(90, 430, "Spider", "img/SpiderWhite.png"))
group_hive_white.add(Player_Hive(90, 520, "Spider", "img/SpiderWhite.png"))
group_hive_white.add(Player_Hive(90, 610, "Ant", "img/AntWhite.png"))
group_hive_white.add(Player_Hive(90, 700, "Ant", "img/AntWhite.png"))
group_hive_white.add(Player_Hive(90, 790, "Ant", "img/AntWhite.png"))


group_hive_white_beatle = pygame.sprite.Group()
group_hive_white_beatle.add(Player_Hive_Beatle(90, 880, "Beatle", "img/BeatleWhite.png",1))
group_hive_white_beatle.add(Player_Hive_Beatle(90, 970, "Beatle", "img/BeatleWhite.png",2))


group_hive_black = pygame.sprite.Group()
group_hive_black.add(Player_Hive(1100, 70, "Queen", "img/QueenBlack.png"))
group_hive_black.add(Player_Hive(1100, 160, "Grasshopper", "img/GrasshopperBlack.png"))
group_hive_black.add(Player_Hive(1100, 250, "Grasshopper", "img/GrasshopperBlack.png"))
group_hive_black.add(Player_Hive(1100, 340, "Grasshopper", "img/GrasshopperBlack.png"))
group_hive_black.add(Player_Hive(1100, 430, "Spider", "img/SpiderBlack.png"))
group_hive_black.add(Player_Hive(1100, 520, "Spider", "img/SpiderBlack.png"))
group_hive_black.add(Player_Hive(1100, 610, "Ant", "img/AntBlack.png"))
group_hive_black.add(Player_Hive(1100, 700, "Ant", "img/AntBlack.png"))
group_hive_black.add(Player_Hive(1100, 790, "Ant", "img/AntBlack.png"))
group_hive_black.add(Player_Hive(1100, 880, "Beatle", "img/BeatleBlack.png"))
group_hive_black.add(Player_Hive(1100, 970, "Beatle", "img/BeatleBlack.png"))


for i in range(10):
    for j in range(10):
        if j % 2 == 0:
            hexs_group.add(Hex(160+100*(j+1) -25*j, 86*(i+1), 'img/BorderPole.png', [i,j]))
        else:
           hexs_group.add(Hex(160+100*(j+1) -25*j, 86*(i+1)+43, 'img/BorderPole.png', [i,j]))
        


#57

#принимает координаты клика и центра гекса, возращает bool
#x1, y1 - точка
#x2, y2 - центр гекса
#z - длина ребра
def IsBelongingPointToHexagon(x1, y1, x2, y2, z):

    x = abs(x1 - x2) 
    y = abs(y1 - y2)

    py1 = z * 0.86602540378;
    px2 = z * 0.2588190451;
    py2 = z * 0.96592582628;

    p_angle_01 = -x * (py1 - y) - x * y;
    p_angle_20 = -y * (px2 - x) + x * (py2 - y);
    p_angle_03 = y * z;
    p_angle_12 = -x * (py2 - y) - (px2 - x) * (py1 - y);
    p_angle_32 = (z - x) * (py2 - y) + y * (px2 - x);

    is_inside_1 = (p_angle_01 * p_angle_12 >= 0) and (p_angle_12 * p_angle_20 >= 0);
    is_inside_2 = (p_angle_03 * p_angle_32 >= 0) and (p_angle_32 * p_angle_20 >= 0);

    return is_inside_1 or is_inside_2;

#выбранный гекс поля в данный момент, используется для выделения   
hex_group_now_choice = pygame.sprite.Group() 
hex_group_posible_moves = pygame.sprite.Group() 
#выбранный гекс на поле
now_sprite = None
#выбранная фишка белых           
white_click = None

white_click_beatle = None

black_click = None

for_beatle_click = None
flag_black_beatle_click = False

flag_white_click = False
flag_black_click = False
flag_click_Hex = False
list_possible_moves = None

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            if event.button == 1:
                print(event.pos)
                x_1 = 0
                x_2 = 0
                y_1 = 0
                y_2 = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                
                clicked_sprites = [s for s in hexs_group if s.rect.collidepoint(pos)]
                               
                clicked_white_hive = [s for s in group_hive_white if s.rect.collidepoint(pos)]
                
                clicked_black_hive = [s for s in group_hive_black if s.rect.collidepoint(pos)]
                
                clicked_white_beatle = [s for s in group_hive_white_beatle if s.rect.collidepoint(pos)]
                

                
                #клик на поле
                if len(clicked_sprites) != 0:
                    now_sprite = clicked_sprites[0]
                    
                    flag_click_Hex = True
                    #print("мы тыкнули на гекс: ", now_sprite.mas)
                    
                     
                
                if len(clicked_sprites) == 2:                                       
                    if not(IsBelongingPointToHexagon(pos[0], pos[1], clicked_sprites[0].x_center, clicked_sprites[0].y_center, 50)):
                        now_sprite = clicked_sprites[1]                       
                        flag_click_Hex = True
                        
                    #print("мы тыкнули на гекс: ", now_sprite.mas)
                
                                      
                        
                
                #клик на белых               
                print(len(clicked_white_hive))
                
                if len(clicked_white_hive) !=0:
                    white_click = clicked_white_hive[0]
                    flag_white_click = True
                    flag_click_Hex = False
                    #print("мы тыкнули на белый гекс: ", white_click.mas)
                    black_click = None
                    
                
                if len(clicked_white_hive) == 2:
                    if not(IsBelongingPointToHexagon(pos[0], pos[1], clicked_white_hive[0].x_center, clicked_white_hive[0].y_center, 50)):
                        white_click = clicked_white_hive[1]
                        flag_white_click = True
                        flag_black_click = False
                        flag_click_Hex = False
                        black_click = None
                        
                    #print("мы тыкнули на белый гекс: ", white_click.mas)
                
                
                #клик на белого жука    
                if len(clicked_white_beatle) != 0:
                        white_click_beatle = clicked_white_beatle[0]
                        flag_white_click = False
                        flag_click_Hex = False
                        black_click = None
                        
                
                if len(clicked_white_beatle) == 2:
                    if not(IsBelongingPointToHexagon(pos[0], pos[1], clicked_sprites[0].x_center, clicked_sprites[0].y_center, 50)):
                        white_click_beatle = clicked_white_beatle[1] 
                        flag_white_click = False
                        flag_click_Hex = False
                        black_click = None
                        
                
                
                if white_click is not None:
                    if white_click.type == "Queen" and white_click.mas is not None:
                        list_possible_moves = state.queen_check(white_click.mas[0], white_click.mas[1])
                    if white_click.type == "Grasshopper" and white_click.mas is not None:
                        list_possible_moves = state.grasshopper_chek(white_click.mas[0], white_click.mas[1])
                    if white_click.type == "Spider" and white_click.mas is not None:
                        list_possible_moves = state.spider_ant_check(white_click.mas[0], white_click.mas[1], "Spider")
                    if white_click.type == "Ant" and white_click.mas is not None:
                        list_possible_moves = state.spider_ant_check(white_click.mas[0], white_click.mas[1], "Ant")   

                    
                
                #клик на черных
                if len(clicked_black_hive) !=0:
                    black_click = clicked_black_hive[0]
                    flag_black_click = True
                    flag_white_click = False
                    flag_click_Hex = False
                    white_click = None
                    #print("мы тыкнули на белый гекс: ", white_click.mas)
                    
                
                if len(clicked_black_hive) == 2:
                    if not(IsBelongingPointToHexagon(pos[0], pos[1], clicked_black_hive[0].x_center, clicked_black_hive[0].y_center, 50)):
                        black_click = clicked_black_hive[1]
                        flag_black_click = True
                        flag_white_click = False
                        
                        white_click = None    
                # print(white_click.mas)
                # print(now_sprite) 
                for black in group_hive_black:
                    if black.mas is not None and now_sprite is not None:
                        if black.mas == now_sprite.mas and black.type == "Beatle":
                            flag_black_beatle_click = True
                            #print("Да вика, это черный жук")
                
                # if white_click is not None and white_click.type == "Beatle":
                #     for_beatle_click = white_click
                    
                # if for_beatle_click is not None and for_beatle_click.mas is not None and now_sprite is not None and for_beatle_click.mas != now_sprite.mas:
                #     for white in group_hive_white:
                #         if white.mas is not None and white.type == "Beatle" and white.mas == for_beatle_click.mas:
                #             white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                #             for_beatle_click = None
                #             break;
                            
                        #     if white_click.mas is None and white.mas is None:
                        #         white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                        #         break
                            
                        #     else:
                        #         if white.mas == white_click.mas:
                        #             white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                        #             break  
                    
                #flag_move_white_beatle = True
                
                if white_click_beatle is not None:
                    flag_big_beatle = True
                    for beatle in group_hive_white_beatle:
                        if beatle.mas is None and white_click_beatle.mas is None and now_sprite is not None:
                            beatle.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]]);
                            #flag_move_white_beatle = False
                            white_click_beatle = None
                            break
                        elif beatle.mas is not None and now_sprite is not None and beatle.mas != now_sprite.mas and white_click_beatle.id == beatle.id:
                            beatle.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]]);
                            for white in group_hive_white:
                                if white.mas is not None and beatle.mas == white.mas:
                                    beatle.update_img("img/BeatleWhiteSmile.png")
                                    flag_big_beatle = False
                                    white_click_beatle = None
                                    break
                            for black in group_hive_black:
                                if black.mas is not None and beatle.mas == black.mas:
                                    beatle.update_img("img/BeatleWhiteSmile.png")
                                    flag_big_beatle = False
                                    white_click_beatle = None
                                    break
                            
                            if flag_big_beatle:
                                   beatle.update_img("img/BeatleWhite.png")
                                   white_click_beatle = None             
                            #flag_move_white_beatle = False
                            #white_click_beatle = None
                            break
                    flag_click_Hex = False
                    
                    
                   
                #перемещение фишки
                if (flag_white_click and flag_click_Hex):
                    state.turn +=1
                    type = white_click.type
                    # group_hive_white.update(Queen(200,200,[0,0]))
                    for white in group_hive_white:
                        
                        if white.type == "Queen" and white_click.type == "Queen":
                            
                            if white.mas is None:
                                state.active_now +=1
                                state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                                    
                            elif white.mas is not None and now_sprite.mas in list_possible_moves:
                                state.board[white.mas[0]][white.mas[1]] = None                           
                                white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])                                                      
                                state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                
                            list_possible_moves = None
                            break   
                                                                                           
                        elif white.type == "Grasshopper" and white_click.type == "Grasshopper":
                            
                            if white_click.mas is None and white.mas is None:
                                state.active_now +=1
                                state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                list_possible_moves = None
                                break
                                                                                  
                            elif list_possible_moves is not None and white.mas is not None and now_sprite.mas in list_possible_moves:
                                if white.mas == white_click.mas:
                                    state.board[white.mas[0]][white.mas[1]] = None
                                    white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                    state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                    list_possible_moves = None
                                    
                                    break
                            
                        
                        elif white.type == "Spider" and white_click.type == "Spider":
                            
                            if white_click.mas is None and white.mas is None:
                                state.active_now +=1
                                state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                list_possible_moves = None
                                break
                            
                            elif list_possible_moves is not None and white.mas is not None and now_sprite.mas in list_possible_moves:
                                if white.mas == white_click.mas:
                                    state.board[white.mas[0]][white.mas[1]] = None
                                    white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                    state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                    list_possible_moves = None
                                    break
                                
                        elif white.type == "Ant" and white_click.type == "Ant":
                            
                            if white_click.mas is None and white.mas is None:
                                state.active_now +=1
                                state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                list_possible_moves = None
                                break
                            
                            elif list_possible_moves is not None and white.mas is not None and now_sprite.mas in list_possible_moves:
                                if white.mas == white_click.mas:
                                    state.board[white.mas[0]][white.mas[1]] = None
                                    white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                    state.board[now_sprite.mas[0]][now_sprite.mas[1]] = white.type
                                    list_possible_moves = None
                                    break 
                                
                        # elif white.type == "Beatle" and white_click.type == "Beatle":
                        #     if white_click.mas is None and white.mas is None:
                        #         white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                        #         break
                            
                        #     else:
                        #         if white.mas == white_click.mas:
                        #             white.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                        #             break   
                                         
                    flag_white_click = False
                    flag_click_Hex = False
                    #print(state.turn)                                                                                       
                
                if flag_black_click and flag_click_Hex:
                    state.turn +=1
                    type = black_click.type
                    # group_hive_white.update(Queen(200,200,[0,0]))
                    for black in group_hive_black:
                        if black.type == "Queen" and black_click.type == "Queen":
                            black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                            break
                        elif black.type == "Grasshopper" and black_click.type == "Grasshopper":
                            if black.mas == None:
                                black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                break
                            else:
                                if black.mas == black_click.mas:
                                    black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                    break
                        elif black.type == "Spider" and black_click.type == "Spider":
                            if black.mas == None:
                                black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                break;
                            else:
                                if black.mas == black_click.mas:
                                    black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                    break
                        elif black.type == "Ant" and black_click.type == "Ant":
                            if black.mas == None:
                                black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                break;
                            else:
                                if black.mas == black_click.mas:
                                    black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                    break 
                        elif black.type == "Beatle" and black_click.type == "Beatle":
                            if black.mas == None:
                                black.update_pos(now_sprite.x_center, now_sprite.y_center, [now_sprite.mas[0], now_sprite.mas[1]])
                                break
                            else:
                                if black.mas == black_click.mas:
                                    #black.update_pos(for_beatle_click.x_center, for_beatle_click.y_center, [for_beatle_click.mas[0], for_beatle_click.mas[1]])
                                    break            
                    flag_black_click = False
                    flag_black_beatle_click = False
                    
                    #print(state.turn)
                #print(white_click) 
                
                if now_sprite is not None:
                    hex_group_now_choice.empty()
                    hex_group_now_choice.add(Hex(now_sprite.x_center, now_sprite.y_center, 'img/BorderBlue.png', [now_sprite.mas[0],now_sprite.mas[1]]))
                    now_sprite = None
                    
                elif white_click_beatle is not None:
                    hex_group_now_choice.empty()
                    hex_group_now_choice.add(Hex(white_click_beatle.x_center, white_click_beatle.y_center, 'img/BorderBlue.png', [None, None])) 
                                  
                elif white_click is not None:
                    hex_group_now_choice.empty()
                    hex_group_now_choice.add(Hex(white_click.x_center, white_click.y_center, 'img/BorderBlue.png', [None, None]))                
                                           
                elif black_click is not None:
                    hex_group_now_choice.empty()
                    hex_group_now_choice.add(Hex(black_click.x_center, black_click.y_center, 'img/BorderBlue.png', [None, None]))
                else:
                    hex_group_now_choice.empty()
                    
                
                if list_possible_moves is not None and len(list_possible_moves) > 0:
                    for hex_fiels in hexs_group:
                        if hex_fiels.mas in list_possible_moves:
                            hex_group_posible_moves.add(Hex(hex_fiels.x_center, hex_fiels.y_center, 'img/BorderGreen.png', [hex_fiels.mas[0], hex_fiels.mas[1]]))
                else:
                    hex_group_posible_moves.empty()
                    
                   
            if event.button == 3:
                hex_group_now_choice.empty()
                hex_group_posible_moves.empty()
                list_possible_moves = None
                now_sprite = None
                flag_white_click = False
                flag_click_Hex = False
                
                
                                  

                    
    # screen.fill(WHITE)
    
    group_hive_white.draw(screen)
    group_hive_black.draw(screen)
    group_hive_white_beatle.draw(screen)
    hexs_group.draw(screen)
    hex_group_now_choice.draw(screen)
    hex_group_posible_moves.draw(screen)
    
    
    
    
    #screen.blit(queen_white.image, queen_white.rect)
    
    pygame.display.update()
    pygame.time.delay(20)
 

import itertools
from model.player import Player
from model.hive import Queen
from copy import deepcopy


class State:
    def __init__(self):
        self.board_size = 10
        self.board = [
            [None for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        self.player_list = []
        self.white_spider_list = []#паук - 2 шт макс - есть
        self.white_beatle_list = []#жук - 3 шт макс
        self.white_grasshopper_list = []#кузнечик - 3 шт макс - есть
        self.white_ant_list = []#муравей - 3 шт макс - есть
        self.white_queen = None #Королева
        self.active_now=0
        self.turn=1
        

    def initial_state(self):
        # init player
        self.player_list.append(Player(0))
        self.player_list.append(Player(1))

        #self.white_queen = Queen(1,1,0)
        #self.board[1][1] = self.white_queen+
        # self.board[1][3] = "HOB1"
        # self.board[2][3] = "HOB2"
        # self.board[3][2] = "HOB3"
        # self.board[3][1] = "HOB4"
        # self.board[3][4] = "HOB5"
        # self.board[3][3] = "HOB1"
        # self.board[4][3] = "HOB2"
        # self.board[4][4] = "HOB3"
        # self.board[5][2] = "HOB4"
        # self.board[5][4] = "HOB5"
        # self.board[6][4] = "HOB5"
        #self.board[4][1] = "HOB5"

        for i, j in itertools.product(range(self.board_size), range(self.board_size)):
            if(self.board[i][j] is not None):
                self.active_now+=1

        # self.board[4][8] = "HOB6"
        # self.board[3][9] = "HOB7"
        #self.board[4][2] = "HOB8"
   
   #ходит паук
   #на вход принимает позицию x,y, возвращает возможные ходы для паука и муравья 
    def spider_ant_check(self, x, y, type_insect):
        print("start")
        #self.board[x][y] = None
        coordinate = []
        new_board = deepcopy(self.board)
        new_board[x][y] = None
        # x_1 = x+(-1+2*(y%2))
        # print(x_1)
        posible_move_start = []
        active = self.active_now - 1
        if(new_board[x+1][y] is None and self.check_turn(x+1,y,active,new_board)):
            posible_move_start.append([x+1,y])
            #print("верно1 = ",x+1,y)
        if(new_board[x-1][y] is None and self.check_turn(x-1,y,active,new_board)):
            posible_move_start.append([x-1,y])
            #print("верно2 = ",x-1,y)
        if(new_board[x][y+1] is None and self.check_turn(x,y+1,active,new_board)):
            posible_move_start.append([x,y+1])
            #print("верно3 = ",x,y+1)
        if(new_board[x][y-1] is None and self.check_turn(x,y-1,active,new_board)):
            posible_move_start.append([x,y-1])
            #print("верно4 = ",x,y-1)
        if(new_board[x+(-1+2*(y%2))][y+1] is None and self.check_turn(x+(-1+2*(y%2)),y+1,active,new_board)):
            posible_move_start.append([x+(-1+2*(y%2)),y+1])
            #print("верно5 = ",x+(-1+2*(y%2)),y+1)
        if(new_board[x+(-1+2*(y%2))][y-1] is None and self.check_turn(x+(-1+2*(y%2)),y-1,active,new_board)):
            posible_move_start.append([x+(-1+2*(y%2)),y-1])
            #print("верно6 = ",x+(-1+2*(y%2)),y-1)

        slip_move = self.check_slip(new_board, x,y)

        coincidences_flag = True

        move_list = []
        for item in posible_move_start:
            if item in slip_move:
                coincidences_flag = False
                #print("есть совпадения = ", item[0], item[1] )
                move_list.append( [item[0], item[1]])
        
        move_list = self.next_step_req(new_board, type_insect, move_list)
        if(type_insect == "Ant" and len(move_list) > 0):
            move_list.remove([x,y])
        
        return move_list
            
            
    def queen_check(self, x, y):
        new_board = deepcopy(self.board)
        new_board[x][y] = None
        
        posible_move_start = []
        active = self.active_now - 1
        if(new_board[x+1][y] is None and self.check_turn(x+1,y,active,new_board)):
            posible_move_start.append([x+1,y])
            #print("верно1 = ",x+1,y)
        if(new_board[x-1][y] is None and self.check_turn(x-1,y,active,new_board)):
            posible_move_start.append([x-1,y])
            #print("верно2 = ",x-1,y)
        if(new_board[x][y+1] is None and self.check_turn(x,y+1,active,new_board)):
            posible_move_start.append([x,y+1])
            #print("верно3 = ",x,y+1)
        if(new_board[x][y-1] is None and self.check_turn(x,y-1,active,new_board)):
            posible_move_start.append([x,y-1])
            #print("верно4 = ",x,y-1)
        if(new_board[x+(-1+2*(y%2))][y+1] is None and self.check_turn(x+(-1+2*(y%2)),y+1,active,new_board)):
            posible_move_start.append([x+(-1+2*(y%2)),y+1])
            #print("верно5 = ",x+(-1+2*(y%2)),y+1)
        if(new_board[x+(-1+2*(y%2))][y-1] is None and self.check_turn(x+(-1+2*(y%2)),y-1,active,new_board)):
            posible_move_start.append([x+(-1+2*(y%2)),y-1])
            #print("верно6 = ",x+(-1+2*(y%2)),y-1)

        slip_move = self.check_slip(new_board, x,y)
        
        move_list = []
        
        for item in posible_move_start:
            if item in slip_move:
                coincidences_flag = False
                #print("есть совпадения = ", item[0], item[1] )
                move_list.append( [item[0], item[1]])
        
        return move_list
        
          
    #на вход принимает позицию x,y, возвращает возможные ходы для паука и муравья           
    def grasshopper_chek(self, x, y):
        new_board = deepcopy(self.board)
        new_board[x][y] = None
        active = self.active_now-1
        
        vector_flag = True
        move_list = []
        i = 1
        while(vector_flag): #прыжок вниз
            
            if(new_board[x+i][y] and new_board[x+i][y] is not None):
                i+=1
            else:
                vector_flag = False
                if( i != 1):
                    move_list.append([x+i,y])
                    
           
        vector_flag = True
        i = 1
        while(vector_flag): #прыжок вверх
            
            if(new_board[x-i][y] and new_board[x-i][y] is not None):
                i+=1
            else:
                vector_flag = False
                if( i != 1):
                    move_list.append([x-i,y])
        
        vector_flag = True
        k = 1
        y_now = y
        x_now = x
        while(vector_flag): #прыжок вверх-право
            if(y_now % 2 == 1):
                if(new_board[x_now][y_now+1] and new_board[x_now][y_now+1] is not None):
                    k += 1
                    y_now+=1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now,y_now+1])
            else:
                if(new_board[x_now-1][y_now+1] and new_board[x_now-1][y_now+1] is not None):
                    k += 1
                    y_now += 1
                    x_now -= 1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now-1,y_now+1])  
                      
        vector_flag = True
        k = 1
        y_now = y
        x_now = x
        while(vector_flag): #прыжок вверх-лево
            if(y_now % 2 == 1):
                if(new_board[x_now][y_now-1] and new_board[x_now][y_now-1] is not None):
                    k += 1
                    y_now-=1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now,y_now-1])
            else:
                if(new_board[x_now-1][y_now-1] and new_board[x_now-1][y_now-1] is not None):
                    k += 1
                    y_now -= 1
                    x_now -= 1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now-1,y_now-1])
        vector_flag = True
        k = 1
        y_now = y
        x_now = x
        while(vector_flag): #прыжок низ-право
            if(y_now % 2 == 1):
                if(new_board[x_now+1][y_now+1] and new_board[x_now+1][y_now+1] is not None):
                    k += 1
                    x_now += 1
                    y_now += 1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now+1,y_now+1])
            else:
                if(new_board[x_now][y_now+1] and new_board[x_now][y_now+1] is not None):
                    k += 1
                    y_now += 1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now,y_now+1])
        
        vector_flag = True
        k = 1
        y_now = y
        x_now = x
        while(vector_flag): #прыжок низ-лево
            if(y_now % 2 == 1):
                if(new_board[x_now+1][y_now-1] and new_board[x_now+1][y_now-1] is not None):
                    k += 1
                    x_now += 1
                    y_now -= 1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now+1,y_now-1])
            else:
                if(new_board[x_now][y_now-1] and new_board[x_now][y_now-1] is not None):
                    k += 1
                    y_now -= 1
                else:
                    vector_flag = False
                    if( k != 1):
                        move_list.append([x_now,y_now-1])                
                        
        hope_flag = True
        
        for item in move_list:
            if(hope_flag):
                if not(self.check_turn(item[0], item[1], active, new_board)):
                    hope_flag = False
                    print("тут", item[0], item[1])
        
        if(hope_flag):
            return move_list
        else:
            return []
        #print("координаты движения кузнечика = ",  move_list)
        
    

    #доделать active или передавать число
    #функция проверки целостности дерева, получает на вход координаты м проверяет целостность дерева от этих координат
    def check_turn(self, x, y, active, board):

        tree = []

        def tree_build(self,x,y,tree):

            if(board[x-1][y] is not None and [[x-1],[y]] not in tree):
                tree.append([[x-1],[y]])
                tree_build(self, x-1, y, tree)           
            if(board[x+1][y] is not None and [[x+1],[y]] not in tree):
                tree.append([[x+1],[y]])
                tree_build(self, x+1, y, tree)
            if(board[x][y-1] is not None and [[x],[y-1]] not in tree):
                tree.append([[x],[y-1]])
                tree_build(self, x, y-1, tree)
            if(board[x][y+1] is not None and [[x],[y+1]] not in tree):
                tree.append([[x],[y+1]])
                tree_build(self, x, y+1, tree)
            if(board[x+(-1+2*(y%2))][y+1] is not None and [[x+(-1+2*(y%2))],[y+1]] not in tree):
                tree.append([[x+(-1+2*(y%2))],[y+1]])
                tree_build(self, x+(-1+2*(y%2)), y+1, tree)
            if(board[x+(-1+2*(y%2))][y-1] is not None and [[x+(-1+2*(y%2))],[y-1]] not in tree):
                tree.append([[x+(-1+2*(y%2))],[y-1]])
                tree_build(self, x+(-1+2*(y%2)), y-1, tree)

        tree_build(self, x, y, tree)
        
        return active == len(tree)

        #return len(active) == len(tree)
    #функция проверки возможности передвижения скольжением на вход - текущая позиция, возвращает доступные координаты с учетом скольжения(правило)   
    def check_slip(self, new_board, x_now ,y_now):
        tree = []
        
        def attemp(tree,x,y):
            #если координата y - четная
            if( y % 2 == 0):
                #if(new_board[x][y] is None and (() or () )):
                if(new_board[x+1][y] is None and ((new_board[x][y-1] is None and new_board[x][y+1] is not None) or (new_board[x][y+1] is None and new_board[x][y-1] is not None) )):
                    tree.append([x+1,y])#проверили клетку ниже
                    #print("скольжение четное j, верный ход = ",x+1,y)
                if(new_board[x-1][y] is None and ((new_board[x-1][y-1] is None and new_board[x-1][y+1] is not None) or (new_board[x-1][y+1] is None and new_board[x-1][y-1] is not None) )):
                    tree.append([x-1,y])#проверили клетку выше
                    #print("скольжение четное j, верный ход = ",x-1,y)
                if(new_board[x][y-1] is None and ((new_board[x-1][y-1] is None and new_board[x+1][y] is not None) or (new_board[x+1][y] is None and new_board[x-1][y-1] is not None) )):
                    tree.append([x,y-1])#проверили клетку лево-низ
                    #print("скольжение четное j, верный ход = ",x,y-1)
                if(new_board[x][y+1] is None and ((new_board[x+1][y] is None and new_board[x-1][y+1] is not None) or (new_board[x-1][y+1] is None and new_board[x+1][y] is not None) )):
                    tree.append([x,y+1])#проверили клетку право-низ
                    #print("скольжение четное j, верный ход = ",x,y+1)
                if(new_board[x-1][y-1] is None and ((new_board[x][y-1] is None and new_board[x-1][y] is not None) or (new_board[x-1][y] is None and new_board[x][y-1] is not None) )):
                    tree.append([x-1,y-1])#проверили клетку лево-верх
                    #print("скольжение четное j, верный ход = ",x-1,y-1)
                if(new_board[x-1][y+1] is None and ((new_board[x-1][y] is None and new_board[x][y+1] is not None) or (new_board[x][y+1] is None and new_board[x-1][y] is not None) )):
                    tree.append([x-1,y+1])#проверили клетку право-верх
                    #print("скольжение четное j, верный ход = ",x-1,y+1)
            else:
                if(new_board[x+1][y] is None and ((new_board[x+1][y-1] is None and new_board[x+1][y+1] is not None) or (new_board[x+1][y+1] is None and new_board[x+1][y-1] is not None) )):
                    tree.append([x+1,y])#проверили клетку ниже
                    #print("скольжение НЕчетное j, верный ход = ",x+1,y)
                if(new_board[x-1][y] is None and ((new_board[x][y-1] is None and new_board[x][y+1] is not None) or (new_board[x][y+1] is None and new_board[x][y-1] is not None) )):
                    tree.append([x-1,y])#проверили клетку выше
                    #print("скольжение НЕчетное j, верный ход = ",x-1,y)
                if(new_board[x+1][y-1] is None and ((new_board[x][y-1] is None and new_board[x+1][y] is not None) or (new_board[x+1][y] is None and new_board[x][y-1] is not None) )):
                    tree.append([x+1,y-1])#проверили клетку лево-низ
                    #print("скольжение НЕчетное j, верный ход = ",x+1,y-1)
                if(new_board[x+1][y+1] is None and ((new_board[x+1][y] is None and new_board[x][y+1] is not None) or (new_board[x][y+1] is None and new_board[x+1][y] is not None) )):
                    tree.append([x+1,y+1])#проверили клетку право-низ
                    #print("скольжение НЕчетное j, верный ход = ",x+1,y+1)
                if(new_board[x][y-1] is None and ((new_board[x+1][y-1] is None and new_board[x-1][y] is not None) or (new_board[x-1][y] is None and new_board[x+1][y-1] is not None) )):
                    tree.append([x,y-1])#проверили клетку лево-верх
                    #print("скольжение НЕчетное j, верный ход = ",x,y-1)
                if(new_board[x][y+1] is None and ((new_board[x-1][y] is None and new_board[x+1][y+1] is not None) or (new_board[x+1][y+1] is None and new_board[x-1][y] is not None) )):
                    tree.append([x,y+1])#проверили клетку право-верх
                    #print("скольжение НЕчетное j, верный ход = ",x,y+1)
        attemp(tree, x_now, y_now)
        
        return tree      
    
    #рекурсивная фунция для жука и муравья, на вход новая доска, тип насекомого, возможные ходы после первой проверки. Вернет координаты всех доступных ходов
    def next_step_req(self, new_bord, type, move_list):
            step = []
            intermediate_step = []
            extra_steps = deepcopy(move_list)
            move_list_all = deepcopy(move_list)  

            def next_step(x, y, n):
                if(type == "Spider" and n == 0):
                    step = self.check_slip(new_bord, x,y)
                    for item in step:
                        if item not in extra_steps:
                            extra_steps.append([item[0], item[1]])
                            next_step(item[0], item[1], n+1)
                else:
                    step = self.check_slip(new_bord, x,y)            
                    for item in step:
                        if item not in extra_steps:
                            intermediate_step.append([item[0], item[1]])
                            
                if(type == "Ant"):
                    step = self.check_slip(new_bord, x,y)
                    for item in step:
                        if item not in extra_steps:
                            extra_steps.append([item[0], item[1]])
                            next_step(item[0], item[1], 0)
                       
                    

            for item in move_list_all:
                next_step(item[0], item[1], 0)
                
            #print(intermediate_step)
            #print(extra_steps)
            
            return intermediate_step if (type == "Spider") else extra_steps

      


        
        
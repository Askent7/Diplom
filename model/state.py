from model.player import Player
from model.hive import Queen


class State:
    def __init__(self):
        self.board_size = 10
        self.board = [
            [None for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        self.player_list = []
        self.white_spider_list = []#паук - 2 шт макс
        self.white_beatle_list = []#жук - 3 шт макс
        self.white_grasshopper_list = []#кузнечик - 3 шт макс
        self.white_ant_list = []#муравей - 3 шт макс
        self.white_queen = None #Королева


    def initial_state(self):
        # init player
        self.player_list.append(Player(0))
        self.player_list.append(Player(1))

        #self.white_queen = Queen(1,1,0)

        #self.board[1][1] = self.white_queen+
        self.board[1][3] = "HOB1"
        self.board[2][2] = "HOB2"
        self.board[2][3] = "HOB3"
        self.board[2][4] = "HOB4"
        self.board[1][5] = "HOB5"
        self.board[1][6] = "HOB6"
        #self.board[6][4] = "HOB7"
        #self.board[4][2] = "HOB8"
   
   #ходит паук 
    def spider_check(self, x, y):
        print("start")
        self.board[x][y] = None
        coordinate = []
        
        
        
        # if( self.check_turn( x,y,0) ):
        #     print("Можно ходить")
        #     coordinate = []
        # else:
        #     self.board[x][y] = "SPID"


    #доделать active или передавать число
    def check_turn(self, x, y, active):

        tree = []

        def tree_build(self,x,y,tree):

            if(self.board[x-1][y] is not None and [[x-1],[y]] not in tree):
                tree.append([[x-1],[y]])
                tree_build(self, x-1, y, tree)
            
            if(self.board[x-1][y-1] is not None and [[x-1],[y-1]] not in tree):
                tree.append([[x-1],[y-1]])
                tree_build(self, x-1, y-1, tree)
            if(self.board[x][y-1] is not None and [[x],[y-1]] not in tree):
                tree.append([[x],[y-1]])
                tree_build(self, x, y-1, tree)
            if(self.board[x+1][y] is not None and [[x+1],[y]] not in tree):
                tree.append([[x+1],[y]])
                tree_build(self, x+1, y, tree)
            if(self.board[x][y+1] is not None and [[x],[y+1]] not in tree):
                tree.append([[x],[y+1]])
                tree_build(self, x, y+1, tree)
            if(self.board[x-1][y+1] is not None and [[x-1],[y+1]] not in tree):
                tree.append([[x-1],[y+1]])
                tree_build(self, x-1, y+1, tree)

        tree_build(self, x, y, tree)
        
        return active == len(tree)

        #return len(active) == len(tree)
        



      


        
        
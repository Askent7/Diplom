from model.state import State


from datetime import datetime
import time
start_time = datetime.now()
state = State()

state.initial_state()
# test = state.check_turn(2,5,6)
# print(test)
#list = state.spider_ant_check(6,2, "Ant")
listt = state.grasshopper_chek(5,2)

print(listt)
#state.check_slip(state.board, 4,5)
print( "время работы = ", datetime.now() - start_time)

"""
for i in range(state.board_size):
    for j in range(state.board_size):
        print(state.board[i][j], end = " ")
    print()
"""
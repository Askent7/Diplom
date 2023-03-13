from model.state import State

state = State()

state.initial_state()
# test = state.check_turn(2,5,6)
# print(test)
state.spider_check(1,2)


"""
for i in range(state.board_size):
    for j in range(state.board_size):
        print(state.board[i][j], end = " ")
    print()
"""
import state

state = state.State()
state.occupied = [[False,False,False,False],
                  [False,False,False,False],
                  [False,True,False,False],
                  [False,False,False,False]]
assert(state.eval() == 2) # because top 2 lines are empty
print("PASS")

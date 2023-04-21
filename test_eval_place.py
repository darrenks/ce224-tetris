import state

state = state.State()

test =           [[False,False,False,False],
                  [False,False,False,False],
                  [False,False,False,False],
                  [True,False,False,False],
                  [True,False,False,True]]

assert(state.eval_place() == test)
print("PASS")


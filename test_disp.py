import state

state = state.State()
state.start_game()
state.activate_random_piece()
state.occupied = [[False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,False],
                  [False,False,False,False,False,False,False,False,False,True],
                  [False,False,False,False,False,False,False,False,False,True],
                  [False,False,False,False,False,False,False,False,False,True],
                  [False,True,True,True,True,False,False,False,False,True]]
state.display()

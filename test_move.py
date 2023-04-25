import state
import consts

state = state.State()
state.start_game()
print("Old position: ", state.active)
state.move(consts.RIGHT)
print("New position: ", state.active)

print("Old position: ", state.active)
state.move(consts.DOWN)
print("New position: ", state.active)

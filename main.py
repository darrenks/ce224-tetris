import consts
import state
import curses

use_ai = False

def get_input():
    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(True)
    
    while True:
        # wait for user input
        char = screen.getch()
        
        if char == ord('a'):
            # rotate left
            return consts.ROTATE_LEFT
        elif char == ord('f'):
            # rotate right
            return consts.ROTATE_RIGHT
        elif char == curses.KEY_DOWN:
            # move down
            return consts.MOVE_DOWN
        elif char == curses.KEY_LEFT:
            # move left
            return consts.MOVE_LEFT
        elif char == curses.KEY_RIGHT:
            # move right
            return consts.MOVE_RIGHT

state = state.State()
state.start_game()
while True:
    state.display()
    if state.lost: break

    if use_ai:
        action=state.search()
    else:
        action=get_input()

    prev_state = state.dup()
    state.move(action)
    if action==consts.DOWN and state==prev_state:
        state.place()

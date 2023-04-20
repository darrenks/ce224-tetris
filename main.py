import consts
from state import State

## you will need to do python -m pip install windows-curses
# to get this to work on the windows computers (then run from command line)
import curses

use_ai = False

def get_input(screen):
    while True:
        # wait for user input
        char = screen.getch()

        if char == ord('a'):
            # rotate left
            return consts.ROT_COUNTER
        elif char == ord('f'):
            # rotate right
            return consts.ROT_CLOCK
        elif char == curses.KEY_DOWN:
            # move down
            return consts.DOWN
        elif char == curses.KEY_LEFT:
            # move left
            return consts.LEFT
        elif char == curses.KEY_RIGHT:
            # move right
            return consts.RIGHT

def main(screen):
    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(True)


    state = State()
    state.start_game()
    while True:
        state.display(screen)
        if state.lost: break

        if use_ai:
            action=state.search()
        else:
            action=get_input(screen)

        prev_state = state.dup()
        state.move(action)
        if action==consts.DOWN and state==prev_state:
            state.place()

curses.wrapper(main)

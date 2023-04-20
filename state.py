import random
import consts
class State:
    def start_game(self):
        self.occupied = [[False for x in range(consts.WIDTH)] for y in range(consts.HEIGHT)]
        self.lost = False
        self.activate_random_piece()

    # Create a copy of the state
    def dup(self):
        new = State()
        new.lost = self.lost
        new.occupied = [line.copy() for line in self.occupied]
        new.active = self.active.copy()
        return new

    def __eq__(self,rhs):
        return self.occupied == rhs.occupied and self.active == rhs.active and self.lost == rhs.lost

    def __hash__(self):
        # definitely not efficient, but correct and good enough for now
        return str(self.occupied).__hash__() ^ str(self.active).__hash__()

    def activate_random_piece(self):
        self.active = []
        piece = consts.PIECES[random.randrange(0,len(consts.PIECES))]
        for y,line in enumerate(piece.split("\n")):
            for x,char in enumerate(line):
                if char != " ":
                    if self.occupied[y][x]: self.lost = True
                    self.active.append((x,y))

    # determine how good of a position we are in, higher = better
    def eval(self):
        # for now we will use a simple method that counts number of empty lines from the top
        for y,line in enumerate(self.occupied):
            if any(line): return y
        return consts.HEIGHT

    # place the active piece and activate a random piece, possibly causing a loss
    def place(self):
        # place the active (todo Connor)
        # remove solid lines (todo Connor)
        self.activate_random_piece()

    def display(self):
        # print the game state (todo Max)
        board = []
        board.append([])
        count = 0

        for i in range(0,12):
            board[count].append('-')

        for i in self.occupied:
         count+=1 
         board.append([])
         board[count].append('|')
         for y in i:
            if y == True:
                board[count].append('█')
            else:
                board[count].append(' ')
         board[count].append('|')
        
        count+=1
        board.append([])
        for i in range(0,12):
            board[count].append('-')
            
        for i in self.active:
            board[i[0]+1][i[1]+1]=('█')
                

        for i in board:
            print("".join(i))
        pass

    def move(self,direction):
        # move or rotate the active piece (or leave same if invalid move)
        # a nested function to determine whether the new location is available
        def is_valid_move(new_positions):
            for x, y in new_positions:
                # if statement to make sure that the move does not move any part out of the board or into another occupied spot
                if x < 0 or x >= consts.WIDTH or y < 0 or y >= consts.HEIGHT or (y >= 0 and self.occupied[y][x]):
                    return False
            return True

        # a list to hold the new positions of the move
        new_positions = list(self.active)

        #print("Old position: ", self.active)

        # if statement to handle the inputs
        if direction == consts.LEFT:
            new_positions = [(x - 1, y) for x, y in self.active]
        elif direction == consts.RIGHT:
            new_positions = [(x + 1, y) for x, y in self.active]
        elif direction == consts.DOWN:
            new_positions = [(x, y + 1) for x, y in self.active]
        # if rotation, swap the x and y coords for 90 degree rotation
        elif direction == consts.ROT_CLOCK or direction == consts.ROT_COUNTER:
            pivot = self.active[1]  # Assuming the second block is the pivot
            for i, (x, y) in enumerate(self.active):
                rel_x, rel_y = x - pivot[0], y - pivot[1]
                if direction == consts.ROT_CLOCK:
                    new_positions[i] = (pivot[0] - rel_y, pivot[1] + rel_x)
                else:
                    new_positions[i] = (pivot[0] + rel_y, pivot[1] - rel_x)

        # if move is valid, update coords of active piece
        if is_valid_move(new_positions):
            self.active = new_positions
            #print("New position: ", self.active)
        #else:
            #print("Did not move.")
        pass

    def search(self):
        # recursively search effects of possible moves, calling eval at max depth to select the action that gives best expected result
        # todo (Mason)
        pass

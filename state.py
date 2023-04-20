import random
import consts
import time
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
        print(self.occupied)
        print(self.active)
        pass

    def move(self,direction):
        # move or rotate the active piece (or leave same if invalid move)
        # todo (Vann)
        pass

    def search(self):
        
        states = [self]
        stateMoves = {self:[]}
        
        highestEval = self.eval()
        bestPosition = self
        
        
        while True:
            currentState = states.pop(0)
            
            
            
            if currentState.eval() >= highestEval:
                highestEval = currentState.eval()
                bestPosition = currentState
                
            for move in consts.POSSIBLE_MOVES:
                nextState = currentState.dup().move(move)
                if nextState not in stateMoves:
                    stateMoves[nextState] = stateMoves.get(currentState).append(move)
                    states.append(nextState)
                    
        return(stateMoves[bestPosition][0])
            
            
            
        
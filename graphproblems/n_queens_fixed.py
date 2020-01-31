import copy

class Board(object):
    def __init__(self, n):
        self.n = n
        self.horizontal = [0] * n
        self.vertical = [0] * n
        self.diag_up = [0] * (2*n - 1) # Tricky
        self.diag_down = [0] * (2*n - 1) # Tricky
        self.num_queens = 0
        self.visited = []
        self.complete_solutions = []
    
    def _set_queen(self, row, col, value):
        self.horizontal[row] = value
        self.vertical[col] = value
        self.diag_up[row + col] = value
        self.diag_down[self.n - row + col - 1] = value #Might need to double check this
    
    def add(self, row, col):
        self._set_queen(row, col, 1)
        self.num_queens = self.num_queens + 1
        self.visited.append((row, col))
        
        if self.num_queens == self.n:
            self.complete_solutions.append(copy.copy(self.visited))
            self.show()
    
    def remove_last(self):
        self.num_queens = self.num_queens - 1
        row, col = self.visited.pop()
        self._set_queen(row, col, 0)
    
    def is_valid(self, row, col):
        return all([
            self.horizontal[row] == 0,
            self.vertical[col] == 0,
            self.diag_up[row + col] == 0,
            self.diag_down[self.n - row + col - 1] == 0
        ])
    
    def _order(self, row, col):
        return self.n * row + col

    def all_valid(self):
        valid = []
        for row in xrange(self.n):
            for col in xrange(self.n):
                if self.is_valid(row, col):
                    if len(self.visited) == 0:
                        valid.append((row, col))
                    elif self._order(self.visited[-1][0], self.visited[-1][1]) < self._order(row, col):
                        valid.append((row, col))
        return valid
    
    def show(self):
        for row in xrange(self.n):
            single_row = []
            for col in xrange(self.n):
                if (row, col) in self.visited:
                    single_row.append("Q")
                else:
                    single_row.append("_")
            print " ".join(single_row)
        print ""
    
        
def solution(n):
    board = Board(n)
    solutions(board)
    return len(board.complete_solutions)
        
def solutions(board):
    next_queens = board.all_valid()
    for row, col in next_queens:
        board.add(row, col)
        solutions(board)
        board.remove_last()



print solution(4)
print solution(8)

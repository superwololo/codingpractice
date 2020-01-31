

"""
arr1 = [1, 2, 3, 1, 2, 3]
arr2 = [1, 5, 3, 8, 0, 2, 3]


def longest_even(arr, index):
    
    




cumsum -> [1, 6, 9, 17, 0, 19, 22]



k = 1


k = 2

"""


https://livecode.amazon.jobs/session/aca517f3-53c6-4c69-befb-5236c3ae399f


The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example :
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
"""
import copy

class Board(object):
    def __init__(self, n):
        self.n = n
        self.horizontal = [0] * n
        self.vertical = [0] * n
        self.diag_up = [0] * (2*n - 1) # Tricky
        self.diag_down = [0] * (2*n - 1) # Tricky
        self.num_queens = 0
        
        self.visited = set([])
        
        self.complete_solutions = []
    
    def _set_queen(self, row, col, value):
        self.horizontal[row] = value
        self.vertical[col] = value
        self.diag_up[row + col] = value
        self.diag_down[n - row + col - 1] = value #Might need to double check this
    
    def add(self, row, col):
        self._set_queen(row, col, 1)
        self.num_queens = self.num_queens + 1
        self.visited.add((row, col))
        
        if self.num_queens == n:
            self.complete_solutions.append(copy.copy(self.visited))
    
    def remove(self, row, col):
        self._set_queen(row, col, 0)
        self.num_queens = self.num_queens - 1
        self.visited.remove((row, col))
    
    def is_valid(self, row, col):
        return all([
            self.horizontal[row] == 0
            self.vertical[col] == 0
            self.diag_up[row + col] == 0
            self.diag_down[n - row + col - 1] == 0
        ])
    
    def all_valid(self):
        valid = []
        for row in xrange(self.n):
            for col in xrange(self.n):
                if self.is_valid(row, col):
                    valid.append((row, col))
        return valid
    
    
        
def solution(n):
    board = Board(n)
    solutions(board)
    return len(board.complete_solutions)
    
        
def solutions(board):
    next_queens = board.all_valid()
    for row, col in next_queens:
        board.add(row, col)
        solutions(board)
        board.remove(row, col


"""
Implementation of Connect 4 game
"""

class Board(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.empty = '_'

        self.board = []

        for _ in xrange(self.rows):
            self.board.append(list(self.empty * self.cols))


    def print_board(self):
        for row in self.board:
            print ' '.join(row)


    def add_coin(self, column, coin):
        for row_index in xrange(self.rows - 1, -1, -1):
            if self.board[row_index][column] == self.empty:
                self.board[row_index][column] = coin
                break


    def row_winner(self, coin):
        for row in self.board:
            s = 0
            for col_index in xrange(self.cols):
                if row[col_index] == coin:
                    s = s + 1
                    if s == 4:
                        return True
                else:
                    s = 0
        return False


    def column_winner(self, coin):
        for column_index in xrange(self.cols):
            s = 0
            for row_index in xrange(self.rows):
                if self.board[row_index][column_index] == coin:
                    s = s + 1
                    if s == 4:
                        return True
                else:
                    s = 0
        return False


    def is_in_board(self, row, column):
        return row >= 0 and row < self.rows and column >= 0 and column < self.cols


    def diagonal_winner(self, coin):
        starting_points = []
        for row_index in xrange(self.rows):
            starting_points.append((row_index, 0, 'up'))

        for col_index in xrange(self.cols):
            starting_points.append((self.rows - 1, col_index, 'up'))

        for row_index in xrange(self.rows):
            starting_points.append((row_index, 0, 'down'))

        for col_index in xrange(self.cols):
            starting_points.append((0, col_index, 'down'))

        
        for point in starting_points:
            current_row = point[0]
            current_col = point[1]
            up_or_down = point[2]
            s = 0
            while True:
                if self.is_in_board(current_row, current_col):
                    if self.board[current_row][current_col] == coin:
                        s = s + 1
                        if s == 4:
                            return True
                    else:
                        s = 0
                    
                    if up_or_down == 'up':
                        current_row = current_row - 1
                        current_col = current_col + 1
                    else:
                        current_row = current_row + 1
                        current_col = current_col + 1
                else:
                    break

        return False


    def is_winner(self, coin):
        return self.row_winner(coin) or self.column_winner(coin) or self.diagonal_winner(coin)



class Game(object):
    def __init__(self, rows, cols):
        self.board = Board(rows, cols)

    def play(self):
        coin = 'O'
        while True:
            self.board.print_board()

            if self.board.is_winner(coin):
                print 'player {0} is the winner!'.format(coin)
                return

            if coin == 'X':
                coin = 'O'
            else:
                coin = 'X'

            column = int(input('Choose a column to add an {0}: '.format(coin)))
            self.board.add_coin(column, coin)
            

if __name__ == '__main__':
    Game(5,5).play()

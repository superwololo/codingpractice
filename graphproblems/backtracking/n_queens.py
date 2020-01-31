



class Availability(object):
    def __init__(self, N):
        self.N = N
        self.free_rows = [0] * N
        self.free_cols = [0] * N
        self.free_upper_diag = [0] * (2 * N - 1)
        self.free_lower_diag = [0] * (2 * N - 1)
        self.queen_indices = set([])

    def num_queens(self):
        return len(self.queen_indices)

    def set(self, row, col):
        self.queen_indices.add((row, col))
        self.free_rows[row] += 1
        self.free_cols[col] += 1
        self.free_upper_diag[row + col] += 1
        self.free_lower_diag[self.N - row - 1 + col] += 1

    def unset(self, row, col):
        self.queen_indices.remove((row, col))
        self.free_rows[row] -= 1
        self.free_cols[col] -= 1
        self.free_upper_diag[row + col] -= 1
        self.free_lower_diag[self.N - row - 1 + col] -= 1

    def is_free(self, row, col):
        return not any([
            self.free_rows[row] > 0,
            self.free_cols[col] > 0,
            self.free_upper_diag[row + col] > 0,
            self.free_lower_diag[self.N - row - 1 + col] > 0
        ])

    def all_free(self):
        free = []
        for row in xrange(self.N):
            for col in xrange(self.N):
                if self.is_free(row, col):
                    free.append((row, col))
        return free

    def print_availability(self):
        for row in xrange(self.N):
            line = []
            for col in xrange(self.N):
                if self.is_free(row, col):
                    line.append('1')
                else:
                    if (row, col) in self.queen_indices:
                        line.append('Q')
                    else:
                        line.append('0')
            print ' '.join(line)
        print ''


def find_n_queens(N):
    data = Availability(N)
    solution = []
    find_n_queens_inner(data, solution)


def find_n_queens_inner(data, solution):
    if len(solution) > 0:
        return
    if data.num_queens() == data.N:
        solution.append(True)
        data.print_availability()
    else:
        free_squares = data.all_free()
        for square in free_squares:
            data.set(square[0], square[1])
            find_n_queens_inner(data, solution)
            data.unset(square[0], square[1])


find_n_queens(8)





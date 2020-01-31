"""
https://www.geeksforgeeks.org/gold-mine-problem/
"""

import sys

grid = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]


def getIndex(grid, row, col, numRows, numCols):
    if row < 0 or row >= numRows:
        return -sys.maxint
    if col < 0 or col >= numCols:
        return -sys.maxint
    return grid[row][col]


def max_gold(grid):

    numRows = len(grid)
    numCols = len(grid[0])

    cache = []
    for index in xrange(numRows):
        cache.append([0] * numCols)
        cache[index][0] = grid[index][0]

    for column_index in xrange(1, numCols):
        for row_index in xrange(numRows):

            v = grid[row_index][column_index]

            m = max(
                getIndex(cache, row_index - 1, column_index - 1, numRows, numCols) + v,
                getIndex(cache, row_index, column_index - 1, numRows, numCols) + v,
                getIndex(cache, row_index + 1, column_index - 1, numRows, numCols) + v
            )
            cache[row_index][column_index] = m

    # get last column
    last_row = []
    for row_index in xrange(numRows):
        num = cache[row_index][-1]
        last_row.append(num)
        print cache[row_index]

    return max(last_row)

print max_gold(grid)

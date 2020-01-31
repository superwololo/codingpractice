import unittest


"""
Colorfill: Given a point in a grid of 1's and 0's, find how many one's surround the point.
"""

def fillCount(grid, row, col):
    numRows = len(grid)
    numCols = len(grid[0])
    pointsVisited = set([])
    return fillCountInner(grid, row, col, numRows, numCols, pointsVisited)
    


def fillCountInner(grid, row, col, numRows, numCols, pointsVisited):
    point = (row, col)
    if point in pointsVisited:
        return 0

    pointsVisited.add((row, col))

    if row < 0 or row >= numRows or col < 0 or col >= numCols:
        return 0
    elif grid[row][col] == 0:
        return 0
    else:
        left = fillCountInner(grid, row - 1, col, numRows, numCols, pointsVisited)
        right = fillCountInner(grid, row + 1, col, numRows, numCols, pointsVisited)
        up  = fillCountInner(grid, row, col - 1, numRows, numCols, pointsVisited)
        down = fillCountInner(grid, row, col + 1, numRows, numCols, pointsVisited)
        return 1 + left + right + up + down


class ColorTest(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

    def test_fillCount(self):
        self.assertEqual(fillCount(self.grid, 2, 1), 9)

    def test_empty_fillCount(self):
        self.assertEqual(fillCount(self.grid, 0, 0), 0)

    def test_not_in_grid(self):
        self.assertEqual(fillCount(self.grid, 10, 10), 0)

if __name__ == '__main__':
    unittest.main()

import unittest
import copy
import sys


"""
This is a BFS approach the problem with it is that copy is linear time so this is actually O(N^2)
"""
def travel(grid, startRow, startCol, endRow, endCol):
    queue = [[(startRow, startCol)]]
    visitedPoints = set([(startRow, startCol)])
    return travelInner(grid, endRow, endCol, len(grid), len(grid[0]), queue, visitedPoints)


def isValidPoint(grid, row, col, numRows, numCols, visitedPoints):
    return row >= 0 and row < numRows and col >= 0 and col < numCols and grid[row][col] == 1 and (row, col) not in visitedPoints

def travelInner(grid, endRow, endCol, numRows, numCols, queue, visitedPoints):
    endPoint = (endRow, endCol)
    
    while len(queue) > 0:
        path = queue.pop(0)
        point = path[-1]
        lastRow = point[0]
        lastCol = point[1]
        if lastRow == endRow and lastCol == endCol:
            return path
        else:
            if isValidPoint(grid, lastRow - 1, lastCol, numRows, numCols, visitedPoints):
                up = copy.copy(path)
                up.append((lastRow - 1, lastCol))
                queue.append(up)
                visitedPoints.add((lastRow - 1, lastCol))
            if isValidPoint(grid, lastRow + 1, lastCol, numRows, numCols, visitedPoints):
                down = copy.copy(path)
                down.append((lastRow + 1, lastCol))
                queue.append(down)
                visitedPoints.add((lastRow + 1, lastCol))
            if isValidPoint(grid, lastRow, lastCol - 1, numRows, numCols, visitedPoints):
                left = copy.copy(path)
                left.append((lastRow, lastCol - 1))
                queue.append(left)
                visitedPoints.add((lastRow, lastCol - 1))
            if isValidPoint(grid, lastRow, lastCol + 1, numRows, numCols, visitedPoints):
                right = copy.copy(path)
                right.append((lastRow, lastCol + 1))
                queue.append(right)
                visitedPoints.add((lastRow, lastCol + 1))


"""
This approach is O(N), at each point we find the next closest point
"""
def travel_min(grid, row, col, startRow, startCol):
    visited = copy.deepcopy(grid)
    for r in xrange(len(grid)):
        for c in xrange(len(grid[0])):
            visited[r][c] = None
    result = travel_min_inner(grid, row, col, startRow, startCol, visited, 1)

    return visited[startRow][startCol]


def travel_min_inner(grid, row, col, startRow, startCol, visited, weight):

    # Return if we've found a path to the start
    if row == startRow and col == startCol:
        visited[row][col] = weight
        return
    #Return if we are out of bounds
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return
    #Return if the path is not allowed
    if grid[row][col] == 0:
        visited[row][col] = -1
        return

    #Return if we've already visited this square
    if visited[row][col] != None:
        return

    visited[row][col] = weight
    travel_min_inner(grid, row + 1, col, startRow, startCol, visited, weight + 1)
    travel_min_inner(grid, row - 1, col, startRow, startCol, visited, weight + 1)
    travel_min_inner(grid, row, col + 1, startRow, startCol, visited, weight + 1)
    travel_min_inner(grid, row, col - 1, startRow, startCol, visited, weight + 1)



def is_valid_point(grid, row, col, path):
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1 and (row, col) not in path



class PointAndPrev(object):
    def __init__(self, curr_row, curr_col, prev_row, prev_col):
        self.curr_row = curr_row
        self.curr_col = curr_col
        self.prev_row = prev_row
        self.prev_col = prev_col

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.curr_row, self.curr_col, self.prev_row, self.prev_col)


    def __repr__(self):
        return str(self)


def travel_bfs(grid, startRow, startCol, endRow, endCol):
    path = {}

    first_elem = PointAndPrev(startRow, startCol, startCol, startCol)

    queue = [first_elem]

    # Perform a breadth first traversal
    while len(queue) > 0:
        next_elem = queue.pop(0)
        next_row = next_elem.curr_row
        next_col = next_elem.curr_col

        print next_row, next_col

        if is_valid_point(grid, next_row, next_col, path):

            # Add to path
            path[(next_row, next_col)] = (next_elem.prev_row, next_elem.prev_col)

            # Check if we've reached the end
            if next_row == endRow and next_col == endCol:
                break

            #append all the next elements
            queue.append(PointAndPrev(next_row, next_col + 1, next_row, next_col))
            queue.append(PointAndPrev(next_row, next_col - 1, next_row, next_col))
            queue.append(PointAndPrev(next_row + 1, next_col, next_row, next_col))
            queue.append(PointAndPrev(next_row - 1, next_col, next_row, next_col))

    reverse_path = []
    current_row = endRow
    current_col = endCol

    if (current_row, current_col) not in path:
        return []

    while (current_row, current_col) != (startRow, startCol):
        reverse_path.append((current_row, current_col))
        (current_row, current_col) = path[(current_row, current_col)]
    reverse_path.append((startRow, startCol))
    
    return reverse_path[::-1]


class TravelGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1]
        ]

    def test_travel(self):
        self.assertEqual(
            travel(self.grid, 0, 0, 4, 4),
            [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]
        )

    def test_travel_min(self):
        self.assertEqual(
            travel_min(self.grid, 4, 4, 0, 0),
            9
        )

    def test_travel_bfs(self):
        self.assertEqual(
            travel_bfs(self.grid, 0, 0, 4, 4),
            [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]
        )


if __name__ == '__main__':
    unittest.main()

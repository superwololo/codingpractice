import sys


class SubSegment(object):
    def __init__(self, start_index, end_index, value):
        self.start_index = start_index
        self.end_index = end_index
        self.value = value


class Rectangle(object):
    def __init__(self, grid):
        self.grid = grid
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])


def max_subsegment(arr):
    cache = [None] * len(arr)

    first_elem = SubSegment(0, 0, arr[0])
    cache[0] = first_elem

    max_value = first_elem

    for index in xrange(1, len(arr)):
        
        # Case 1: just the last element
        a = SubSegment(index, index, arr[index])
        b = SubSegment(cache[index - 1].start_index, index, cache[index - 1].value + arr[index])
        
        if a > b:
            cache[index] = a
        else:
            cache[index] = b

        #Finally set the new max value
        if cache[index].value > max_value.value:
            max_value = cache[index]

    return max_value


def max_subrectangle(rect):

    max_value = -sys.maxint

    for left_index in xrange(rect.num_cols):

        temp_array = [0] * rect.num_rows

        for right_index in xrange(left_index, rect.num_cols):
            
            # Construct temp array
            for row_index in xrange(rect.num_rows):
                temp_array[row_index] = temp_array[row_index] + rect.grid[row_index][right_index]
            
            value = max_subsegment(temp_array)
            if value > max_value:
                max_value = value


import unittest

class KadaneTest(unittest.TestCase):
    def test_max_subsegment(self):
        arr = [-1, -2, 4, -1, 5, -2]
        max_value = max_subsegment(arr)
        self.assertEqual(max_value.value, 8)
        self.assertEqual(max_value.start_index, 2)
        self.assertEqual(max_value.end_index, 4)


if __name__ == '__main__':
    unittest.main()

"""
https://www.geeksforgeeks.org/largest-rectangular-sub-matrix-whose-sum-0/
"""

grid = [
    [9, 7, 16, 5],
    [1, -6, -7, 3],
    [1, 8, 7, 9],
    [7, -2, 0, 10]
]





arr = [2, 1, 3, 2, -5, 6, -6, 7, 10]




def max_zero_array(arr):
    lookup = {}
    s = 0
    max_len = 0
    start_index = -1
    end_index = -1
    for index in xrange(len(arr)):
        s += arr[index]
        if s in lookup:
            print s, index, lookup
            if index - lookup[s] > max_len:
                max_len = index - lookup[s]
                start_index = lookup[s] + 1
                end_index = index
        else:
            lookup[s] = index
    
    return max_len, start_index, end_index
        

print max_zero_array(arr)

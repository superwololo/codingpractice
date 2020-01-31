"""
https://www.geeksforgeeks.org/divide-the-array-in-k-segments-such-that-the-sum-of-minimums-is-maximized/

Note: I ended up just implementing the painter problem here

"""

arr = [5, 7, 4, 2, 8, 1, 6]
k = 3



import sys


def min_max(arr, k):
    return min_max_inner(arr, k, 0, {})


def min_max_inner(arr, k, start_index, lookup):

    if (k, start_index) in lookup:
        return lookup[(k, start_index)]

    if k < 0:
        return sys.maxint

    if start_index == len(arr):
        if k == 0:
            return 0
        else:
            return sys.maxint

    print k, start_index
    
    s = 0
    res = sys.maxint
    for index in xrange(start_index, len(arr)):
        s = s + arr[index]
        tmp = max(s, min_max_inner(arr, k-1, index+1, lookup))
        if tmp < res:
            res = tmp

    lookup[(k, start_index)] = res
    
    return res
    
    

    

print min_max(arr, k)

"""
https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
"""

"""
Note: This solution doesn't leverage dynamic programming
"""

import copy

arr = [2, 3, 5, 6, 8, 10]
s = 10

def subset_sum(arr, s):
    subsets = []
    subset_sum_inner(arr, s, 0, [], subsets)
    for subset in subsets:
        print subset

def subset_sum_inner(arr, s, index, subset, subsets): 
    if index == len(arr):
        if s == 0:
            subsets.append(copy.copy(subset))
    else:
        # Option A : element is part of subset
        subset.append(arr[index])
        subset_sum_inner(arr, s - arr[index], index + 1, subset, subsets)
        subset.pop()

        # Option B : element is not part of subset
        subset_sum_inner(arr, s, index + 1, subset, subsets)


subset_sum(arr, s)

"""
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
"""

arr = [3, 34, 4, 12, 5, 2]
arr_sum = 9


def isSum(arr, arr_sum, index, cache):
    
    # check cache
    if (arr_sum, index) in cache:
        return cache[(arr_sum, index)]

    # base case
    if arr_sum == 0:
        return True
    if arr_sum < 0 or index >= len(arr):
        return False

    # option A: index is included
    option_a = isSum(arr, arr_sum - arr[index], index+1, cache)

    # option B: index is not included:
    option_b = isSum(arr, arr_sum, index + 1, cache)

    cache[(arr_sum, index)] = option_a or option_b

    return cache[(arr_sum, index)]


print isSum(arr, arr_sum, 0, {})

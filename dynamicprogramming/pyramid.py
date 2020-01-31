"""
https://www.geeksforgeeks.org/pyramid-form-increasing-decreasing-consecutive-array-using-reduce-operations/
"""
import sys


arr = [1, 2, 3, 4, 2, 1]



def pyramid_down(arr, index, prev_height):
    if index == len(arr):
        return 0

    if prev_height == 0:
        return arr[index] + pyramid_down(arr, index+1, 0)

    if arr[index] < prev_height - 1:
        return sys.maxint

    #Finally just shave to be one less than prior
    return arr[index] - prev_height + 1 + pyramid_down(arr, index+1, prev_height - 1)


def pyramid_up(arr, index, prev_height):
    if index == len(arr):
        return sys.maxint

    # We can always shave down to zero
    option_a = sys.maxint
    if prev_height == 0:
        option_a = arr[index] + pyramid_up(arr, index+1, 0)

    
    if arr[index] < prev_height + 1:
        return sys.maxint

    option_b = arr[index] - prev_height - 1 + pyramid_up(arr, index+1, prev_height + 1)
    option_c = arr[index] - prev_height - 1 + pyramid_down(arr, index+1, prev_height+1)

    return min(option_a, option_b, option_c)


def pyramid(arr):
    return pyramid_up(arr, 0, 0)



print pyramid(arr)

"""
https://www.geeksforgeeks.org/subset-sum-divisible-m/
"""

"""

# Notes: I wasn't able to solve this one

arr = [3, 1, 7, 5]
m = 6

def subset_m(arr, m):
    return subset_m_inner(arr, 0, m, m)

def subset_m_inner(arr, index, m, original_m):

    if index >= len(arr):
        return m == original_m

    # option A: index is part of subset
    
    new_m = m - arr[index] % m
    if new_m == 0:
        new_m = original_m
    option_a = subset_m_inner(arr, index + 1, new_m, original_m)
    
    # option B: index is not part of subset
    option_b = subset_m_inner(arr, index + 1, m, original_m)

    if option_a % m == 0:
        return True
    elif option_b % m == 0:
        return True
    else:
        return False

print subset_m(arr, m)
"""

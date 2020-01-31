"""
https://www.geeksforgeeks.org/permutation-coefficient/
"""

# This was given to us
# P(n, k) = P(n-1, k) + k* P(n-1, k-1) 

def P(n, k):
    return P_inner(n, k, {})


def P_inner(n, k, cache):
    
    if (n, k) in cache:
        return cache[(n, k)]

    if n == 0 or k == 0:
        return 0
    
    if k == 1:
        return n

    s = P_inner(n-1, k, cache) + k * P_inner(n-1, k-1, cache)

    cache[(n, k)] = s

    return s


print P(10, 2) # 90
print P(10, 3) # 720
print P(10, 0) # 1
print P(10, 1) # 10

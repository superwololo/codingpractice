"""
https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
"""

# number of ways k objects chosen from among n objects
def C(n, k):
    return C_inner(n, k, {})


def C_inner(n, k, cache):
    
    if (n, k) in cache:
        return cache[(n, k)]

    if n == 0:
        return 1

    if k == 0:
        return 0

    # option A: nth object chosen
    option_a = C_inner(n-1, k-1, cache)

    # option B: nth object not chosen
    option_b = C_inner(n-1, k, cache)

    cache[(n, k)] = option_a + option_b

    return cache[(n, k)]



print C(5, 2)

"""
https://www.geeksforgeeks.org/tiling-problem/
"""

# board is of size n

def tiling(n, cache):

    if n in cache:
        return cache[n]

    if n == 0:
        return 1
    if n == 1:
        return 1
    
    # Option A : place tile vertically
    option_a = tiling(n-1, cache)

    # Option B : place two horizontal tiles
    option_b = tiling(n-2, cache)
    
    cache[n] = option_a + option_b

    return option_a + option_b


print tiling(1, {})
print tiling(2, {})
print tiling(3, {})
print tiling(4, {})

"""
https://www.geeksforgeeks.org/friends-pairing-problem/
"""

def pair(n, cache):
    
    if n in cache:
        return cache[n]

    if n <= 0:
        return 1
    if n == 1:
        return 1

    # Option A: Friend is unpaired
    option_a = pair(n - 1, cache)

    # Option B: Friend is paired
    option_b = (n - 1) * pair(n - 2, cache)

    cache[n] = option_a + option_b

    return option_a + option_b


print pair(1, {})
print pair(2, {})
print pair(3, {})
print pair(4, {})

"""
https://www.geeksforgeeks.org/count-number-of-ways-to-arrange-first-n-numbers/
"""

import copy
# Brute force first

def count(n):
    
    arr = range(2, n+1)
    available = set(arr)

    path = [1]
    all_paths = []

    count_inner(available, path, all_paths)

    return all_paths


def option(elem, available, path, all_paths):
    if elem in available:
        available.remove(elem)
        path.append(elem)
        count_inner(available, path, all_paths)
        path.pop()
        available.add(elem)


def count_inner(available, path, all_paths):

    if len(available) == 0:
        all_paths.append(copy.copy(path))
        return
    
    elem = path[-1]

    # Option A : Increment by one
    option(elem+1, available, path, all_paths)

    # Option B : Increment by two
    option(elem+2, available, path, all_paths)

    # Option C : Decrement by one
    option(elem-1, available, path, all_paths)

    # Option D : Decrement by two
    option(elem-2, available, path, all_paths)


print count(4)

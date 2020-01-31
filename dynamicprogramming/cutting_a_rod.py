"""
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
"""

import sys

price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
cache = {}

def cut_price_inner(price, n, index, cache):
    
    if (n, index) in cache:
        return cache[(n, index)]

    if n == 0 and index == 0:
        return 0
    elif n == 0:
        return -sys.maxint

    # Option 1: Cut
    option1 = cut_price_inner(price, n - 1, 0, cache)

    # Option 2: Don't cut
    option2 = cut_price_inner(price, n - 1, index + 1, cache)

    res =  max(option1 + price[index], option2)
    cache[(n, index)] = res
    return res


def cut_price(price, n):
    cache = {}
    return cut_price_inner(price, n, 0, cache)


print cut_price(price, n)

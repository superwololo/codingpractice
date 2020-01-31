"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
"""
import sys

value = [60, 100, 120]
weight = [10, 20, 30]
W = 50


def knapsack(value, weight, W, index, cache):

    if (W, index) in cache:
        return cache[(W, index)]

    if W < 0:
        return -sys.maxint
    if index == len(value):
        return 0
    else:
        # Option A : Element is in knapsack
        option_a = value[index] + knapsack(value, weight, W - weight[index], index+1, cache)

        # Option B : Element is not in knapsack
        option_b = knapsack(value, weight, W, index+1, cache)

        cache[(W, index)] = max(option_a, option_b)

        return cache[(W, index)]


print knapsack(value, weight, W, 0, {})

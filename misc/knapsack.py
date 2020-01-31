import copy

"""
Solve knapsack problem
"""

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50


def knapsack_inner(values, weights, remaining_capacity, existing_value):
    values_copy = copy.copy(values)
    weights_copy = copy.copy(weights)

    if len(values_copy) == 0:
        return existing_value

    value = values_copy.pop(0)
    weight = weights_copy.pop(0)

    larger = 0
    if weight <= remaining_capacity:
        larger = knapsack_inner(values_copy, weights_copy, remaining_capacity - weight, existing_value + value)

    smaller = knapsack_inner(values_copy, weights_copy, remaining_capacity, existing_value)

    return max(smaller, larger)

def knapsack(values, weights, capacity):
    return knapsack_inner(values, weights, capacity, 0)


print knapsack(values, weights, W)

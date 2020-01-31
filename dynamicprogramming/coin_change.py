"""
https://www.geeksforgeeks.org/coin-change-dp-7/
"""

import copy

N = 4
S = [1,2,3]


def coins(S, N):
    counters = [0] * len(S)
    cache = {}
    return coins_inner(counters, S, N, 0, cache)


def coins_inner(counters, S, N, M, cache):
    if (N, M) in cache:
        return cache[(N, M)]
    if N == 0:
        return [copy.copy(counters)]
    if N < 0 or M >= len(S):
        return []

    # Option A: Increment the Mth counter
    counters[M] = counters[M] + 1
    res1 = coins_inner(counters, S, N - S[M], M, cache)
    counters[M] = counters[M] - 1

    # Option B: Move to next counter
    res2 = coins_inner(counters, S, N, M+1, cache)
    res1.extend(res2)

    cache[(N, M)] = copy.copy(res1)

    return res1

print coins(S, N)

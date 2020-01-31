"""
https://www.geeksforgeeks.org/count-ofdifferent-ways-express-n-sum-1-3-4/
"""

# Note that I expanded the question to include the paths, but to do this I removed the caching



import copy

def ways(N):
    solutions = []
    res = ways_inner(N, [-1] * (N+1), [], solutions)

    print "SOLUTIONS"
    for s in solutions:
        print " + ".join(s)
    print ""

    return res

def ways_inner(N, cache, solution, solutions):
    if N == 0:
        solutions.append(copy.copy(solution))
        return 1
    if N < 0:
        return 0

    solution.append("1")
    option_a = ways_inner(N-1, cache, solution, solutions)
    solution.pop()

    solution.append("3")
    option_b = ways_inner(N-3, cache, solution, solutions)
    solution.pop()

    solution.append("4")
    option_c = ways_inner(N-4, cache, solution, solutions)
    solution.pop()

    cache[N] = option_a + option_b + option_c

    return cache[N]

print ways(1)
print ways(2)
print ways(3)
print ways(4)
print ways(5)

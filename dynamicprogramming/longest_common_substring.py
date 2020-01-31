"""
https://www.geeksforgeeks.org/longest-common-substring-dp-29/
"""

a = "TheGeeksforGeeks" 
b = "AGeeksQuiz"

import sys

def extract_string(cache):
    row = cache[0]
    v = sys.maxint
    s = []

    for weight, char in row:
        if weight < v:
            v = weight
            s.append(char)
    
    return "".join(s)

def longest_substring(a, b):
    cache = []
    for row in xrange(len(a)):
        cache.append([(-1, "")]*len(b))

    res = substring_inner(a, b, 0, 0, cache)
    
    print "CACHE"
    for row in cache:
        print row
    print ""

    return res[0], extract_string(cache)


def substring_inner(a, b, a_index, b_index, cache):

    if a_index == len(a) or b_index == len(b):
        return (0, "")

    if cache[a_index][b_index][0] != -1:
        return cache[a_index][b_index]

    if a[a_index] == b[b_index]:
        v = 1 + substring_inner(a, b, a_index + 1, b_index + 1, cache)[0]
        cache[a_index][b_index] = (v, a[a_index])
        return cache[a_index][b_index]

    option_a = substring_inner(a, b, a_index + 1, b_index, cache)
    option_b = substring_inner(a, b, a_index, b_index + 1, cache)
    
    cache[a_index][b_index] = max(option_a, option_b, lambda x:x[0])

    return cache[a_index][b_index]

print longest_substring(a, b)

"""
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
"""
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


def subsequence_length(a, b):
    cache = []
    for row in xrange(len(a)):
        cache.append([(-1, "")] * len(b))

    res = subsequence_length_inner(a, b, 0, 0, cache)

    print "CACHE: "
    for row in cache:
        print row
    print ""

    return res[0], extract_string(cache)


def subsequence_length_inner(a, b, a_index, b_index, cache):

    if a_index == len(a) or b_index == len(b):
        return (0, "")

    if cache[a_index][b_index][0] != -1:
        return cache[a_index][b_index]
    
    # Option a : both terms match
    option_a = (0, "")
    if a[a_index] == b[b_index]:
        option_a = (1 + subsequence_length_inner(a, b, a_index + 1, b_index + 1, cache)[0], a[a_index])

    # Option b : increase a index
    option_b = subsequence_length_inner(a, b, a_index + 1, b_index, cache)

    # Option c : increase b index
    option_c = subsequence_length_inner(a, b, a_index, b_index + 1, cache)

    cache[a_index][b_index] = max(option_a, option_b, option_c, key=lambda x:x[0])

    return cache[a_index][b_index]


print subsequence_length("ABCDGH", "AEDFHR")
print subsequence_length("AGGTAB", "GXTXAYB")

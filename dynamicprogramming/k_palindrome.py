"""
https://www.geeksforgeeks.org/find-if-string-is-k-palindrome-or-not/
"""


string = "abcdecbaf"
k = 0


def palindrome(string, i, j, cache):

    if (i, j) in cache:
        return cache[(i, j)]

    if i >= j:
        return 0

    v = 0
    if string[i] == string[j]:
        v = palindrome(string, i+1, j-1, cache)
    else:
        v = 1 + min(palindrome(string, i+1, j, cache), palindrome(string, i, j-1, cache))

    cache[(i, j)] = v
    return v

print palindrome(string, 0, len(string) - 1, {})

"""
https://www.geeksforgeeks.org/longest-repeated-subsequence/
"""


s = "aabebcdd"

"""
def longest_repeated(s):
    return longest_repeated_inner(s, 0, [], [])


def longest_repeated_inner(s, index, prefix_a, prefix_b):
    
    if index == len(s):
        if str(prefix_a) == str(prefix_b):
            return "".join(prefix_a)
        else:
            return ""
    else:
        # Option A : we ignore the character at this index
        option_a = longest_repeated_inner(s, index + 1, prefix_a, prefix_b)
        
        # Option B : character at this index is added to string a
        prefix_a.append(s[index])
        option_b = longest_repeated_inner(s, index + 1, prefix_a, prefix_b)
        prefix_a.pop()

        # Option C : character at this index is added to string b
        prefix_b.append(s[index])
        option_c = longest_repeated_inner(s, index + 1, prefix_a, prefix_b)
        prefix_b.pop()

        return max([option_a, option_b, option_c], key=lambda x:len(x))

print longest_repeated(s)
"""

"""

longest(i, j) represents the longest substring that can be formed ending with index i, j

  a a b e b c d d
a 0 1 1 1 1 1 1 1       
a   1 1 1 1 1 1 1
b     1 1 2 2 2 2
e       1 2 2 2 2
b         2 2 2 2
c           2 2 2
d             2 3
d               3

longest(0, 1) = 1

"""



def longest_repeated(s, index_a, index_b):
    pass

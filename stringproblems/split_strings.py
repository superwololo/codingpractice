
"""
Determine if we can validly split a string into substring
"""

dictionary = {"i", "like", "sam", "sung", "samsung"}

def can_split(string, dictionary):
    return can_split_inner(string, "", dictionary, {})



def can_split_inner(string, prefix, dictionary, cache):

    if (string, prefix) in dictionary:
        return cache[(string, prefix)]

    if len(string) == 0:
        if prefix in dictionary:
            return True
        else:
            return False

    res = any([
        can_split_inner(string[1::], prefix + string[0], dictionary, cache),
        prefix + string[0] in dictionary and can_split_inner(string[1::], "", dictionary, cache)
    ])
    
    cache[(string, prefix)] = res

    return res




print can_split("ilikesamsung", dictionary)

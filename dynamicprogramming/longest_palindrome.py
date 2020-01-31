
string = "forgeeksskeegfor"


def palindrome(string):
    lookup = []
    for _ in string:
        lookup.append([None] * len(string))

    find_palindrome(string, 0, len(string)-1, lookup)

    max_size = -1
    start = -1
    finish = -1

    for row_index in xrange(len(lookup)):
        for column_index in xrange(len(lookup[row_index])):
            if lookup[row_index][column_index] == True:
                if column_index-row_index+1 > max_size:
                    max_size = column_index-row_index+1
                    start = row_index
                    finish = column_index

    return string[start:finish+1]


def find_palindrome(string, start, finish, lookup):
    if lookup[start][finish] != None:
        return lookup[start][finish]

    if start >= finish:
        lookup[start][finish] = True
        return True

    is_palindrome = False
    if string[start] == string[finish]:
        is_palindrome = find_palindrome(string, start+1, finish-1, lookup)
        lookup[start][finish] = is_palindrome
    else:
        lookup[start][finish] = False
        
    lookup[start+1][finish] = find_palindrome(string, start+1, finish, lookup)
    lookup[start][finish-1] = find_palindrome(string, start, finish-1, lookup)

    return is_palindrome


palindrome(string)

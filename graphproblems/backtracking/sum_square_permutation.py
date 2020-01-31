import copy


def all_required_squares(number):
    s = number + number - 1
    
    squares = set([])

    counter = 0
    maximum = -1

    while maximum < s:
        counter = counter + 1
        squares.add(counter * counter)
        maximum = counter * counter
    return squares

def sum_square_array(number):
    arr = range(1, number+1)

    squares = all_required_squares(number)

    solutions = []
    for index in xrange(len(arr)):
        sum_square_array_inner(arr, [arr[index]], set([index]), solutions, squares)
    return solutions


def sum_square_array_inner(arr, prefix, visited_indices, solutions, squares):
    
    if len(prefix) == len(arr):
        solutions.append(copy.copy(prefix))
    else:
        # Get all possible next numbers
        # Call recursion
        for index in xrange(len(arr)):
            if index not in visited_indices:
                if arr[index] + prefix[-1] in squares:
                    visited_indices.add(index)
                    prefix.append(arr[index])
                    sum_square_array_inner(arr, prefix, visited_indices, solutions, squares)
                    visited_indices.remove(index)
                    prefix.pop()
    


solutions = sum_square_array(17)

for s in solutions:
    print s



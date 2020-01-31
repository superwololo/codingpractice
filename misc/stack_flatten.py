arr = [1, 3, 5, [0, 5, 10, [11], 4], [2, 1], 4]


def flatten(arr):
    soln = []
    stack = []

    stack.append(arr)

    while len(stack) > 0:
        elem = stack.pop()
        
        while len(elem) > 0:
            if isinstance(elem[0], int):
                soln.append(elem[0])
                elem.pop(0)
            else:
                p = elem.pop(0)
                stack.append(elem)
                stack.append(p)
                break
    return soln


def flatten2(arr):
    soln = []
    stack = arr[::-1]

    while len(stack) > 0:
        elem = stack.pop()
        if isinstance(elem, int):
            soln.append(elem)
        else:
            stack.extend(elem[::-1])
    return soln


import copy
print flatten(copy.deepcopy(arr))
print flatten2(arr)

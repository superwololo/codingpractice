
arr = [1, 4, 6, 7, 12, 14]


def find(arr, v):
    return find_inner(arr, v, 0, len(arr))


def find_inner(arr, v, low, high):

    if low >= high:
        if arr[low] == v:
            return low
        else:
            None
    
    if low + 1 == high:
        if arr[low] == v:
            return low
        if arr[high] == v:
            return high
        return None

    target = (low + high) / 2
    
    if arr[target] == v:
        return target

    if v > arr[target]:
        return find_inner(arr, v, target, high)
    else:
        return find_inner(arr, v, low, target)


print find(arr, 8)

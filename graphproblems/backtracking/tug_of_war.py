

"""
To implement tug of war I will just create all array combinations, and then return the minimum array
"""

def min_cut(arr, arr1, arr2, arr_1_max, arr_2_max, index):
    
    if len(arr1) < arr_1_max and len(arr2) < arr_2_max:
        arr1.append(arr[index])
        option1 = min_cut(arr, arr1, arr2, arr_1_max, arr_2_max, index + 1)
        arr1.pop()
        
        arr2.append(arr[index])
        option2 = min_cut(arr, arr1, arr2, arr_1_max, arr_2_max, index + 1)
        arr2.pop()
        return min(option1, option2)

    elif len(arr1) < arr_1_max:
        arr1.append(arr[index])
        value = min_cut(arr, arr1, arr2, arr_1_max, arr_2_max, index + 1)
        arr1.pop()
        return value

    elif len(arr2) < arr_2_max:
        arr2.append(arr[index])
        value = min_cut(arr, arr1, arr2, arr_1_max, arr_2_max, index + 1)
        arr2.pop()
        return value

    else:
        return abs(sum(arr1) - sum(arr2))


def solve_min_cut(arr):
    arr_1_max = len(arr) / 2
    arr_2_max = len(arr) - arr_1_max
    return min_cut(arr, [], [], arr_1_max, arr_2_max, 0)


print solve_min_cut([3, 4, 5, -3, 100, 1, 89, 54, 23, 20])
print solve_min_cut([23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4])
print solve_min_cut([])





arr = [3, 2, 1, 3, 1, 1, 1]


def make_subarrays(arr, start_index, target):
    curr_value = 0
    for index in xrange(start_index, len(arr)):
        curr_value = curr_value + arr[index]


def subarrays(arr):
    target = 0
    for index in xrange(len(arr)):
        target = target + arr[index]
        make_subarrays(arr, index + 1, target)


subarrays(arr)

import unittest


"""
Implementation of quicksort. Note that this isn't an in-place sort with the current implementation
"""
def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) / 2
    pivot_value = arr[pivot_index]

    a1 = []
    a2 = []
    same_value = []

    for elem in arr:
        if elem < pivot_value:
            a1.append(elem)
        elif elem > pivot_value:
            a2.append(elem)
        else:
            same_value.append(elem)

    a1_sorted = quicksort(a1)
    a2_sorted = quicksort(a2)

    a1_sorted.extend(same_value)
    a1_sorted.extend(a2_sorted)
    return a1_sorted


class QuickSortTest(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(
            quicksort([1, 5, 2, 3, 4]),
            [1, 2, 3, 4, 5]
        )


if __name__ == '__main__':
    unittest.main()

import unittest


"""
implementation of mergesort
"""
def merge_two_sorted_arrays(a1, a2):
    res = []
    while True:
        if len(a1) == 0 and len(a2) == 0:
            return res
        if len(a1) == 0:
            res.extend(a2)
            return res
        if len(a2) == 0:
            res.extend(a1)
            return res
        elif a1[0] < a2[0]:
            res.append(a1.pop(0))
        elif a1[0] >= a2[0]:
            res.append(a2.pop(0))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        half = len(arr) / 2
        a1 = arr[:half:]
        a2 = arr[half::]
        return merge_two_sorted_arrays(merge_sort(a1), merge_sort(a2))



class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.arr = [5, 1, 3, 2, 4]

    def test_merge_sort(self):
        self.assertEqual(
            merge_sort(self.arr),
            [1, 2, 3, 4, 5]
        )

    def test_merge_two_sorted_arrays(self):
        self.assertEqual(
            merge_two_sorted_arrays([1, 3, 5], [2, 4]),
            [1, 2, 3, 4, 5]
        )


if __name__ == '__main__':
    unittest.main()

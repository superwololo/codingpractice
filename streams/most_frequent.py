"""
https://www.geeksforgeeks.org/find-top-k-or-most-frequent-numbers-in-a-stream/
"""
import heapq

arr = [5, 2, 1, 3, 2]
k = 4

def most_frequent(arr, k):
    counter = {}
    heap = []
    heap_elements = set()
    soln = []

    for elem in arr:
        if elem not in counter:
            counter[elem] = 0
        counter[elem] = counter[elem] + 1

        if len(heap) < k:
            heapq.heappush(heap, (counter[elem], elem))
            heap_elements.add(elem)
        else:
            
            
        

    return ' '.join(map(lambda x: str(x), soln))

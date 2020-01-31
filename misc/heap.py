import heapq


li = [5, 7, 9, 1, 3]


heapq.heapify(li)
heapq.heappush(li, 4)

print li

heapq.heappop(li, 4)
print li

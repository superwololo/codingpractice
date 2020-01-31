"""
https://www.geeksforgeeks.org/reservoir-sampling/
"""
from random import randint


arr = range(1,101)


def sample(arr, k):
    samples = []
    
    for index in xrange(len(arr)):
        if len(samples) < k:
            samples.append(arr[index])
        else:
            r = randint(0, index)
            if r < k:
                samples[r] = arr[index]

    return samples



print sample(arr, 3)

"""
https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/
"""

def num_partitions(num_elements):
    return num_partitions_inner(num_elements, 1, {})


def num_partitions_inner(num_elements, existing_partitions, cache):
    
    if (num_elements, existing_partitions) in cache:
        return cache[(num_elements, existing_partitions)]

    if num_elements == 1 or num_elements == 0:
        return 1

    # Option A: append to all existing partitions
    option_a = num_partitions_inner(num_elements - 1, existing_partitions, cache) * existing_partitions

    # Option B: create a new partition
    option_b = num_partitions_inner(num_elements - 1, existing_partitions+1, cache)

    cache[(num_elements, existing_partitions)] = option_a + option_b

    return cache[(num_elements, existing_partitions)]


for index in xrange(7):
    print num_partitions(index)

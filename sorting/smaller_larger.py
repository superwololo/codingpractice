
print 'hello, smaller/larger!'


arr = [12, 1, 2, 3, 0, 11, 4]


def smaller_larger(arr):
    pairs = zip(arr, range(len(arr)))
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    smaller = [0] * len(arr)
    larger = [0] * len(arr)
    
    for index in xrange(len(sorted_pairs)):
        num_larger = len(arr) - index - 1
        num_smaller = index

        insert_index = sorted_pairs[index][1]

        print sorted_pairs[index]

        smaller[insert_index] = num_smaller
        larger[insert_index] = num_larger

    return smaller, larger


print smaller_larger(arr)

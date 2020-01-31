


boards = [1, 5, 2, 7, 6, 2, 4, 6, 2]

K = 3


"""
        0   1   2   3   4   5   6   7   8
K = 1   1   6   8   15  21  23  27  -1  -1
K = 2   -1  5
K = 3

"""



def split(boards, K):
    cache = []
    for index in xrange(K):
        cache.append([-1]*len(boards))

    

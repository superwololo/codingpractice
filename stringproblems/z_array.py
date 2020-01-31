




def construct_z_array(string):
    z_array = [None] * len(string)

    L = 0
    R = 0

    for index in xrange(1, len(string)):

        # In this case we want to reset the L and R indices
        if index > R:
            L = index
            R = index
            
            while string[R] == string[R - L]:
                R  = R + 1
            z_array[index] = R - L

        else:
            k = index - L
            z_array[index] = z_array[k]

        print index, string[index]

    return z_array


print construct_z_array("aabcaabxaaaz")





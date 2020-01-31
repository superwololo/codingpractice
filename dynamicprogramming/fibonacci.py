
"""
https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""

def fibonacci(n):
    fib_array = [0, 1]
    
    if n == 0 or n == 1:
        return fib_array[n]
    else:
        while True:
            s = fib_array[-1] + fib_array[-2]
            fib_array.append(s)
            if len(fib_array) == n + 1:
                return fib_array[-1]

# 10th element of fibonacci sequence is 55
print fibonacci(10)


"""
https://www.geeksforgeeks.org/print-fibonacci-sequence-using-2-variables/
"""

def fibonacci2(n):
    
    fib1 = 0
    fib2 = 1

    if n == 0:
        return fib1
    if n == 1:
        return fib2
    
    counter = 1
    while counter < n:
        
        fib3 = fib1 + fib2
        
        # shift over
        fib1 = fib2
        fib2 = fib3

        counter += 1

    return fib2

# 10th element of fibonacci sequence is 55
print fibonacci2(10)


"""
https://www.geeksforgeeks.org/print-fibonacci-series-reverse-order/
"""

def reverse_fibonacci(n):
    fib_array = [0, 1]
    
    if n == 0 or n == 1:
        return fib_array[n]
    else:
        while True:
            s = fib_array[-1] + fib_array[-2]
            fib_array.append(s)
            if len(fib_array) == n + 1:
                return fib_array[::-1]

print reverse_fibonacci(10)




a = range(4, 0, -1)
b = []
c = []


print a, b, c


def move(rod_a, rod_b):
    elem = rod_a.pop()
    rod_b.append(elem)


def hanoi(n, a, b, c):
    if n == 1:
        move(a, c)
        print a, b, c
    else:
        hanoi(n-1, a, c, b) # Move to middle rod
        move(a, c)
        print a, b, c
        hanoi(n-1, b, a, c) # Move to end rod


hanoi(4, a, b, c)
print a, b, c

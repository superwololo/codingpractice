class Elem(object):
    def __init__(self, value, next_value):
        self.next_value = next_value
        self.value = value

    def print_all(self):
        print self.value
        if self.next_value:
            self.next_value.print_all()
            


D = Elem('D', None)
C = Elem('C', D)
B = Elem('B', C)
A = Elem('A', B)


"""
Reverse a linked list
"""
def reverse(first_elem):
    prev = None
    current = first_elem
    while current:
        next = current.next_value
        current.next_value = prev
        prev = current
        current = next

reverse(A)
D.print_all()

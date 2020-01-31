"""
https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/
"""
import unittest


symbol = ['T', 'F', 'T']
operator = ['^', '&']




def parens(expr):
    
    index = 0
    counter = 0
    
    while True:
        if expr[index] == '(':
            counter += 1
        if expr[index] == ')':
            counter -= 1
        
        if counter == 0:
            return expr[1:index]

        index += 1


def evaluate(expr):
    index = 0
    stack = []
    while index < len(expr):
        if expr[index] == 'T':
            stack.append(True)
        elif expr[index] == 'F':
            stack.append(False)
        elif expr[index] == '&':
            stack.append('&')
        elif expr[index] == '|':
            stack.append('|')
        elif expr[index] == '^':
            stack.append('^')
        elif expr[index] == '(':
            expr_a = parens(expr[index::])
            stack.append(evaluate(expr_a))
            index += len(expr_a) + 1

        index += 1

        if len(stack) == 3:
            rhs = stack.pop()
            operator = stack.pop()
            lhs = stack.pop()

            if operator == '|':
                stack.append(lhs or rhs)
            elif operator == '&':
                stack.append(lhs and rhs)
            elif operator == '^':
                stack.append(lhs ^ rhs)

    
    return stack.pop() # The last element is always the solution




class TestExpr(unittest.TestCase):
    def test_unitary(self):
        self.assertEqual(evaluate("T"), True)
        self.assertEqual(evaluate("F"), False)

    def test_simple(self):
        self.assertEqual(evaluate("T&T"), True)
        self.assertEqual(evaluate("T&F"), False)
        self.assertEqual(evaluate("T|F"), True)
        self.assertEqual(evaluate("F|F"), False)
        self.assertEqual(evaluate("T^F"), True)
        self.assertEqual(evaluate("T^T"), False)

    def test_entire_parens(self):
        self.assertEqual(evaluate("(T)"), True)
        self.assertEqual(evaluate("(T|F)"), True)

    def test_chain(self):
        self.assertEqual(evaluate("T^F&T"), True)
    
    def test_complete(self):
        self.assertEqual(evaluate("(T|F)^(F&T)"), True)


if __name__ == '__main__':
    unittest.main()

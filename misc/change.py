import unittest
import copy


"""
Stores the state for calculating different ways of finding change
"""
class PiggyBank(object):
    def __init__(self, target):
        self.target = target
        self.total = 0
        self.quarters = 0
        self.dimes = 0
        self.nickels = 0
        self.pennies = 0

    def can_add_quarter(self):
        return self.target - self.total >= 25

    def add_quarter(self):
        self.total = self.total + 25
        self.quarters = self.quarters + 1

    def can_add_dime(self):
        return self.target - self.total >= 10

    def add_dime(self):
        self.total = self.total + 10
        self.dimes = self.dimes + 1
    
    def can_add_nickel(self):
        return self.target - self.total >= 5

    def add_nickel(self):
        self.total = self.total + 5
        self.nickels = self.nickels + 1

    def can_add_penny(self):
        return self.target - self.total >= 1

    def add_penny(self):
        self.total = self.total + 1
        self.pennies = self.pennies + 1
    
    def hit_target(self):
        return self.target == self.total

    def __str__(self):
        return "q: {0}, d: {1}, n: {2}, p: {3}, t: {4}, t: {5}".format(
            self.quarters,
            self.dimes,
            self.nickels,
            self.pennies,
            self.total,
            self.target
        )

    def __hash__(self):
        return hash(self.total)

    def __eq__(self, that):
        return all([self.target == that.target,
                self.total == that.total,
                self.quarters == that.quarters,
                self.dimes == that.dimes, 
                self.nickels == that.nickels,
                self.pennies == that.pennies])


def change(value):
    lookup = set([PiggyBank(value)])
    while True:
        lookup = change_inner(lookup)
        all_hit_target = True
        for elem in lookup:
            if elem.hit_target() == False:
                all_hit_target = False
        if all_hit_target:
            return lookup


def change_inner(lookup):
    
    new_lookup = set([])

    for elem in lookup:
        if elem.hit_target():
            new_elem = copy.copy(elem)
            new_lookup.add(new_elem)

    for elem in lookup:
        if elem.can_add_quarter():
            new_elem = copy.copy(elem)
            new_elem.add_quarter()
            new_lookup.add(new_elem)
        
    for elem in lookup:
        if elem.can_add_dime():
            new_elem = copy.copy(elem)
            new_elem.add_dime()
            new_lookup.add(new_elem)

    for elem in lookup:
        if elem.can_add_nickel():
            new_elem = copy.copy(elem)
            new_elem.add_nickel()
            new_lookup.add(new_elem)

    for elem in lookup:
        if elem.can_add_penny():
            new_elem = copy.copy(elem)
            new_elem.add_penny()
            new_lookup.add(new_elem)

    return new_lookup


class ChangeTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_simple(self):
        self.assertEqual(
            len(change(10)),
            4
        )


if __name__ == '__main__':
    unittest.main()

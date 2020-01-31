import sys
import unittest

class CounterDict(object):
    def __init__(self):
        self.lookup = {}

    def size(self):
        return len(self.lookup)

    def addChar(self, char):
        if char in self.lookup:
            self.lookup[char] = self.lookup[char] + 1
        else:
            self.lookup[char] = 1

    def removeChar(self, char):
        if self.lookup[char] > 1:
            self.lookup[char] = self.lookup[char] - 1
        else:
            del self.lookup[char]


def smallest_window(text, string):
    string_set = set(string)
    
    lookup = CounterDict()
    lookup.addChar(text[0])

    start = 0
    finish = 0

    min_window = sys.maxint

    while True:
        if lookup.size() == len(string_set):
            window = finish - start + 1
            if window < min_window:
                min_window = window

        if lookup.size() < len(string_set) and finish < len(text) - 1:
            finish = finish + 1
            
            if text[finish] in string_set:
                lookup.addChar(text[finish])

        elif lookup.size() == len(string_set):

            if text[start] in string_set:
                lookup.removeChar(text[start])
            start = start + 1
        else:
            break

    return min_window
        


class TestStringWindow(unittest.TestCase):
    def test_smallest_window(self):
        self.assertEqual(
            smallest_window("timetopractice", "toc"),
            6
        )


if __name__ == '__main__':
    unittest.main()

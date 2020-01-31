
"""
Find longest substring
"""

import unittest




d = {"ale", "apple", "monkey", "plea"}
string = "abpcplea"



def remove_at(string, index):
    return string[:index:] + string[index + 1::]


def longest_string(string, d):
    if string == "":
        return ""
    elif string in d:
        return string
    else:
        lines = []
        for index in xrange(len(string)):
            lines.append(longest_string(remove_at(string, index), d))

        return sorted(lines, key=lambda x: len(x))[-1]




class TestLongestString(unittest.TestCase):
    def test_remove_at(self):
        self.assertEqual(
            remove_at("bobby", 1),
            "bbby"
        )

    def test_empty_remove_at(self):
        self.assertEqual(
            remove_at('a', 0),
            ""
        )

    def test_longest_string(self):
        self.assertEqual(
            longest_string(string, d),
            "apple"
        )


if __name__ == "__main__":
    unittest.main()



"""
https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/
"""

class FiniteAutomata(object):
    def __init__(self, string):
        self.string = string
        self.lookup = []
        self.unique = {}

        # initialize lookup
        index = 0
        for elem in string:
            if elem not in self.unique:
                self.unique[elem] = index
                index += 1
        
        for _ in xrange(len(string) + 1):
            self.lookup.append([0] * len(self.unique))

        self.populate(list(string))


    def string_equals(self, arr1, arr2, start1, start2, stop1, stop2):
        while start1 < stop1 and start2 < stop2:
            if arr1[start1] != arr2[start2]:
                return False
            start1 += 1
            start2 += 1
        return True


    def longest_suffix(self, string, substring):
        for index in xrange(len(substring)):

            # Handle case where substring is actually longer than real string
            if len(substring) - index > len(string):
                continue

            if self.string_equals(string, substring, 0, index, len(string), len(substring)):
                return len(substring) - index
        return 0


    def populate(self, string):
        substring = []
        for index in xrange(len(string)+1):
            for k, v in self.unique.iteritems():
                substring.append(k)
                self.lookup[index][v] = self.longest_suffix(string, substring)
                substring.pop()
            
            if index < len(string):
                substring.append(string[index])

    
    def find_substrings(self, text):
        substrings = []
        loc = 0
        for t_ind in xrange(len(text)):
            if text[t_ind] in self.unique:
                loc = self.lookup[loc][self.unique[text[t_ind]]]
                if loc == len(self.string):
                    substrings.append(t_ind - len(self.string) + 1)
            else:
                loc = 0
        return substrings
 

def substrings(string, text):
    fa = FiniteAutomata(string)
    return fa.find_substrings(text)


print substrings("AABA", "AABAACAADAABAABA")

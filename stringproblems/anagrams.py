import unittest
import copy


def anagrams(word):
    return anagrams_inner('', word)

def anagrams_inner(prefix, word):
    if len(word) <= 1:
        return [prefix + word]

    arr = []
    for char_index in xrange(len(word)):

        char = word[char_index]
        substring = word[:char_index:] + word[char_index+1::]

        arr.extend(anagrams_inner(prefix + char, substring))

    return arr




def anagrams_2(word):
    indices = [True] * len(word)
    all_paths = []
    anagrams_2_inner(word, indices, [], all_paths)
    return all_paths


def anagrams_2_inner(word, indices, path, all_paths):

    if len(path) == len(word):
        all_paths.append("".join(path))
        return

    for index in xrange(len(indices)):
        if indices[index]:
            indices[index] = False
            path.append(word[index])
            anagrams_2_inner(word, indices, path, all_paths)
            indices[index] = True
            path.pop()


print anagrams_2("lake")




class AnagramTest(unittest.TestCase):
    def test_anagrams(self):
        self.assertEqual(
            len(anagrams('lake')),
            24
        )


if __name__ == '__main__':
    unittest.main()

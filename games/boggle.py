import random
import copy

"""
We create a board and find all words contained within the board
"""


class PrefixDictionary(object):
    def __init__(self, path):
        self.lookup = {}
        self.words = set([])
        f = open(path, 'r')
        for line in f.readlines():
            sline = line.strip().upper()
            if sline:
                self.words.add(sline)
                prefix_words = self._prefix_word(sline)
                for prefix_word in prefix_words:
                    if prefix_word in self.lookup:
                        self.lookup[prefix_word].append(sline)
                    else:
                        self.lookup[prefix_word] = [sline]
        f.close()

    def _prefix_word(self, word):
        return [word[:index+1:] for index in xrange(len(word))]
            



class Board(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.board = []
        
        letters = 'aaaaaaaaabbbcccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'.upper()

        for row_index in xrange(self.rows):
            row = []
            for _ in xrange(self.cols):
                random_letter = letters[random.randint(0, len(letters) - 1)]
                row.append(random_letter)

            self.board.append(row)
        

    def print_board(self):
        for row in self.board:
            print ' '.join(row)


    def find_all_words(self, prefix_dictionary):
        words = []
        for row_index in xrange(self.rows):
            for col_index in xrange(self.cols):
                words.extend(self.find_words_from_index(row_index, col_index, prefix_dictionary))
        return list(set(words))

    def find_words_from_index(self, row, col, prefix_dictionary):
        words = []
        visited = set([])
        self.find_words_from_index_inner(row, col, '', prefix_dictionary, words, visited)
        return words

    def find_words_from_index_inner(self, row, col, prefix, prefix_dictionary, words, visited):
        
        if not self.is_in_board(row, col):
            return
        
        point = (row, col)
        cvisited = copy.copy(visited)
        if point in cvisited:
            return
        
        cvisited.add(point)

        new_prefix = prefix + self.board[row][col]
        if new_prefix in prefix_dictionary.lookup:

            # If the prefix is a word, then add it
            if new_prefix in prefix_dictionary.words:
                words.append(new_prefix)

            # Look around to build more words
            self.find_words_from_index_inner(row + 1, col, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row - 1, col, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row, col - 1, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row, col + 1, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row + 1, col + 1, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row - 1, col - 1, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row + 1, col - 1, new_prefix, prefix_dictionary, words, cvisited)
            self.find_words_from_index_inner(row - 1, col + 1, new_prefix, prefix_dictionary, words, cvisited)

    def is_in_board(self, row, col):
        return row >= 0 and col >= 0 and row < self.rows and col < self.cols




board = Board(5,5)
board.print_board()
d = PrefixDictionary('words.txt')
print board.find_all_words(d)

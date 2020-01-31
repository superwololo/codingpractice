import unittest


def compute_all_primes(max_chars):
    all_primes = []
    candidate = 2
    while len(str(candidate)) <= max_chars:
        
        is_prime = True
        for prime in all_primes:
            if candidate % prime == 0:
                is_prime = False

        if is_prime:
            all_primes.append(candidate)

        candidate = candidate + 1
    
    return set(map(lambda x: str(x), all_primes))


def all_single_edits(number, all_primes):
    all_numbers = list("0123456789")
    start_numbers = list("123456789")
    permutations = []

    for index in xrange(len(number)):
        if index == 0:
            for char in start_numbers:
                if char != number[index]:
                    new_number = char + number[1::]
                    if new_number in all_primes:
                        permutations.append(new_number)
        else:
            for char in all_numbers:
                if char != number[index]:
                    new_number = number[:index:] + char + number[index+1::]
                    if new_number in all_primes:
                        permutations.append(new_number)

    return permutations
    

def bfs_to_find_min(start, finish):
    all_primes = compute_all_primes(len(str(finish)))
    queue = [(start, 0)]
    numbers_visited = set([])
    while len(queue) > 0:
        value = queue.pop(0)
        number = value[0]
        changes = value[1]
        
        if number == finish:
            return changes

        if number not in numbers_visited:
            numbers_visited.add(number)
            edits = all_single_edits(number, all_primes)

            for edit in edits:
                queue.append((edit, changes + 1))


class TestBfsToFindMin(unittest.TestCase):
    def test_find_to_find_min(self):
        self.assertEqual(bfs_to_find_min('1033', '8179'), 6)
        self.assertEqual(bfs_to_find_min('1373', '8017'), 7)
        self.assertEqual(bfs_to_find_min('1033', '1033'), 0)



if __name__ == '__main__':
    unittest.main()

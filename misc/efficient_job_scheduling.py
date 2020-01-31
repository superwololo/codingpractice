"""
https://www.geeksforgeeks.org/job-sequencing-using-disjoint-set-union/
"""

jobs = [
    ("a", 2, 100),
    ("b", 1, 19),
    ("c", 2, 27),
    ("d", 1, 25),
    ("e", 3, 15),
]

class SetNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = value

    def find_parent(self, disjoint_sets):
        if self.value == self.parent:
            return self.value
        else:
            self.parent = disjoint_sets[self.parent].find_parent(disjoint_sets)
            return self.parent

    def merge(self, other_index, disjoint_set):
        other_set = disjoint_set[other_index]
        if self.find_parent(disjoint_set) == other_set.find_parent(disjoint_set):
            return

        if self.value > other_index:
            self.parent = other_set.find_parent(disjoint_set)
        else:
            other_set.parent = self.find_parent(disjoint_set)


def max_profit(jobs):
    mtime = max(jobs, key=lambda x:x[1])[1]
    sorted_jobs = sorted(jobs, key=lambda x:-x[2])

    # sets
    disjoint_sets = []
    for index in xrange(mtime+1):
        disjoint_sets.append(SetNode(index))

    best_jobs = []
    total_profit = 0

    for job_id, deadline, profit in sorted_jobs:
        
        max_available = disjoint_sets[deadline].find_parent(disjoint_sets)
        if max_available > 0:
            best_jobs.append(job_id)
            total_profit += profit
            disjoint_sets[max_available].merge(max_available-1, disjoint_sets)

    return best_jobs, total_profit


print max_profit(jobs)

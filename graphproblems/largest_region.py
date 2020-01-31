"""
https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/
"""

grid = [
    [0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1]
]


# Method 1: DFS

def is_in_grid(grid, row, col):
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])


def dfs(grid, row, col, visited):
    
    if not is_in_grid(grid, row, col):
        return 0

    if (row, col) in visited:
        return 0
    
    visited.add((row, col))

    if grid[row][col] == 0:
        return 0

    return 1 + sum([
        dfs(grid, row+1, col, visited),
        dfs(grid, row-1, col, visited),
        dfs(grid, row, col+1, visited),
        dfs(grid, row, col-1, visited),
        dfs(grid, row+1, col+1, visited),
        dfs(grid, row+1, col-1, visited),
        dfs(grid, row-1, col+1, visited),
        dfs(grid, row-1, col-1, visited)
    ])


def max_segment(grid):
    visited = set()
    
    max_size = -1

    for row in xrange(len(grid)):
        for col in xrange(len(grid[0])):
            s = dfs(grid, row, col, visited)
            if s > max_size:
                max_size = s

    return max_size

print max_segment(grid)


# Method 2: Disjoint set

class DisjointSetNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = value
        self.size = 1

    def find(self, lookup):
        if self.value == self.parent:
            return self.value
        else:
            p = lookup[self.parent].find(lookup)
            return p

    def union(self, that, lookup):

        node_a_ref = self.find(lookup)
        node_b_ref = that.find(lookup)

        node_a = lookup[node_a_ref]
        node_b = lookup[node_b_ref]

        if node_a_ref == node_b_ref:
            return # The parents are the same so do nothing

        if node_a.size > node_b.size:
            node_b.parent = node_a.value
            node_a.size = node_b.size + node_a.size
        else:
            node_a.parent = node_b.value
            node_b.size = node_a.size + node_b.size


def maybe_union(node, grid, lookup, row, col):
    if is_in_grid(grid, row, col) and grid[row][col] == 1:
        target = lookup[row * len(grid[0]) + col]
        node.union(target, lookup)

def find_max_segment(grid):
    
    # Initialize disjoint set
    lookup = []
    for row in xrange(len(grid)):
        for col in xrange(len(grid[0])):
            node_id = row * len(grid[0]) + col
            lookup.append(DisjointSetNode(node_id))
    
    #Do unions
    for row in xrange(len(grid)):
        for col in xrange(len(grid[0])):
            if grid[row][col] == 0:
                continue

            node = lookup[row * len(grid[0]) + col]
            
            maybe_union(node, grid, lookup, row, col+1)
            maybe_union(node, grid, lookup, row+1, col+1)
            maybe_union(node, grid, lookup, row+1, col)
            maybe_union(node, grid, lookup, row+1, col-1)
        
    # Find max
    return max(map(lambda x: x.size, lookup))


print find_max_segment(grid)

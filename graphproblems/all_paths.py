import unittest
import copy


graph = {
    'A' : ['B', 'C', 'E'],
    'B' : ['D', 'E'],
    'C' : ['E'],
    'D' : ['C'],
    'E' : []
}

def all_paths(start, finish):
    found_paths = []
    all_paths_inner(start, finish, [start], found_paths)
    return found_paths


def all_paths_inner(start, finish, path, found_paths):
    if start == finish:
        found_paths.append(copy.copy(path))
        return

    children = graph[start]
    for child in children:
        if child not in path:
            path.append(child)
            all_paths_inner(child, finish, path, found_paths)
            path.pop()

result = all_paths('A', 'E')

for r in result:
    print ' -> '.join(r)

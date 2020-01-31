import unittest
import copy

graph = {
    0 : [],
    1 : [],
    2 : [3],
    3 : [1],
    4 : [0, 1],
    5 : [0, 2]
}

"""
Find a single topological sort
"""
def topological_sort(graph):
    visited = set([])
    stack = []
    for vertex, links in graph.iteritems():
        topological_sort_inner(graph, vertex, visited, stack)
    print stack

def topological_sort_inner(graph, vertex, visited, stack):
    if vertex not in visited:
        visited.add(vertex)
        for link in graph[vertex]:
            topological_sort_inner(graph, link, visited, stack)
        stack.insert(0, vertex)


def find_root_nodes(graph, prefix, results):

    # Get all vertices from the graph
    all_vertices = set([])
    for k, v in graph.iteritems():
        all_vertices.add(k)

    # Stop recursion if we've found a complete topological sort
    if len(all_vertices) == len(prefix):
        results.append(prefix)

    # Remove graph vertices that were already selected
    for elem in prefix:
        all_vertices.remove(elem)

    temp_removal = set([])
    for k, v in graph.iteritems():
        if k in all_vertices:
            for elem in v:
                if elem in all_vertices:
                    temp_removal.add(elem)

    for elem in temp_removal:
        all_vertices.remove(elem)

    for vertex in all_vertices:
        prefix_copy = copy.copy(prefix)
        prefix_copy.append(vertex)
        find_root_nodes(graph, prefix_copy, results)


"""
Find all topological sorts
"""
def all_topological_sort(graph):
    prefix = []
    results = []
    find_root_nodes(graph, prefix, results)
    return results


class TestTopologicalSort(unittest.TestCase):
    def test_all_topological_sort(self):
        graph = {
            0 : [],
            1 : [],
            2 : [3],
            3 : [1],
            4 : [0, 1],
            5 : [0, 2]
        }
        results = all_topological_sort(graph)
        self.assertEqual(
            len(results),
            13
        )


if __name__ == '__main__':
    unittest.main()

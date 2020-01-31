
graph = {
    0 : [1, 5],
    1 : [2, 3, 4],
    2 : [3, 4],
    3 : [4],
    4 : [],
    5 : [1, 2]
}

new_edges = [
    (0, 2),
    (0, 3),
    (4, 5)
]


def topological_sort(graph):
    stack = []
    visited = set()
    
    for k, _ in graph.iteritems():
        topological_sort_inner(graph, k, stack, visited)

    return stack[::-1]


def topological_sort_inner(graph, node, stack, visited):
    
    if node in visited:
        return

    vertices = graph[node]

    for vertex in vertices:
        topological_sort_inner(graph, vertex, stack, visited)

    stack.append(node)
    visited.add(node)


def add_directions(graph, new_edges):

    tsort = topological_sort(graph)

    directed_edges = []

    for node_a, node_b in new_edges:
        for elem in tsort:
            if elem == node_a:
                directed_edges.append((node_a, node_b))
                break
            if elem == node_b:
                directed_edges.append((node_b, node_a))
                break

    return directed_edges


print add_directions(graph, new_edges)

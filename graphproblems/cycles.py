
graph = {
    0 : [1],
    1 : [2],
    2 : [0, 3],
    3 : [3]
}



def detect_cycles(graph):
    for k, _ in graph.iteritems():
        res = cycles_inner(graph, k, set())
        if res:
            return True
    return False


def cycles_inner(graph, node, visited):

    vertices = graph[node]

    for vertex in vertices:

        if vertex in visited:
            return True

        visited.add(vertex)
        res = cycles_inner(graph, vertex, visited)
        if res:
            return True
        visited.remove(vertex)

    return False


print detect_cycles(graph)

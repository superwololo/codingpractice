


graph = {
    0 : [(1, 5), (3, 10)],
    1 : [(2, 3)],
    2 : [(3, 1)],
    3 : []
}


def floyd_warshall(graph):

    # initialized vertex pairs
    result = []
    for _ in xrange(len(graph)):
        result.append([None] * len(graph))

    # fill in first values
    for k, v in graph.iteritems():
        for vertex, weight in v:
            result[k][vertex] = weight

    

    return result


result = floyd_warshall(graph)


for row in result:
    print row

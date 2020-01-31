
values = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 6),
]

def create_graph(values):
    graph = {}
    for v in values:
        if v[0] in graph:
            graph[v[0]].append(v[1])
        else:
            graph[v[0]] = [v[1]]
    return graph


def bfs(graph, root, max_depth):
    traversal = []
    queue = [root]
    count = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node[1] == max_depth:
            count = count + 1
        traversal.append(node)
        children = graph.get(node[0], [])
        
        for child in children:
            depth = node[1] + 1
            if depth <= max_depth:
                queue.append((child, depth))

    return count

def count_at_depth(values, target_depth):
    graph = create_graph(values)
    return bfs(graph, (0, 0), target_depth)


print count_at_depth(values, 2)



edges = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 7, 11),
    (1, 2, 8),
    (2, 8, 2),
    (7, 8, 7),
    (7, 6, 1),
    (8, 6, 6),
    (6, 5, 2),
    (2, 5, 4),
    (3, 5, 14),
    (2, 3, 7),
    (3, 4, 9),
    (5, 4, 10)
]

def create_graph(edges):
    graph = {}
    for edge in edges:
        nodeA = edge[0]
        nodeB = edge[1]
        weight = edge[2]

        if nodeA not in graph:
            graph[nodeA] = [(nodeB, weight)]
        else:
            graph[nodeA].append((nodeB, weight))

        if nodeB not in graph:
            graph[nodeB] = [(nodeA, weight)]
        else:
            graph[nodeB].append((nodeA, weight))

    return graph



def at_least_k(edges, start, K):
    graph = create_graph(edges)
    return dfs(graph, start, 0, set([]))
    

def dfs(graph, start, path_weight, visited):

    if start in visited:
        return -1

    visited.add(start)

    nodes = graph[start]

    weights = [path_weight]
    for node in nodes:
        new_node = node[0]
        edge_weight = node[1]

        new_path = dfs(graph, new_node, path_weight + edge_weight, visited)

        weights.append(new_path)

        if new_path > -1:
            visited.remove(new_node)

    return max(weights)


print at_least_k(edges, 0, 58)

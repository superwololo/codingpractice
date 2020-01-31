import copy

graph = [
    [-1, 10, 3, 2],
    [-1, -1, -1, 7],
    [-1, -1, -1, 6],
    [-1, -1, -1, -1]
]


"""
This is the unoptimized solution, we can do better by creating an optimized solution
"""
def shortest_k_path_inner(graph, src, dst, k, path, weight, all_paths):
    
    if k == 0:
        if src == dst:
            all_paths.append((copy.copy(path), weight))
        return

    nodes = graph[src]
    for index in xrange(len(nodes)):
        if nodes[index] != -1:
            path.append(index)
            shortest_k_path_inner(graph, index, dst, k - 1, path, weight + nodes[index], all_paths)
            path.pop()



def shortest_k_path(graph, src, dst, k):
    all_paths = []
    shortest_k_path_inner(graph, src, dst, k, [src], 0, all_paths)
    return all_paths


def visited_to_path(visited, src, dst, k):
    path = [dst]
    while visited[(dst, k)][1] != None:
        dst = visited[(dst, k)][1]
        k = k - 1
        path.append(dst)
    return path[::-1]


def shortest_k(graph, src, dst, k):
    
    visited = {}

    q = [(src, 0, 0, None)] # Node, steps, weight, prev

    while len(q) > 0:
        
        node, steps, weight, prev = q.pop(0)
        
        if (node, steps) not in visited:
            visited[(node, steps)] = (weight, prev)
        elif visited[(node, steps)][0] > weight:
            visited[(node, steps)] = (weight, prev)
        else:
            continue
        
        if steps == k:
            continue

        vertices = graph[node]

        for node_index in xrange(len(vertices)):
            if vertices[node_index] != -1:
                q.append((node_index, steps+1, weight + vertices[node_index], node))

    return visited_to_path(visited, src, dst, k)


print shortest_k(graph, 0, 3, 2)



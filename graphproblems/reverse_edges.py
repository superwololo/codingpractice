from Queue import PriorityQueue


graph = {
    0 : [1],
    1 : [],
    2 : [1, 3],
    3 : [],
    4 : [5],
    5 : [1],
    6 : [3, 4]
}


def to_weighted(graph):
    new_graph = {}

    for k, v in graph.iteritems():
        
        new_graph[k] = []

        # Add nodes of weight 0
        for node in v:
            new_graph[k].append((0, node))

    
    for k, v in graph.iteritems():
        for node in v:
            if node not in new_graph:
                new_graph[node] = []
            new_graph[node].append((1, k))

    return new_graph


def create_path(visited, src, dst):
    path = [dst]
    while visited[dst] != None:
        dst = visited[dst]
        path.append(dst)

    return path[::-1]


def flips(graph, path):
    
    # All edges
    edges = set()
    for k, v in graph.iteritems():
        for node in v:
            edges.add((k, node))

    reverse = []

    for index in xrange(len(path)-1):
        edge = (path[index], path[index+1])
        
        if edge not in edges:
            reverse.append(edge)

    return reverse
    


def shortest_path(new_graph, src, dst):

    q = PriorityQueue()
    q.put((0, src, None))

    visited = {}

    while not q.empty():
        
        weight, node, prev_node = q.get()
        
        if node in visited:
            continue
        
        visited[node] = prev_node

        if node == dst:
            return visited

        vertices = new_graph[node]

        for vertex_weight, vertex in vertices:
            q.put((weight + vertex_weight, vertex, node))


def reverse_edges(graph, src, dst):
    new_graph = to_weighted(graph)
    visited = shortest_path(new_graph, src, dst)
    
    print flips(graph, create_path(visited, src, dst))



reverse_edges(graph, 0, 6)

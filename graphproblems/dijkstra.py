import heapq


edges = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 7, 11),
    (1, 2, 8),
    (2, 8, 2),
    (7, 8, 7),
    (7, 6, 1),
    (8, 6, 6),
    (2, 3, 7),
    (2, 5, 4),
    (6, 5, 2),
    (3, 5, 14),
    (3, 4, 9),
    (5, 4, 10)
]

def create_graph(edges):
    graph = {}
    for edge in edges:
        nodeA = edge[0]
        nodeB = edge[1]
        weight = edge[2]

        if nodeA in graph:
            graph[nodeA].append((nodeB, weight))
        else:
            graph[nodeA] = [(nodeB, weight)]

        if nodeB in graph:
            graph[nodeB].append((nodeA, weight))
        else:
            graph[nodeB] = [(nodeA, weight)]
    return graph


class PQueue(object):
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, item, weight):
        heapq.heappush(self.heap, (weight, item))

    def dequeue(self):
        return heapq.heappop(self.heap)



def dijkstra(graph, startNode):
    
    # Map from current node -> (prevNode, distance)
    visited = {}

    pqueue = PQueue()
    pqueue.enqueue((startNode, None), 0)
    
    while not pqueue.is_empty():
        weight, elem = pqueue.dequeue()
        current = elem[0]
        prev = elem[1]

        if current not in visited:
            visited[current] = (prev, weight)
            
            vertices = graph[current]
            
            for vertex, edge_weight in vertices:
                pqueue.enqueue((vertex, current), edge_weight + weight)
    return visited
    

graph = create_graph(edges)
print dijkstra(graph, 0)



        
        

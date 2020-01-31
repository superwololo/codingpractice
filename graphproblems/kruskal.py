

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



class DisjointSetNode(object):
    def __init__(self, node_id):
        self.node_id = node_id
        self.parent = node_id
        self.size = 1
        


class DisjointSet(object):
    def __init__(self, node_ids):
        self.node_map = {}
        for node_id in node_ids:
            self.node_map[node_id] = DisjointSetNode(node_id)

    def find_parent(self, node_id):
        node = self.node_map[node_id]
        if node.node_id == node.parent:
            return node.node_id
        else:
            node.parent = self.find_parent(node.parent)
            return node.parent

    def merge_nodes(self, node_id_a, node_id_b):
        node_a = self.node_map[node_id_a]
        node_b = self.node_map[node_id_b]
        
        if node_a.parent == node_b.parent:
            return
        else:
            node_a_parent = self.node_map[node_a.parent]
            node_b_parent = self.node_map[node_b.parent]

            if node_a_parent.size > node_b_parent.size:
                node_b_parent.parent = node_a_parent.node_id
                node_a_parent.size = node_a_parent.size + node_b_parent.size
            else:
                node_a_parent.parent = node_b_parent.node_id
                node_b_parent.size = node_a_parent.size + node_b_parent.size


def find_node_ids(edges):
    node_ids = set([])
    for node_1, node_2, weight in edges:
        node_ids.add(node_1)
        node_ids.add(node_2)
    return node_ids


def spanning_tree(edges):

    node_ids = find_node_ids(edges)
    spanning_edges = []

    djs = DisjointSet(node_ids)
    
    sorted_edges = sorted(edges, key=lambda x:x[2])
    for node_a_id, node_b_id, weight in sorted_edges:
        if djs.find_parent(node_a_id) != djs.find_parent(node_b_id):
            spanning_edges.append((node_a_id, node_b_id))
            djs.merge_nodes(node_a_id, node_b_id)

    return spanning_edges



print spanning_tree(edges)

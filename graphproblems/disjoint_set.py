
"""
Implementation to find if two vertices are from the same subset
"""


edges = [
    (0, 1),
    (1, 2),
    (2, 1),
    (3, 4),
    (4, 5),
    (5, 3),
]


class DisjointSet(object):
    def __init__(self, edges):
        self.nodes = self._create_set_nodes(edges)

    def _create_set_nodes(self, edges):
        nodes = {}
        for nodeA, nodeB in edges:
            if nodeA not in nodes:
                nodes[nodeA] = DisjointSetNode(nodeA)

            if nodeB not in nodes:
                nodes[nodeB] = DisjointSetNode(nodeB)
        return nodes


    def find(self, node_id):
        node = self.nodes[node_id]
        if node.parent == node.value:
            return node.value
        else:
            node.parent = self.find(node.parent)
            return node.parent


    def union(self, node_1_id, node_2_id):
        node_1_root_id = self.find(node_1_id)
        node_2_root_id = self.find(node_2_id)

        node_1_root = self.nodes[node_1_root_id]
        node_2_root = self.nodes[node_2_root_id]

        if node_1_root_id == node_2_root_id:
            return

        if node_1_root.size < node_2_root.size:
            node_1_root.parent = node_2_root_id
            node_2_root.size = node_2_root.size + node_1_root.size
        else:
            node_2_root.parent = node_1_root_id
            node_1_root.size = node_2_root.size + node_1_root.size


class DisjointSetNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = value
        self.size = 1



djs = DisjointSet(edges)
for a, b in edges:
    djs.union(a, b)

for a, b in edges:
    print a, b, djs.find(a), djs.find(b)

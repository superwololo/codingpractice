import unittest


print 'hello, mother vertex'


class Node(object):
    def __init__(self, identifier):
        self.identifier = identifier
        self.children = []


class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes


    """
    Returns the identifier of a mother vertex
    """
    def findMotherVertex(self):
        sub_vertices = {}
        for node in self.nodes:
            vertices = set([])
            verticesForNode(node, vertices, sub_vertices)
            sub_vertices[node.identifier] = vertices
            if len(vertices) == len(self.nodes):
                return node.identifier
        return None


    def verticesForNode(self, node, vertices, sub_vertices):
        if node.identifier in sub_vertices:
            return 
        elif node.identifier in vertices:
            return
        else:
            vertices.add(node.identifier)

        for child in self.children:
            verticesForNode(child, vertices)



class TestMotherVertex(unittest.TestCase):
    def setUp():
        pass

    def test_full_case(self):
        pass



if __name__ == '__main__':
    unittest.main()



nodes = [
    Node("A"),
    Node("B"),
    Node("C"),
    Node("D"),
    Node("E"),
    Node("F")
]

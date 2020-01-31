import unittest

"""
Sample code to create a tree and then traverse it using DFS and BFS
"""

"""
Step 1: Create tree datastructures so we can construct a tree
"""
class Node(object):
    def __init__(self, name):
        self.children = []
        self.name = name

    def appendChildNode(self, node):
        self.children.append(node)

    def __str__(self):
        return "NODE: " + self.name

    def __repr__(self):
        return str(self)


class Tree(object):
    def __init__(self):
        self.lookup = {}

    def createNode(self, name):
        self.lookup[name] = Node(name)


"""
Step 2: traverse the tree using depth first search
"""
def traverseDFSWrapper(node):
    arr = []
    traverseDFS(node, arr)
    return arr

def traverseDFS(node, arr):
    arr.append(node.name)
    for child in node.children:
        traverseDFS(child, arr)

"""
Step 3: traverse the tree using breadth first search
"""
def traverseBFSWrapper(node):
    output = []
    queue = []
    traverseBFS(node, output, queue)
    return output

def traverseBFS(node, output, queue):
    output.append(node.name)
    for child in node.children:
        queue.append(child)
    while len(queue) > 0:
        elem = queue.pop(0)
        traverseBFS(elem, output, queue)

class TraversalTest(unittest.TestCase):

    # create a sample tree
    def setUp(self):
        self.tree = Tree()
        
        #Create nodes
        nodes = ['root', 'A', 'B', 'C', 'D', 'E', 'F']
        for node in nodes:
            self.tree.createNode(node)

        #Connect tree
        self.tree.lookup['root'].appendChildNode(self.tree.lookup['A'])
        self.tree.lookup['root'].appendChildNode(self.tree.lookup['B'])
        self.tree.lookup['A'].appendChildNode(self.tree.lookup['C'])
        self.tree.lookup['A'].appendChildNode(self.tree.lookup['D'])
        self.tree.lookup['B'].appendChildNode(self.tree.lookup['E'])
        self.tree.lookup['B'].appendChildNode(self.tree.lookup['F'])

    def tearDown(self):
        pass

    def test_dfs(self):
        res = traverseDFSWrapper(self.tree.lookup['root'])
        self.assertEqual(res, ['root', 'A', 'C', 'D', 'B', 'E', 'F'])

    def test_bfs(self):
        res = traverseBFSWrapper(self.tree.lookup['root'])
        self.assertEqual(res, ['root', 'A', 'B', 'C', 'D', 'E', 'F'])


if __name__ == '__main__':
    unittest.main()

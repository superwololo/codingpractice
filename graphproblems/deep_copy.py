"""
Create a deep copy of a graph
"""

class Node(object):
    def __init__(self, name):
        self.name = name
        self.links = []

    def __str__(self):
        return self.name + ' ' + ' '.join(map(lambda x: x.name, self.links))


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.links.append(B)
A.links.append(C)
C.links.append(D)
C.links.append(E)
C.links.append(F)
F.links.append(A)
F.links.append(B)

# Print out the graph
def print_graph(node, visited):
    if node.name not in visited:
        print node.name, map(lambda x : x.name, node.links)
        visited.add(node.name)
        
        for link in node.links:
            print_graph(link, visited)

#print_graph(A, set([]))



def deep_copy_inner(node, copies):
    if node.name not in copies:
        copies[node.name] = Node(node.name)
        for link in node.links:
            deep_copy_inner(link, copies)


def add_links(node, copies, visited):
    if node.name not in visited:
        visited.add(node.name)
        original_link_names = map(lambda x: x.name, node.links)
        node_copy = copies[node.name]
        for original_link_name in original_link_names:
            node_copy.links.append(copies[original_link_name])
        for link_node in node.links:
            add_links(link_node, copies, visited)


def deep_copy(node):
    copies = {}
    deep_copy_inner(node, copies)
    add_links(node, copies, set([]))
    print_graph(copies['A'], set([]))


deep_copy(A)

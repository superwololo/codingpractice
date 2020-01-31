

tree = {
    10 : (3, 15),
    3 : (1, 4),
    4 : (None, 5),
    5 : (None, None),
    1 : (None, None),
    15 : (12, 16),
    12 : (None, None),
    16 : (None, None)
}

root  = 10


stack = []
def dfs(tree, root, stack):
    if root == None:
        return

    left, right = tree[root]
    dfs(tree, left, stack)
    stack.append(root)
    dfs(tree, right, stack)


def kth_smallest(tree, root, K):
    stack = []
    dfs(tree, root, stack)
    return stack[K]

print sorted(tree.keys())
print kth_smallest(tree, root, 3)

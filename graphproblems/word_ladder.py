
d = {"POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"}


def delete_chars(word):
    res = []
    for index in xrange(len(word)):
        a = word[:index:] + "_" + word[index+1::]
        res.append(a)
    return res


def make_graph(d):
    g = {}
    for word in d:
        words = delete_chars(word)

        for w in words:
            if w not in g:
                g[w] = []
            g[w].append(word)
    return g


def backward(visited, start, target):
    path = [target]
    while visited[target] != None:
        target = visited[target]
        path.append(target)
    return path


def shortest_change(d, start, target):

    g = make_graph(d)

    q = [(start, None)]
    visited = {}
    while len(q) > 0:
        
        elem, prev = q.pop(0)
        
        if elem in visited:
            continue

        visited[elem] = prev

        if elem == target:
            return backward(visited, start, target)

        sanitized = delete_chars(elem)
        for s in sanitized:
            q.extend(map(lambda x: (x, elem), g.get(s, [])))

    return None


print shortest_change(d, "TOON", "PLEA")

from collections import deque, defaultdict
def install_package(package, dep_graph):
    dep_path = deque()

    if package not in dep_graph:
        return dep_path

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    stack = [package]
    while stack:
        p = stack.pop()
        if p not in in_degree:
            in_degree[p] = 0
        if p not in graph:
            graph[p] = []
        if p in dep_graph:
            for child in dep_graph[p]:
                in_degree[child] += 1
                graph[p].append(child)
                stack.append(child)

    sources = deque()
    for k,v in in_degree.items():
        if v == 0:
            sources.append(k)

    while sources:
        parent = sources.popleft()
        dep_path.appendleft(parent)
        for child in graph[parent]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(dep_path) != len(graph):
        return []

    return list(dep_path)

modules = install_package('N', {
  'A' : ['E','N','S'],  
  'E' : ['N'],
  'S' : ['H', 'N'],
  'H' : [],
  'N' : []
})
print(5 - len(modules))

line = "a,e,i,o,u"
data = line.split(',')
print(data)
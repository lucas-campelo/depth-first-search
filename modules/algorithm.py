clock = 0

def dfs_search(graph, s):
    global clock
    clock += 1
    s.start = clock
    s.color = 'g'
    for i in s.adj:
        if graph[i].color == 'w':
            graph[i].parent = s
            dfs_search(graph, graph[i])
    clock += 1
    s.end = clock
    s.color = 'b'

def dfs(graph):
    for node in graph:
        if node.color == 'w':
            dfs_search(graph, node)
    return graph
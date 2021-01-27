from modules import Node, dfs, dfs_search, clock

g = [
    Node(label='A', adj=[1, 3]),
    Node(label='B', adj=[0, 2, 5, 6]),
    Node(label='C', adj=[1, 6]),
    Node(label='D', adj=[0, 5, 4]),
    Node(label='E', adj=[3, 5, 6]),
    Node(label='F', adj=[1, 3, 4]),
    Node(label='G', adj=[2, 1, 4, 7]),
    Node(label='H', adj=[6])
]

if __name__ == '__main__':
    tree = dfs(g)
    for node in tree:
        print(node)
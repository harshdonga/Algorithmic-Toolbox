#python3

import sys

def reach(adj, x, y, visited):
    if x == y:
        return 1
    else:
        visited[x] = 1
        for i in range(len(adj[x])):
            if (not visited[adj[x][i]]):
                if reach(adj, adj[x][i], y, visited):
                    return 1

    return 0

if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    adj = [[] for _ in range(v)]
    for i in range(e):
        a, b = [int(i) for i in input().split()]
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x, y = [int(i) for i in input().split()]
    x, y = x-1, y-1
    visited = [0]*len(adj)
    print(reach(adj, x, y, visited))
#Uses python3

def acyclic(adj):
    visited = [0]*len(adj)
    rec = [0]*len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            if explore(adj, i, visited, rec):
                return 1
    return 0

def explore(adj, x, visited, rec):
    visited[x] = 1
    rec[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]] and explore(adj, adj[x][i], visited, rec):
            return 1
        elif rec[adj[x][i]]:
            return 1
    rec[x] = 0
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())		
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
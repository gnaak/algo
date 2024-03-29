
n, m, v = map(int,input().split())
node = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    node[a][b] = node[b][a] = 1

dfs_cnt = []
bfs_cnt = []
visited = [0] * (n + 1)
visited2 = [0] * (n + 1)
def dfs(v):
    dfs_cnt.append(v)
    visited[v] = 1
    for i in range(1,n+1):
        if visited[i] == 0 and node[v][i] ==1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited2[v] = 1
    while queue:
        v = queue.pop(0)
        bfs_cnt.append(v)
        for i in range(1,n+1):
            if visited2[i] == 0 and node[v][i] ==1:
                queue.append(i)
                visited2[i] = 1

dfs(v)
bfs(v)
for i in dfs_cnt:
    print(i, end=' ')
print()
for i in bfs_cnt:
    print(i, end=' ')

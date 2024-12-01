import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    depth = 1
    visited[start] = depth
    while queue:
        cur_node = queue.popleft()

        for nxt in graph[cur_node]:
            if visited[nxt] == 0 :
                depth += 1
                visited[nxt] = depth
                queue.append(nxt)


n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort(reverse=True)

visited = [0]*(n+1)
bfs(r)

print('\n'.join(map(str,visited[1:])))
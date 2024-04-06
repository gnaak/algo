'''
백준 실버 2
연결 요소의 개수
'''

import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split()) # 정점의 개수 n, 간선의 개수 m
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque([])
cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        queue.append(i)
        while queue:
            start = queue.popleft()
            for node in graph[start]:
                if visited[node] == 0 :
                    visited[node] = 1
                    queue.append(node)
        cnt +=1

print(cnt)
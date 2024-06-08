'''
백준 실버 2
알고리즘 수업 - 너비 우선 탐색 1
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    cnt = 1
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                cnt += 1
                visited[next] = cnt
                queue.append(next)

n, m, r = map(int,input().split()) # n : 정점의 개수, m : 간선의 개수, r : 시작 정점
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i].sort()

visited= [0] * (n+1)
visited[r] = 1
bfs(r) # 시작 정점과, 방문 순서는 1
print(*visited[1:])

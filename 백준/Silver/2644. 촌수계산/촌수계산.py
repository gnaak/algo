'''
백준 실버 2
촌수계산
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    while queue:
        x, distance = queue.popleft()
        if x == b:
            return distance
        for neighbor in graph[x]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                queue.append((neighbor, distance + 1))
    return -1

n = int(input()) # 전체 사람의 수
a, b = map(int,input().split()) # 관계를 구해야 하는 사람들
m = int(input()) # 관계의 개수

graph = [[] for _ in range(n+1)] # 사람의 부모 찾기
visited = [0]*(n+1)
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited[a] = 1
result = bfs(a)
print(result)
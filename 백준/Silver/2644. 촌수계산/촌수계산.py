import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([(start, 0)]) # 시작 사람과 촌 수
    while queue:
        x, distance = queue.popleft()
        if x == b :
            return distance
        for neighbor in graph[x]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                queue.append((neighbor, distance+1))
    return -1

n = int(input()) # 전체 사람의 수 n
a, b = map(int,input().split()) # 촌수를 구해야 하는 사람 a, b
m = int(input()) # 관계의 개수 m
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    x, y = map(int,input().split()) # x는 y의 부모를 의미
    graph[x].append(y)
    graph[y].append(x)
visited[a] = 1
print(bfs(a))
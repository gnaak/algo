'''
백준 실버 1
경로 찾기
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        a = queue.popleft()
        for i in range(n):
            if check[i] == 0 and graph[a][i] == 1:
                check[i] = 1
                visited[x][i] = 1
                queue.append(i)


queue = deque();
n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
for _ in range(n):
    node = list(map(int,input().split()))
    graph.append(node)

for i in range(n):
    bfs(i)

for _ in visited:
    print(*_)


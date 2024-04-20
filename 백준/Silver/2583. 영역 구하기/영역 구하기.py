import sys
from collections import deque

queue = deque()
m, n, k = map(int, sys.stdin.readline().split())  # m*n k개
maps = [[0] * n for _ in range(m)]

def bfs():
    s = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == 0 and maps[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = 1
                s+=1
    area.append(s)

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            maps[j][i] = 1

visited = [[0] * n for _ in range(m)]
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
area = []
for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            queue.append((i, j))
            bfs()

area.sort()
print(len(area))
print(*area)
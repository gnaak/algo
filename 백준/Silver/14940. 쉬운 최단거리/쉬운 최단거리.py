import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x, 0)])
    while queue:
        y, x, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if board[ny][nx] == 1:
                    board[ny][nx] = cnt + 1
                    queue.append((ny, nx, cnt + 1))

n, m = map(int, input().split())  # 지도 크기 n, m
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start_y, start_x = -1, -1

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start_y, start_x = i, j
            break
            
visited[start_y][start_x] = 1
board[start_y][start_x] = 0
bfs(start_y, start_x)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            board[i][j] = -1

for row in board:
    print(*row)

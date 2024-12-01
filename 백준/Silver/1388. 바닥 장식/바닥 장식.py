# 바닥 장식

import sys
input = sys.stdin.readline
from collections import deque

def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1

    flag = 0
    if board[y][x] == '|':
        flag = 1

    while queue :
        y, x = queue.popleft()
        if flag:
            ny, nx = y + 1, x
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0 and board[ny][nx] == '|':
                visited[ny][nx] = 1
                queue.append((ny, nx))
        else:
            ny, nx = y, x + 1
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0 and board[ny][nx] == '-':
                visited[ny][nx] = 1
                queue.append((ny, nx))


n , m = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
ans = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            bfs(i, j)
            ans += 1
print(ans)
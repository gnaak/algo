# 전쟁 - 전투

import sys
input = sys.stdin.readline
from collections import deque

def check(i, j):
    queue = deque([(i, j)])
    current = warriors[i][j]
    count = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and counted[ny][nx] == 0 and warriors[ny][nx] == current:
                counted[ny][nx] = 1
                queue.append((ny,nx))
                count += 1
    return count**2
m, n = map(int,input().split())
warriors = [list(map(str,input().strip())) for _ in range(n)]
counted = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
w, b = 0, 0
for i in range(n):
    for j in range(m):
        if counted[i][j] == 0 :
            counted[i][j] = 1
            if warriors[i][j] == 'W':
                w += check(i, j)
            else:
                b += check(i, j)

print(w, b)
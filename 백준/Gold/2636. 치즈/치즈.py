# 치즈

import sys
input = sys.stdin.readline
from collections import deque

def meltin():
    queue = deque([(0,0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    melt = []

    while queue :
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0 :
                visited[ny][nx] = 1
                if board[ny][nx] == 0 :
                    queue.append((ny,nx))
                else:
                    melt.append((ny,nx))

    for cheese in melt:
        y, x = cheese
        board[y][x] = 0

    return len(melt)

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

last = 0
time = 0
while True:
    left = meltin()
    if left != 0 :
        last = left
    else:
        break

    time +=1


print(time)
print(last)
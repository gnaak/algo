# 빙산

# 지구 온난화로 빙산이 녹고 있다.

import sys
input = sys.stdin.readline
from collections import deque

def melt():
    melt_ice = [[0]*m for _ in range(n)]
    while ice:
        y, x = ice.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and sea[ny][nx] == 0:
                melt_ice[y][x] += 1

    for i in range(n):
        for j in range(m):
            if sea[i][j] >= melt_ice[i][j]:
                sea[i][j] -= melt_ice[i][j]
                if sea[i][j] > 0 :
                    ice.append((i,j))
            else:
                sea[i][j] = 0


def check(y,x):
    queue = deque([])
    queue.append((y,x))
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            ny = r + dy[i]
            nx = c + dx[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0 and sea[ny][nx]!= 0:
                visited[ny][nx] = 1
                queue.append((ny,nx))


n, m = map(int,input().split())
sea = [list(map(int,input().split())) for _ in range(n)]

year = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ice = []
for i in range(n):
    for j in range(m):
        if sea[i][j] != 0:
            ice.append((i,j))
while True:
    visited = [[0]*m for _ in range(n)]
    # 빙산의 덩어리 구하기
    cnt = 0
    for i, j in ice:
        if visited[i][j] == 0 :
            cnt += 1
            check(i,j)

    if cnt >= 2 :
        break

    elif cnt == 0 :
        year = 0
        break


    # 빙산 위치 파악한 후, 녹이기
    melt()
    year += 1

print(year)
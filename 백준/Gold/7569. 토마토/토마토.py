'''
백준 골드 5
토마토
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if nx < 0 or nx >=m or ny < 0 or ny >=n or nz < 0 or nz >=h :
                continue
            if graph[nz][ny][nx] == 0:
                queue.append((nz,ny,nx))
                graph[nz][ny][nx] = graph[z][y][x] +1

m, n, h = map(int,input().split()) # 가로 m, 세로 n, 상자의 수h
graph = [[] for _ in range(h)]
queue = deque()
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int,input().split())))

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
cnt = 0
ans = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append((z,y,x))
bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                ans = -1
                break
            cnt = max(cnt,graph[i][j][k])
print(cnt-1 if ans !=-1 else ans)
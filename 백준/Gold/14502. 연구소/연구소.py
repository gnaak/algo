'''
백준 골드 4
연구소
'''
import copy
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    tmp_maps = copy.deepcopy(maps)

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 > nx or nx >=n or 0 > ny or ny >=m:
                continue
            if tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                queue.append((nx,ny))

    global ans
    cnt = 0

    for i in range(n):
        for j in range(m):
            if tmp_maps[i][j] == 0 :
                cnt +=1

    ans = max(ans,cnt)

n, m = map(int,input().split())
maps = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0

for _ in range(n):
    maps.append(list(map(int,input().split())))


def makingWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0 :
                maps[i][j] = 1
                makingWall(cnt+1)
                maps[i][j] = 0

makingWall(0)
print(ans)

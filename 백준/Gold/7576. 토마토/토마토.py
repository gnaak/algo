'''
백준 골드 5
토마토
'''

import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int,input().split()) # 가로 칸 수, 세로 칸 수
box = []
for _ in range(n):
    a = list(map(int,input().split()))
    box.append(a)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
queue = deque([])

def bfs():
    for y in range(n):
        for x in range(m):
            if box[y][x] == 1:
                queue.append((y,x))
    while queue:
        ay, ax = queue.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0<=nx<m and 0<=ny<n and box[ny][nx] == 0:
                box[ny][nx] = box[ay][ax] +1
                queue.append((ny,nx))

bfs()

answer = 0
for y in range(n):
    for x in range(m):
        if box[y][x] == 0:
            answer = -1
            break
        else:
            cnt = max(cnt, box[y][x])

if answer:
    print(answer)
else:
    print(cnt-1)

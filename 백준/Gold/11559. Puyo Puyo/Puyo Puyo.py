# Puyo Puyo

import sys
input = sys.stdin.readline
from collections import deque

def pang(y,x):
    visited = [[0]*6 for _ in range(12)]
    queue = deque([(y,x)])
    cnt = 0
    tmp = []

    while queue:
        y, x = queue.popleft()
        tmp.append((y,x))
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<12 and 0<=nx<6 and visited[ny][nx] == 0 and board[ny][nx] == board[y][x]:
                queue.append((ny,nx))
                visited[ny][nx] = 1
        cnt +=1

    tmp.sort(reverse=True)
    a = board
    if cnt >= 4:
        for y,x in tmp:
            board[y][x] = "."

        return 1

    return 0

def pullDown():
    a = board
    for x in range(6):
        empty_row = 11  # 맨 아래부터 채워나갈 빈 위치
        for y in range(11, -1, -1):
            if board[y][x] != ".":
                board[empty_row][x], board[y][x] = board[y][x], board[empty_row][x]
                empty_row -= 1


board = [list(map(str,input().strip())) for _ in range(12)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
while 1:
    hasPang = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                hasPang = max(hasPang,pang(i,j))

    if not hasPang:
        break

    pullDown()
    cnt += 1


print(cnt)

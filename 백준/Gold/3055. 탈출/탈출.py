import sys
from collections import deque

input = sys.stdin.readline

def water_move():
    for _ in range(len(water)):
        y, x = water.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == '.':
                board[ny][nx] = '*'
                water.append((ny, nx))

def dochi_move():
    global flag
    for _ in range(len(dochi)):
        y, x = dochi.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if board[ny][nx] == 'D':  # 목적지 도착
                    flag = True
                    return
                if board[ny][nx] == '.':  # 빈 칸 이동
                    board[ny][nx] = 'S'
                    dochi.append((ny, nx))

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dochi = deque()
water = deque()
s_position_x, s_position_y = 0, 0

for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            s_position_x, s_position_y = i, j
        elif board[i][j] == '*':
            water.append((i, j))

dochi.append((s_position_x, s_position_y))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

time = 0
flag = False

while dochi:
    time += 1
    water_move()  # 물 확산
    dochi_move()  # 고슴도치 이동
    if flag:  # 목적지 도달
        print(time)
        break

if not flag:
    print("KAKTUS")

'''
백준 골드 5
로봇 청소기
'''

import sys
sys.stdin.readline

n, m = map(int,input().split())
y,x,d = map(int,input().split()) # 로봇 위치 y, x, 방향 d
board = [list(map(int,input().split())) for _ in range(n)] # 청소해야 하는 구역
cnt = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]

while 1:
    if board[y][x] == 0 :
        cnt +=1
        board[y][x] = 2
        flag = 0
    for i in range(1,5):    # 방향 변환
        ny = y + dy[(d-i)%4]
        nx = x + dx[(d-i)%4]
        if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0 :
            d = d-i
            y = ny
            x = nx
            flag = 1
            break

    if flag == 0: # 청소할 경우가 없는 경우
        ny = y - dy[d%4]
        nx = x - dx[d%4]
        if 0<=ny<n and 0<=nx<m :
            if board[ny][nx] == 1 :
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)



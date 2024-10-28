# 사탕 게임

import sys
input = sys.stdin.readline

def bomboni():
    mx = 0

    for y in range(n):
        for x in range(n):
            for k in range(2):
                ny, nx = y + dy[k], x + dx[k]
                if 0<=ny<n and 0<=nx<n and board[ny][nx] != board[y][x]:
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                    mx = max(mx,check())
                    a = board
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

    return mx


def check():
    max_cnt = 0

    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt_row += 1
            elif board[i][j] != board[i][j-1]:
                max_cnt = max(cnt_row, max_cnt)
                cnt_row = 1

            if board[j][i] == board[j-1][i]:
                cnt_col +=1
            elif board[j][i] != board[j-1][i]:
                max_cnt = max(cnt_col, max_cnt)
                cnt_col = 1

        max_cnt = max(max_cnt,cnt_col,cnt_row)

    return max_cnt

n = int(input())
board = [list(map(str,input().strip())) for _ in range(n)]
dx = [1,0]
dy = [0,1]
print(bomboni())
# 숫자판 점프

import sys
input = sys.stdin.readline

def dfs(cur,y,x,depth):
    if depth == 6 :
        result.add(cur)
        return

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<5 and 0<=nx<5 :
            dfs(cur + str(board[ny][nx]), ny, nx, depth + 1)


board = [list(map(int,input().split())) for _ in range(5)]
result = set()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(5):
    for j in range(5):
        dfs(str(board[i][j]), i,j,1)

print(len(result))
# 피자

import sys
input = sys.stdin.readline

r, c, w = map(int,input().split())
l = r+w
board = [[0]*(l) for _ in range(l)]
board[1][0] = 1

for i in range(2,l):
    board[i][0] = 1
    for j in range(1,l-1):
        board[i][j] = board[i-1][j] + board[i-1][j-1]

ans = 0
a = 1
for i in range(r, l):
    for j in range(c-1,c+a-1):
        ans += board[i][j]
    a+=1

print(ans)
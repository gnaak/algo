# 이동하기
# 가져갈 수 있는 사탕의 최대값
# 이동은 오른쪽, 아래, 우측 대각선만 가능

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = board[0][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1] + board[0][i]

for i in range(1,n):
    for j in range(m):
        if j>=1 :
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + board[i][j]
        else:
            dp[i][j] = dp[i-1][j] + board[i][j]

print(dp[-1][-1])
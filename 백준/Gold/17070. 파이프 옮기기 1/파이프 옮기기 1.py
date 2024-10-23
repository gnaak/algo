# 파이프 옮기기 1

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

# 가장 첫 파이프는 (0,0), (0,1)을 차지하고 방향은 가로
# 어차피 뒷 부분은 따라오는 거기 때문에 0,1 만 신경쓰면 된다?

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1 # [y,x,dir] 0 = 가로, 1 = 세로, 2 = 대각선
for k in range(2,n):
    if board[0][k] == 0 :
        dp[0][k][0] += dp[0][k-1][0]

for i in range(1,n):
    for j in range(1,n):
        if board[i][j] == 0 :
            if board[i][j-1] == 0 :
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
            if board[i-1][j] == 0:
                dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
            if board[i-1][j] == 0 and board[i][j-1] == 0 :
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(map(int,dp[n-1][n-1])))
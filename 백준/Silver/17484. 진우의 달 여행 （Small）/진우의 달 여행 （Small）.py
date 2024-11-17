# 진우의 달 여행

import sys
input = sys.stdin.readline
inf = float('inf')
n, m = map(int,input().split())
trip = [list(map(int,input().split())) for _ in range(n)]
dp = [[[inf, inf, inf] for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = trip[0][j]

for i in range(m):
    dp[1][i][1] = trip[0][i] + trip[1][i]
    if i - 1 >= 0 :
        dp[1][i][0] = trip[0][i-1] + trip[1][i]
    if i + 1 < m :
        dp[1][i][2] = trip[0][i+1] + trip[1][i]

for i in range(2,n):
    for j in range(m):
        if j - 1 >= 0 :
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + trip[i][j]
        if j + 1 < m :
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + trip[i][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + trip[i][j]

ans = inf
for row in dp[n-1]:
    for a in row:
        if ans > a:
            ans = a

print(ans)
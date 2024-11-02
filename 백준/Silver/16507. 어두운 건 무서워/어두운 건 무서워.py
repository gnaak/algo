# 어두운 건 무서워

import sys
input = sys.stdin.readline

r, c, q = map(int,input().split())
a = [[0]*(c+1)]
for _ in range(r):
    a.append([0] + list(map(int,input().split())))

dp = [[0]*(c+1) for _ in range(r+1)]

for i in range(1,r+1):
    for j in range(1,c+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + a[i][j] - dp[i-1][j-1]

for _ in range(q):
    y1,x1,y2,x2 = map(int,input().split())
    print((dp[y2][x2]-dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1])// ((x2-x1+1)*(y2-y1+1)))



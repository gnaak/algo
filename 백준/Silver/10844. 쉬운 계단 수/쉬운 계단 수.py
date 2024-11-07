# 쉬운 계단 수

import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000000

dp = [[0]*10 for _ in range(n+1)]

# n이 1일때, 1~9
for i in range(1,10):
    dp[1][i] = 1

# n이 2 이상일 때, dp[1]의 마지막 자리수로 개수 결정됨
for i in range(2,n+1):
    # 0과 9는 앞자리 수가 1 or 8일때만 가능
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    # ex) 2는 앞 자리 수가 1 or 3
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%mod)


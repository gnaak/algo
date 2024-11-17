# 피보나치 비스무리한 수열

import sys
input = sys.stdin.readline

n = int(input())
dp = [1]*(117)

for i in range(4,n+1):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[n])
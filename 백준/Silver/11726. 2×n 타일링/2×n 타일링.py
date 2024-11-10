# 2 x n 타일링

import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
mod = 10007
if n == 1:
    print(1)
elif n == 2:
    print(2)
else :
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-1]%mod)
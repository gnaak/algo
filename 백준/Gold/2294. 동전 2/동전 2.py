# 동전2

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = set()
for i in range(n):
    coins.add(int(input()))

dp = [float('inf')]*(k+1)
dp[0] = 0
for i in range(1,k+1):
    for coin in coins:
        if i - coin >= 0 and dp[i] > dp[i-coin] + 1:
            dp[i] = dp[i-coin] + 1

print(dp[-1] if dp[-1] != float('inf') else -1)
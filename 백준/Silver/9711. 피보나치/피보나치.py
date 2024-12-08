# 피보나치

import sys
input = sys.stdin.readline

t = int(input())
dp = [0]*10001
dp[0], dp[1] = 1, 1
for j in range(2,10000):
    dp[j] = dp[j-1] + dp[j-2]
    
for i in range(1,t+1):
    p, q = map(int,input().split())


    print(f'Case #{i}: {dp[p-1]%q}')
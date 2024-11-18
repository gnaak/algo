# 정수 a를 k로 만들기

import sys
input = sys.stdin.readline

# 연산은 더하기 1, 곱하기 2
a, k = map(int,input().split())
dp = [0]*(k+1)
dp[a] = 1

for i in range(a+1, k+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i] and dp[i//2] != 0:
        dp[i] = dp[i//2] + 1

print(dp[k] -1)
# 퇴사 2

# n+1일째 되는날 퇴사를 할거다
# n일 동안 최대한 많은 상담을 하려고 한다.

import sys
input= sys.stdin.readline

n = int(input())
dp = [0]*(n+1) # 1일부터 n일까지 상담해서 벌 수 있는 비용

for i in range(1,n+1):
    time, pay = map(int,input().split())
    # 상담을 하는 경우
    if i + time <= n+1: # n일 안에 끝날 때,
        dp[i+time-1] = max(dp[i+time-1], dp[i-1] + pay)



    # 상담을 선택하지 않는 경우
    dp[i] = max(dp[i], dp[i-1])

print(dp[n])
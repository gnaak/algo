# 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [0]*n # 포도주의 개수

if n == 0 :
    print(0)
    sys.exit()
elif n == 1: # 와인이 한개면, 무조건 마심
    print(wines[0]) # (1)
elif n == 2: # 와인이 두개여도 무조건 마심
    print(wines[0] + wines[1]) # (1,2)
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(dp[1], wines[1] + wines[2], wines[0] + wines[2]) # (1,2), (2,3), (1,3)

    for i in range(3,n):
        # 3번째 전 + 이전 + 현재 , 2번째 전 + 현재, 바로 이전 값 유지 
        dp[i] += max(dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i], dp[i-1])

    print(dp[-1])
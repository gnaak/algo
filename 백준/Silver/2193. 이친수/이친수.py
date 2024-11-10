# 이친수
# 이친수는 0으로 시작하지 않는다.
# 이친수는 1이 연속해서 나오지 않는다.
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

if n == 1 or n ==2:
    print(1)
else:
    dp[1],dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])
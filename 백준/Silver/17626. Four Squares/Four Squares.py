# Four Squares

import sys
input = sys.stdin.readline

n = int(input())
# 최소값 구하기
dp = [float('inf')] * (n+1)

# 중복이 가능하니까 정순으로 가는게 맞을듯?
for i in range(1,n+1):
    if int(i**0.5) ** 2 == i :
        dp[i] = 1
    else:
        for j in range(1, int(i**0.5) + 1):
            if dp[i] > dp[i-j**2] + 1:
                dp[i] = dp[i-j**2] + 1

print(dp[n])
import sys
input = sys.stdin.readline

n = int(input())

dp = [float('inf')]*(n+1)
# 무게 0을 만들 수 있는 봉지의 개수는 0개
dp[0] = 0

sugars = [3, 5]
# 중복이 가능하니까 dp를 정순으로
for i in range(1, n+1):
    for sugar in sugars:
        if i-sugar >= 0 and dp[i] > dp[i-sugar] + 1:
            dp[i] = dp[i-sugar] +1

print(dp[-1] if dp[-1] != float('inf') else -1)
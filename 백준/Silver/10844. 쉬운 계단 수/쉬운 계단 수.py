import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n+1)] # 0부터 9까지는 마지막 자리수 값
# n+1은 최종값
for i in range(1, 10):
    dp[1][i] = 1

for j in range(2,n+1):
    dp[j][0] = dp[j-1][1]
    dp[j][9] = dp[j-1][8]
    for i in range(1,9):
        dp[j][i] = dp[j-1][i-1] + dp[j-1][i+1]

print(sum(dp[n])%1000000000)
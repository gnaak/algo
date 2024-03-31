'''
백준 실버 3
계단 오르기
'''

n = int(input()) # 계단의 개수
stairs = [0]*301
for i in range(1,n+1):
    stairs[i] = int(input())

dp = [0]*301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2]+stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[n])
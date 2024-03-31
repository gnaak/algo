'''
백준 실버 5
피보나치수 4
'''

n = int(input())
dp = [0]*1000000

for i in range(n+1):
    dp[0] = 0
    dp[1] = 1
    if i > 1 :
        dp[i] = dp[i-1]+dp[i-2]

print(dp[n])
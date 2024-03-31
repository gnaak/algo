'''
백준 실버 3
퇴사
'''

n = int(input())
list = []
for _ in range(n):
    a, b = map(int,input().split())
    list.append([a,b])

dp = [0]*(n+1)

# top-down
for i in range(n-1, -1, -1):
    if i+list[i][0] > n :
        dp[i] = dp[i+1] # 상담 진행 x
    else:
        dp[i] = max(dp[i+1], list[i][1] + dp[i+list[i][0]])

print(dp[0])
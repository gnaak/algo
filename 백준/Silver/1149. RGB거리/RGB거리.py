'''
백준 실버 1
RGB 거리
'''

n = int(input()) # 집의 수
costs = []
dp = [[0]*3 for _ in range(n)]
for _ in range(n):
    r, g, b = map(int,input().split())
    costs.append([r,g,b])
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]


for i in range(1,n):
    dp[i][0] = costs[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = costs[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = costs[i][2]+min(dp[i-1][0],dp[i-1][1])

print(min(dp[n-1]))
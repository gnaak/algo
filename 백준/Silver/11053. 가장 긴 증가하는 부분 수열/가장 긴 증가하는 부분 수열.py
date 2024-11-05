# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n

for i in range(n):
    for j in range(i+1,n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[i]+1, dp[j])
            
print(max(dp))
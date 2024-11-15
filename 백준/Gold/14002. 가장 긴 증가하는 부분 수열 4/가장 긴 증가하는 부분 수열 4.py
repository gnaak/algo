# 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

k = max(dp)
print(k)
ans = []
for i in range(n-1,-1,-1):
    if dp[i] == k:
        ans.append(arr[i])
        k -= 1
print(' '.join(map(str,ans[::-1])))
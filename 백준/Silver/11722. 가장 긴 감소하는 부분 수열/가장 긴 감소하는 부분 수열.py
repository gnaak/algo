# 가장 긴 감소하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [1]*n

for i in range(1, n):
    # 이전 값들만 비교해서,
    for j in range(i-1,-1,-1):
        # i가 더 작다면,
        if a[i] < a[j]:
            if dp[i] < dp[j]+1 :
                dp[i] = dp[j]+1 

print(max(dp))
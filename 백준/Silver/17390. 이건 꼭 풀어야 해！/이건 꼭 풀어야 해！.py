# 이건 꼭 풀어야 해!

# 길이 n짜리 수열a를 만들고, a를 비내림차순해서 수열 b를 만들었다
# L R : BL~BR까지 더한 값을 출력

import sys
input = sys.stdin.readline

n, q = map(int,input().split())
a = [0] + list(map(int,input().split()))
a.sort()
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = dp[i-1] + a[i]
for _ in range(q):
    l, r = map(int,input().split())
    print(dp[r] - dp[l-1])

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

# DP 배열 계산
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

# LIS 길이 출력
k = max(dp)
print(k)

# LIS 수열 역추적
ans = []
for i in range(n - 1, -1, -1):
    if dp[i] == k:
        ans.append(arr[i])
        k -= 1

# 결과 출력
print(' '.join(map(str, ans[::-1])))

import sys 
input = sys.stdin.readline 

n, k = map(int, input().split())  # 필요한 n개의 물건, 최대 무게 k
dp = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())  # 물건의 무게 w, 가치 v
    for i in range(k, w - 1, -1):  # 가능한 무게 역순으로 순회
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])

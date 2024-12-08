import sys
input = sys.stdin.readline

# 입력: 초기 투자 금액 h, 투자 기간 y
h, y = map(int, input().split())

# dp[i]: i년 후 얻을 수 있는 최대 금액
dp = [0] * (y + 1)
dp[0] = h  # 초기 금액

# DP 계산
for i in range(y + 1):
    if i + 1 <= y:  # 1년 투자
        dp[i + 1] = max(dp[i + 1], int(dp[i] * 1.05))
    if i + 3 <= y:  # 3년 투자
        dp[i + 3] = max(dp[i + 3], int(dp[i] * 1.20))
    if i + 5 <= y:  # 5년 투자
        dp[i + 5] = max(dp[i + 5], int(dp[i] * 1.35))

# 결과 출력
print(dp[y])

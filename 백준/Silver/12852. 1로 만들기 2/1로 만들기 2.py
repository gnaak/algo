import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())

# DP 테이블 초기화
inf = float('inf')
dp = [inf] * (n + 1)
dp[1] = 0

# DP 계산
for i in range(1, n):
    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)

# 경로 추적
def track(n):
    path = [n]  # 경로 리스트에 최종 값을 먼저 추가
    while n > 1:
        if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
            n //= 3
        elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
            n //= 2
        else:
            n -= 1
        path.append(n)
    return path  # 경로를 뒤집어서 반환

# 결과 출력
print(dp[n])  # 최소 연산 횟수 출력
print(*track(n))  # 경로 출력

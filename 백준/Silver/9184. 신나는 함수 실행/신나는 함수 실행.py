import sys
input = sys.stdin.readline

# 메모이제이션을 위한 3차원 배열 초기화 (-1은 아직 계산되지 않았음을 의미)
dp = [[[-1] * 21 for _ in range(21)] for __ in range(21)]

def w(a, b, c):
    # 이미 계산된 값이 있으면 바로 반환
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c] != -1:
        return dp[a][b][c]

    # 메모이제이션 없을 경우 계산
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

# 입력 처리 및 출력
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

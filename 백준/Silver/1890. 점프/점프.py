import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # dp[y][x]: (y, x)까지 도달하는 경로의 개수
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for y in range(n):
        for x in range(n):
            if y == n - 1 and x == n - 1:
                continue
            jump = board[y][x]
            if y + jump < n:  # 아래로 이동
                dp[y + jump][x] += dp[y][x]
            if x + jump < n:  # 오른쪽으로 이동
                dp[y][x + jump] += dp[y][x]

    return dp[n - 1][n - 1]

print(solve())

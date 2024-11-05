# 구간 합 구하기 5
# n*n 크기의 표에서 x1,y1 부터 x2,y2까지 합을 구하는 프로그램을 작성

import sys
input = sys.stdin.readline

def sum():
    n, m = map(int, input().split())
    a = [[0] * (n + 1)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(n):
        a_row = [0] + [int(x) for x in input().split()]
        a.append(a_row)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + a[i][j]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
sum()
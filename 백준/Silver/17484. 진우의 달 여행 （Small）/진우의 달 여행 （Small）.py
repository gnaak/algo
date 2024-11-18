# 진우의 달 여행

import sys
input = sys.stdin.readline

def moon_travel(depth, dir, current, x):
    global fuel

    # 마지막 행에 도달한 경우
    if depth == n - 1:
        fuel = min(fuel, current)
        return

    # 오른쪽 이동
    if dir != 1 and x + 1 < m:
        moon_travel(depth + 1, 1, current + board[depth + 1][x + 1], x + 1)

    # 아래로 이동
    if dir != 2:
        moon_travel(depth + 1, 2, current + board[depth + 1][x], x)

    # 왼쪽 이동
    if dir != 3 and x - 1 >= 0:
        moon_travel(depth + 1, 3, current + board[depth + 1][x - 1], x - 1)

# 입력 처리
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

fuel = float('inf')

# 첫 번째 행에서 시작하는 모든 경우 탐색
for i in range(m):
    moon_travel(0, 0, board[0][i], i)

print(fuel)

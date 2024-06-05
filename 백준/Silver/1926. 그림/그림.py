'''
백준 실버 1
그림
'''

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = [(x,y)]
    board[x][y] = 0
    area = 1  # 시작점도 포함하므로 초기값은 1

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 1:
                queue.append((dx, dy))
                board[dx][dy] = 0
                area += 1  # 그림의 넓이 갱신

    return area


n, m = map(int, input().split())  # n은 세로 길이, m은 가로 길이
board = [list(map(int, input().split())) for _ in range(n)]

nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]

total = 0
maxpic = 0

for i in range(n):  # 세로 순회
    for j in range(m):  # 가로 순회
        if board[i][j] == 1:  # 그림 영역이면 bfs 함수 호출
            total += 1  # 그림의 개수 1 추가
            maxpic = max(maxpic, bfs(i, j))

print(total)
print(maxpic)

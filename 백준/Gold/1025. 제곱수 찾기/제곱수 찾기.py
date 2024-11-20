# 제곱수 찾기

import sys
input = sys.stdin.readline
from math import sqrt
def check(tmp):
    if int(sqrt(int(tmp)))**2 == int(tmp):
        return True
    else:
        return False
n, m = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]

ans = -1
for i in range(n):
    for j in range(m):
        for diff_y in range(-n, n):
            for diff_x in range(-m, m):
                y, x = i, j
                tmp = ''
                if diff_y ==0 and diff_x == 0:
                    continue
                while 0<=y<n and 0<=x<m:
                    tmp += str(board[y][x])
                    if check(tmp):
                        ans = max(ans, int(tmp))
                    y += diff_y
                    x += diff_x
print(ans)
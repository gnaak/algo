# 행렬 곱셈

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
m, k = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

ans = [[] for _ in range(n)]
for i in range(n):
    for l in range(k):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]*b[j][l]
        ans[i].append(tmp)

for an in ans:
    print(*an)
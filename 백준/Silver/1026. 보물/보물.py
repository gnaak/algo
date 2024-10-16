# 보물

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
c = sorted(b)

ans = 0
for i in range(n):
    ans += a[i]*c[i]

print(ans)
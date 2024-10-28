# 수 이어쓰기

import sys
input = sys.stdin.readline

n = int(input())
ans = 0
length = 1
start = 1

while start <= n:
    end = min(n, start * 10 - 1)
    ans += (end - start + 1) * length
    length += 1
    start *= 10

print(ans)

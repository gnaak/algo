# 수열

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
temps = list(map(int,input().split()))

standard = sum(temps[:k])
max_temp = standard
for end in range(k,n):
    standard += temps[end] - temps[end-k]
    if standard > max_temp:
        max_temp = standard

print(max_temp)
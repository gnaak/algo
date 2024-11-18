# 피자

import sys
input = sys.stdin.readline

n = int(input())
a = 0

for i in range(2, n+1):
    a += i-1

print(a)
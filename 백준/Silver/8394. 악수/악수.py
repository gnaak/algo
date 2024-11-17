# 악수

import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

a, b = 1, 1

for i in range(2, n+1):
    a, b = b%10, (a+b)%10

print(b)
# 피보나치는 지겨웡~

import sys
input = sys.stdin.readline

n = int(input())
a, b = 1, 1
mod = 1000000007
for _ in range(2,n+1):
    a, b = b%mod, (a + b + 1)%mod

print(b)
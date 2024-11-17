# 피보나치 수 7

import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1
mod = 1000000007
for _ in range(2,n+1):
    a, b = b%mod, (a + b)%mod

print(b if n!=0 else a)
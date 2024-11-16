import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000000

if n == 0:
    print(0)
    print(0)
else:
    sign = 1 if n > 0 else (-1 if abs(n) % 2 == 0 else 1)
    print(sign)

    n = abs(n)
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b % mod, (a + b) % mod
    print(b)

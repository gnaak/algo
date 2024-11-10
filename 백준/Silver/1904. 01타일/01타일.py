
import sys
input = sys.stdin.readline

def calc(n):
    mod = 15746

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a,b = 1, 2
        for i in range(n-2):
            a, b = b, (a + b) % mod
        return b

n = int(input())
print(calc(n))



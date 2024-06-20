import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    prev2 = 1
    prev1 = 2
    current = 0

    for i in range(3, n+1):
        current = (prev2 + prev1) % 15746
        prev2 = prev1
        prev1 = current

    print(current)

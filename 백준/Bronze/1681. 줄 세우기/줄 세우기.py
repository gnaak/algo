import sys
input = sys.stdin.readline

n, l = map(int,input().split())
current = 1
for i in range(n):
    while str(l) in str(current):
        current += 1

    current += 1

print(current - 1)
import sys
input = sys.stdin.readline

n, l = map(int,input().split())
current = 1
label = [0]*n
for i in range(n):
    while str(l) in str(current):
        current += 1

    label[i] = current
    current += 1

print(max(label))
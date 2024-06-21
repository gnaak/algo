import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(float(input()))

for i in range(1,n):
    lst[i] = max(lst[i], lst[i]*lst[i-1])

print('%0.3f' % max(lst))

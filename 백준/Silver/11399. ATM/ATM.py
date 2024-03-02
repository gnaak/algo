import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

t = [0]*n
t[0] = arr[0]

for i in range(1,n):
    t[i] = t[i-1] + arr[i]

print (sum(t))
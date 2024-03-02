import sys
input = sys.stdin.readline

def f(i,m):
    if i == m:
        print(*tmp)
        return
    else:
        for k in arr:
            tmp[i] = k
            if tmp[i] >= tmp[i-1]:
                f(i+1, m)
            tmp[i] = 0
n, m = map(int,input().split())
arr = [i for i in range(1, n+1)]
tmp = [0]*m
f(0,m)
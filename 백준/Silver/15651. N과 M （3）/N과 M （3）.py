def f(i,m):
    if i == m:
        print(*tmp)
        return
    else:
        for k in arr:
            tmp[i]=k
            f(i+1,m)


import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [i for i in range(1,n+1)]
tmp = [0]*m
f(0,m)

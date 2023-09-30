def f(i,m):
    if i == m:
        print(*tmp)
        return
    else:
        for k in arr:
            tmp[i]=k
            f(i+1,m)
            tmp[i]=0

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
tmp = [0]*m
f(0,m)

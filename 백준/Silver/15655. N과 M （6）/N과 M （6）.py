import sys
input = sys.stdin.readline

def f(i,m):
    if i == m:
        print(*tmp)
        return
    else:
        for k in arr:
            if k not in tmp:
                if tmp[i-1] < k:
                    tmp[i] = k
                    f(i+1, m)
                    tmp[i] = 0

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
tmp = [0]*m
f(0,m)

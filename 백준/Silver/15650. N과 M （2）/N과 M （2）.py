import sys
input = sys.stdin.readline

def f(start):
    if len(s) == m:
        print(*s)
        return
    else:
        for i in range(start,n+1):
            if i not in s:
                s.append(i)
                f(i+1)
                s.pop()

n, m = map(int,input().split())
s = []
f(1)
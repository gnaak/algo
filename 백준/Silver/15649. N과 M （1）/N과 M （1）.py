import sys
input = sys.stdin.readline

def f():
    if len(s) == m:
        print(*s)
        return
    else :
        for i in range(1,n+1):
            if i not in s:
                s.append(i)
                f()
                s.pop()


n, m = map(int,input().split())
s = []
f()
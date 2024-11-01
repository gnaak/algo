# 블로그

import sys
input = sys.stdin.readline

def blog():
    
    n, x = map(int,input().split())
    visited = [0] + list(map(int,input().split()))
    tot_visited = [0]*(n+1)
    tot_visited[0] = 0
    
    standard = sum(visited[:x])
    max_days = standard
    cnt = 1
    for i in range(x,n+1):
        standard += visited[i] - visited[i-x]
        if max_days < standard:
            max_days = standard
            cnt = 1
        elif max_days == standard:
            cnt += 1
    
    print(max_days if max_days > 0 else 'SAD')
    print(cnt if max_days > 0 else '')

blog()

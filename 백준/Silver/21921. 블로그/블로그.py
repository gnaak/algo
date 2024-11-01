# 블로그

import sys
input = sys.stdin.readline


n, x = map(int,input().split())
visited = [0] + list(map(int,input().split()))
tot_visited = [0]*(n+1)
tot_visited[0] = 0
for i in range(1,n+1):
    tot_visited[i] = tot_visited[i-1] + visited[i]

max_days = 0
cnt = 1
for i in range(x,n+1):
    if i >= x-1:
        x_days = tot_visited[i] - tot_visited[i-x]
        if x_days > max_days:
            max_days = x_days
            cnt = 1
        elif x_days == max_days:
            cnt += 1

print(max_days if max_days > 0 else "SAD")
print(cnt if max_days > 0 else '')
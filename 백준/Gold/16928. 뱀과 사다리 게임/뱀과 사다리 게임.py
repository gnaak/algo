# 뱀과 사다리 게임

# 게임의 크기는 10 * 10
# 사다리의 수 n, 뱀의 수  m
# n개의 줄에 사다리의 정보를 의미하는 x, y
# m개의 줄에 뱀의 정보를 의미하는 u, v

import sys
input = sys.stdin.readline
from collections import deque



def bfs(start,end):
    queue = deque()
    queue.append([start,0])
    while queue:
        now, value = queue.popleft()
        visited[now] = value

        if now == end :
            return visited[now]

        for i in range(1,7):
            nxt_now = now + i
            if nxt_now < 101 and visited[nxt_now] == 0:
                if nxt_now in ladders.keys():
                    nxt_now = ladders[nxt_now]
                visited[nxt_now] = value + 1
                queue.append([nxt_now, value+1])

n, m = map(int,input().split())
ladders = dict()
visited = [0 for _ in range(101)]
for _ in range(n):
    x, y = map(int,input().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int,input().split())
    ladders[u] = v


print(bfs(1,100))
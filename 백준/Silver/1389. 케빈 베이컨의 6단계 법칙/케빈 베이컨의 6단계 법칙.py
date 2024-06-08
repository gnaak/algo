'''
백준 실버 2
케빈 베이커의 6단계 법칙
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    visited = [0]*(n+1)
    visited[start] = 1
    while queue:
        me, cnt = queue.popleft()
        for friend in friends[me]:
            if visited[friend] == 0:
                visited[friend] = cnt+1
                queue.append((friend, cnt+1))
    link_list[start] = sum(visited)

n, m = map(int,input().split()) # n : 사람의 수, m : 친구 관계의 수
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

link_list = [0]*(n+1)
for i in range(1,n+1):
    bfs(i)

ans = 1
for idx in range(1,n+1):
    if link_list[ans] > link_list[idx]:
        ans = idx

print(ans)
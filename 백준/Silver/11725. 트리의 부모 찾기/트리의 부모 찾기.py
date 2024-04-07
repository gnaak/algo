'''
백준 실버 2
트리의 부모 찾기
'''

import sys
input = sys.stdin.readline
from collections import deque
queue = deque()
queue.append(1)
def bfs():
    while queue:
        a = queue.popleft()
        for k in nodes[a]:
            if parents[k] == 0:
                parents[k] = a
                queue.append(k)



n = int(input())
nodes = [[] for _ in range(n+1)]
parents = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

bfs()
for child in parents[2:]:
    print(child)
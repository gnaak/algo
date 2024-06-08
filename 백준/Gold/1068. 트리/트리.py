'''
백준 골드 5
트리
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(root):
    if d == root:
        return 0
    queue = deque([root])
    leaf_count = 0

    while queue:
        node = queue.popleft()
        if node == d:
            continue

        children = 0
        for child in graph[node]:
            if child != d:
                queue.append(child)
                children += 1

        if children == 0:
            leaf_count += 1

    return leaf_count


n = int(input()) # 노드의 총 개수
parents = list(map(int,input().split())) # 노드들
d = int(input()) # 지울 노드의 번호

graph = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        graph[parents[i]].append(i)

print(bfs(root))
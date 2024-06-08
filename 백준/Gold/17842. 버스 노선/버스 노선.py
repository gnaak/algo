'''
백준 골드 2
버스 노선
'''

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
edges = []

def find_min_route(n,edges):
    if n == 2:
        return 1
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    leaf_count = 0

    for node in range(n):
        if len(graph[node]) == 1:
            leaf_count += 1

    return (leaf_count + 1) // 2

for _ in range(n - 1):
    a, b = map(int, input().split())
    edges.append((a,b))

print(find_min_route(n,edges))

import sys
from collections import deque

input = sys.stdin.readline

def find_minimum_routes(n, edges):
    if n == 2:
        return 1
    
    # 트리의 인접 리스트를 만듭니다.
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 리프 노드의 개수를 셉니다.
    leaf_count = 0
    for node in range(n):
        if len(graph[node]) == 1:
            leaf_count += 1
    
    # 리프 노드의 개수를 반으로 나누어 최소 경로 개수를 계산합니다.
    return (leaf_count + 1) // 2

# 입력을 처리합니다.
n = int(input().strip())
edges = []
for _ in range(n-1):
    a, b = map(int, input().strip().split())
    edges.append((a, b))

# 최소 경로 개수를 찾습니다.
print(find_minimum_routes(n, edges))

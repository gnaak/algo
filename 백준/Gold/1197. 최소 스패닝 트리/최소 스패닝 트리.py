import sys
sys.stdin.readline
import heapq

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

chk = [0]*(v+1)
heap = [[0, 1]]
rs = 0
while heap:
    w, node = heapq.heappop(heap)
    if chk[node] == 0:
        chk[node] = 1
        rs += w
        for next_node, weight in graph[node]:
            if chk[next_node] == 0:
                heapq.heappush(heap, [weight, next_node])

print(rs)

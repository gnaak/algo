
import sys
input = sys.stdin.readline
import heapq
inf = float('inf')

def dijkstra(start):
    visited = [inf] * (n + 1)  # 방문 및 최소 거리 저장
    visited[start] = 0
    heap = [(0, start)]
    collected_items = items[start - 1]  # 현재 지역의 아이템 수집

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > visited[current_node]:
            continue

        for neighbor, distance in graph[current_node]:
            total_dist = current_dist + distance
            if total_dist < visited[neighbor]:
                visited[neighbor] = total_dist
                heapq.heappush(heap, (total_dist, neighbor))

    return visited

n, m, r = map(int, input().split())  # 지역 수, 수색 범위, 길 개수
items = list(map(int, input().split()))  # 각 지역의 아이템 수
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

max_items = 0
for start in range(1, n + 1):
    collected = 0
    dist_list = dijkstra(start)
    for i in range(len(dist_list)):
        if dist_list[i] <= m:
            collected += items[i-1]
    max_items = max(max_items, collected)


print(max_items)

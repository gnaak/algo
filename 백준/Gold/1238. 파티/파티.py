# n개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

# x번 마을에 모여서 파티를 버리기로 했다. 마을 사이에는 총 m개의 단방향 도로들이 있고, i번째 길을 지나는데 ti를 소모한다
# 마을에 갓다가, 다시 마을로 돌아와야 한다.

# 도로는 단방향이기 때문에, 오고 가는 길이 다를 수 있다. 가장 많은 시간을 소비하는 학생은 누구인가 ?

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))

    while queue:
        dist, current_node = heapq.heappop(queue)
        if distance[current_node] < dist:
            continue
        for next_node, value in graph[current_node]:
            cost = dist + value
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue,(cost,next_node))

    return distance
n, m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, value = map(int,input().split())
    graph[start].append((end, value))

max_time = 0
for i in range(1,n+1):
    dist = dijkstra(i)[x]
    dist_reverse = dijkstra(x)[i]
    if max_time <= dist + dist_reverse:
        max_time = dist + dist_reverse

print(max_time)
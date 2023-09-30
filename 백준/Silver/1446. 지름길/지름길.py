import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    q = [(0,0)]
    distance[0] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in g[now]:
            next_node = next[1]
            cost = next[0]
            if next_node - now < cost or d < next_node:
                continue
            new_cost = cost + dist

            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(q,(new_cost, next_node))

    return distance[d]

n, d = map(int,input().split()) # 지름길의 개수 n, 고속도로의 길이  150
g = [[] for _ in range(d+1)]
for _ in range(n):
    f, t, w = map(int,input().split())
    if t > d:
        continue
    g[f].append((w,t))
for i in range(d+1):
    g[i].append((1,i+1))
distance = [float('inf')]*(d+1)
print(dijkstra())
# print(g)
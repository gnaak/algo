import heapq
import sys
input = sys.stdin.readline


def dijkstra(s,e):
    q = []
    heapq.heappush(q, (0,s))
    d[s] = 0
    while q:
        dst, now = heapq.heappop(q)

        if d[now] < dst:
            continue

        for next in g[now]:
            next_node = next[1]
            cost = next[0]
            new_cost = cost + dst

            if d[next_node] <= new_cost:
                continue
            d[next_node] = new_cost
            heapq.heappush(q,(new_cost,next_node))
    return d[e]

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
d = [100000000001]*(n+1)
for _ in range(m):
    f,t,w = map(int,input().split())
    g[f].append((w,t))
s, e = map(int,input().split())
print(dijkstra(s,e))
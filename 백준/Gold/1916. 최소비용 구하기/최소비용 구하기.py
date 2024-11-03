# 최소 비용 구하기
# 가중치가 있으니까 다익스트라
import sys
input = sys.stdin.readline
import heapq
inf = 1e9

def travel(start, end):
    queue = []
    heapq.heappush(queue,(0,start))
    visited[start] = 0
    while queue:
        cost, current = heapq.heappop(queue)

        if visited[current] < cost:
            continue

        for next in buses[current]:
            nxt_stop, fee = next
            new_cost = cost + fee

            if visited[nxt_stop] > new_cost:
                visited[nxt_stop] = new_cost
                heapq.heappush(queue,(new_cost, nxt_stop))

    return visited[end]


n = int(input()) # 도시의 개수 n
m = int(input()) # 버스의 개수 m
buses = [[] for _ in range(n+1)]
visited = [inf]*(n+1)
for _ in range(m):
    u, v, w = map(int,input().split())
    buses[u].append((v, w))
start, end = map(int,input().split())
min_cost = travel(start, end)
print(min_cost)
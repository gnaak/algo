# 최소비용 구하기 2

# n 개의 도시, m개의 버스
# a번째 도시에서 b도시까지 가는 최소비용과 경로

# 가중치가 있으면 다익스트라

import sys
input = sys.stdin.readline
import heapq
inf = 1e9
def dijk(start):
    cost = [inf]*(n+1)
    prev = [-1]*(n+1)
    cost[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        fee, current = heapq.heappop(queue)

        if cost[current] < fee :
            continue

        for nxt, fee2 in buses[current]:
            total = fee+fee2
            if cost[nxt] > total:
                cost[nxt] = total
                prev[nxt] = current
                heapq.heappush(queue,(total,nxt))

    return cost, prev

def path(prev, end):
    path = []

    while end != -1:
        path.append(end)
        end = prev[end]
    path.reverse()

    return path
n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
buses = [[] for _ in range(n+1)] # 1번 도시부터 n번 도시까지 버스 경로 표시
for _ in range(m):
    start, end, cost = map(int,input().split())
    buses[start].append((end, cost))

start, end = map(int,input().split()) # 출발도시, 도착도시
cost,prev = dijk(start)
city = path(prev,end)
print(cost[end])
print(len(city))
print(*city)
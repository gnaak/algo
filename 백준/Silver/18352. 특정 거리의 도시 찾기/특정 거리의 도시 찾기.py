import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) 

n,m,k,x = map(int, input().split()) # k=찾을거리, x=출발

graph = [[] for _ in range(n+1)] # 그래프
distance = [INF] * (n+1) 

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append((v,1)) # 거리는 1로 고정

def dijkstra(start):
    queue = [] 
    heapq.heappush(queue, (0,start)) 
    distance[start] = 0 

    while queue:
        dist, node = heapq.heappop(queue) 

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1] 
           
            if cost < distance[next[0]]: 
                distance[next[0]] = cost 
                heapq.heappush(queue, (cost, next[0])) 

dijkstra(x)

if k not in distance:
    print(-1)

else:
    for i in range(1, len(distance)): 
        if distance[i] == k:
            print(i)
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대 값 설정


def dijkstra(start):
    distance = [INF] * (n + 1)  # 거리 테이블 무한대로 초기화
    distance[start] = 0  # 시작 지점의 거리는 0
    queue = []
    heapq.heappush(queue, (0, start))  # 시작 노드를 우선순위 큐에 삽입

    while queue:
        dist, now = heapq.heappop(queue)

        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for next_node, weight in graph[now]:
            cost = dist + weight

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return distance


# 입력 처리
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())  # 반드시 통과해야 하는 두 정점

# 1번 노드에서 모든 노드로 가는 최단 거리
dist_from_1 = dijkstra(1)
# v1에서 모든 노드로 가는 최단 거리
dist_from_v1 = dijkstra(v1)
# v2에서 모든 노드로 가는 최단 거리
dist_from_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> n 경로와 1 -> v2 -> v1 -> n 경로 계산
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

# 두 경로 중 작은 값을 선택
result = min(path1, path2)

# 경로가 없는 경우 -1 출력
if result >= INF:
    print(-1)
else:
    print(result)

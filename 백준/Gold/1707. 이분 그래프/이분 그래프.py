import sys
input = sys.stdin.readline
from collections import deque

def check_bipartite(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1  # 시작 정점을 1번 그룹에 할당

    while queue:
        node = queue.popleft()

        for nxt_node in nodes[node]:
            if visited[nxt_node] == 0:  # 아직 방문하지 않은 정점이면
                visited[nxt_node] = -visited[node]  # 현재 노드와 다른 그룹으로 할당
                queue.append(nxt_node)
            elif visited[nxt_node] == visited[node]:  # 인접한 노드가 같은 그룹이면 이분 그래프가 아님
                return False
    return True

k = int(input())  # 테스트 케이스 개수
for _ in range(k):
    V, E = map(int, input().split())  # 정점 V와 간선 E

    nodes = [[] for _ in range(V + 1)]  # 인접 리스트로 그래프 저장
    for __ in range(E):
        u, v = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)

    visited = [0] * (V + 1)  # 방문 여부 및 그룹 할당을 위한 배열
    is_bipartite = True

    for i in range(1, V + 1):
        if visited[i] == 0:  # 아직 방문하지 않은 정점에 대해
            if not check_bipartite(i):  # 이분 그래프가 아니면
                is_bipartite = False
                break

    if is_bipartite:
        print("YES")
    else:
        print("NO")

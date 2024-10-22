import sys
input = sys.stdin.readline

# 반복적인 DFS (스택 사용)
def dfs_stack(start):
    distances = [-1] * (n + 1)
    distances[start] = 0
    stack = [(start, 0)]  # (노드, 현재 거리)

    while stack:
        node, value = stack.pop()
        for child, weight in tree[node]:
            if distances[child] == -1:  # 아직 방문하지 않은 노드라면
                distances[child] = value + weight
                stack.append((child, distances[child]))

    return distances

n = int(input())  # 노드의 개수
tree = [[] for _ in range(n + 1)]

# 트리 정보 입력받기
for _ in range(n - 1):
    parent, child, value = map(int, input().split())
    tree[parent].append((child, value))
    tree[child].append((parent, value))  # 양방향 그래프

# 1. 임의의 노드(1번 노드)에서 가장 먼 노드 찾기 (DFS 1)
distances = dfs_stack(1)
start = distances.index(max(distances))

# 2. 그 노드에서 다시 가장 먼 노드를 찾기 (DFS 2)
distances = dfs_stack(start)

# 트리의 지름 (가장 멀리 있는 노드까지의 거리)
print(max(distances))

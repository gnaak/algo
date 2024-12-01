import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
order = 1  # 방문 순서를 기록하는 변수

# DFS 함수
def dfs(node):
    global order
    visited[node] = order
    for nxt in graph[node]:
        if visited[nxt] == 0:
            order += 1
            dfs(nxt)

# 그래프 입력 및 정렬
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort(reverse=True)

# DFS 실행
dfs(r)

# 결과 출력
print('\n'.join(map(str, visited[1:])))

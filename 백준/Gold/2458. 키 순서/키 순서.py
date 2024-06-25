import sys
input = sys.stdin.readline

def dfs(now, visit, graph):
    visit[now] = 1
    for nxt in graph[now]:
        if visit[nxt]:
            continue
        dfs(nxt, visit, graph)

def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        dfs(i, visited[i], graph)

    result = 0
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, N + 1):
            if visited[i][j] or visited[j][i]:
               cnt += 1
        if cnt == N:
            result += 1

    print(result)

solution()
n, m = map(int, input().split())  # n x m 크기의 배열
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[0]*m for _ in range(n)]
queue = [(0, 0)]  # 시작점을 큐에 추가
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = [(x, y, 1)]  # 시작점과 경로의 길이를 함께 저장
    visited[x][y] = 1
    while queue:
        x, y, distance = queue.pop(0)  # 큐에서 꺼내기
        if x == n - 1 and y == m - 1:  # 도착점에 도달하면 경로의 길이 반환
            return distance

        for i in range(4):  # 상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, distance + 1))  # 다음 칸과 경로의 길이 함께 저장
                visited[nx][ny] = 1

result = bfs(0, 0)
print(result)

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs(x, y):
        queue = [(x, y, 1)]
        visited[x][y] = True
        while queue:
            x, y, distance = queue.pop(0)
            if x == n - 1 and y == m - 1:
                return distance
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    queue.append((nx, ny, distance + 1))
                    visited[nx][ny] = 1
        return -1  
    
    return bfs(0, 0)

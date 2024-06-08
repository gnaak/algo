from collections import deque

def bfs():
    queue = deque([(0, 0, 1, 0)])  # 시작점과 카운트를 큐에 추가
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 벽을 부수고 방문한 경우와 부수지 않고 방문한 경우를 따로 저장
    visited[0][0][0] = 1  # 시작점 방문 처리
    while queue:
        y, x, cnt, breakcnt = queue.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 0 and visited[ny][nx][breakcnt] == 0:  # 이동 가능한 경우
                    queue.append((ny, nx, cnt + 1, breakcnt))
                    visited[ny][nx][breakcnt] = 1  # 방문 여부를 체크
                elif board[ny][nx] == 1 and breakcnt == 0 and visited[ny][nx][1] == 0:  # 벽을 한 번 깰 수 있는 경우
                    queue.append((ny, nx, cnt + 1, 1))
                    visited[ny][nx][1] = 1  # 벽을 깼으므로 방문 처리
    return -1

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs())

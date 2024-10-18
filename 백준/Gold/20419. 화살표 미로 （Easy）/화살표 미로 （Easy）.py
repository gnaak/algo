from collections import deque

def check():
    # 3D visited 배열로 주문서 개수까지 추적
    visited = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, k, k)])  # (r, c, left, right)
    visited[0][0][k] = 0  # (left, right) 주문서를 사용한 상태

    directions = {
        'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)
    }

    while queue:
        r, c, left, right = queue.popleft()

        # 도착 지점에 도달하면 True 반환
        if r == n - 1 and c == m - 1:
            return True

        # 현재 칸의 방향에 따른 이동
        direction = board[r][c]
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc
        
        # 그대로 이동 가능할 경우
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc][left] == -1:
            visited[nr][nc][left] = visited[r][c][left] + 1
            queue.append((nr, nc, left, right))

        # 주문서를 사용하여 이동할 수 있는 경우 처리
        # 시계방향 90도, 180도, 270도 회전 (right 사용)
        for use_right in range(1, 4):
            if right >= use_right:
                new_direction = rotate(direction, use_right, 'R')
                dr, dc = directions[new_direction]
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc][left] == -1:
                    visited[nr][nc][left] = visited[r][c][left] + 1
                    queue.append((nr, nc, left, right - use_right))

        # 반시계방향 90도, 180도, 270도 회전 (left 사용)
        for use_left in range(1, 4):
            if left >= use_left:
                new_direction = rotate(direction, use_left, 'L')
                dr, dc = directions[new_direction]
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc][left - use_left] == -1:
                    visited[nr][nc][left - use_left] = visited[r][c][left] + 1
                    queue.append((nr, nc, left - use_left, right))

    return False

def rotate(direction, times, turn_type):
    # direction을 times번 회전
    directions = ['U', 'R', 'D', 'L']
    idx = directions.index(direction)
    if turn_type == 'R':
        return directions[(idx + times) % 4]
    else:
        return directions[(idx - times) % 4]

# 입력 처리
n, m, k = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

if check():
    print("Yes")
else:
    print("No")

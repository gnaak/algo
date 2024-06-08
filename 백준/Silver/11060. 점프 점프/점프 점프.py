import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque([(0, 0)])  # 시작 지점, 점프 횟수
    visited = [False] * n
    visited[0] = True

    while queue:
        now, cnt = queue.popleft()
        if now == n - 1:
            return cnt
        for i in range(1, maze[now] + 1):
            next_pos = now + i
            if next_pos < n and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, cnt + 1))
    return -1

n = int(input())  # 1*n 크기의 미로
maze = list(map(int, input().split()))
print(bfs())

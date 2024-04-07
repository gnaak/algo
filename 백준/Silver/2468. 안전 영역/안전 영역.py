'''
백준 실버 1
안전 영역
'''

import sys
from collections import deque

input = sys.stdin.readline

def safety(height):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if areas[i][j] > height and not visited[i][j]:
                bfs(i, j, height, visited)
                cnt += 1
    return cnt

def bfs(x, y, height, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and areas[nx][ny] > height and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

n = int(input())
areas = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for height in range(101):
    max_cnt = max(max_cnt, safety(height))

print(max_cnt)


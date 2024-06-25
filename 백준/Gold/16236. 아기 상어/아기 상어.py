import sys
from collections import deque

input = sys.stdin.readline

# 무한대를 설정
INF = sys.maxsize

# BFS를 이용해 먹이까지의 거리 계산
def bfs():
    queue = deque([(now_y, now_x)])
    visited = [[-1] * n for _ in range(n)]
    visited[now_y][now_x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == -1:
                if sea[ny][nx] <= shark_size:  # 상어 크기보다 작거나 같은 위치로만 이동 가능
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
    return visited

# 먹이의 위치 확인(바로 먹을 수 있는 먹이만)
def fishing(visited):
    fishes = []
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if sea[i][j] != 0 and sea[i][j] < shark_size and visited[i][j] != -1:
                dist = visited[i][j]
                if dist < min_dist:
                    fishes = [(i, j, dist)]
                    min_dist = dist
                elif dist == min_dist:
                    fishes.append((i, j, dist))
    if fishes:
        return sorted(fishes, key=lambda x: (x[2], x[0], x[1]))[0]
    else:
        return False

# 입력 받기
n = int(input())  # n * n 크기의 어항
sea = [list(map(int, input().split())) for _ in range(n)]

now_x = 0
now_y = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 아기 상어 위치 파악
for y in range(n):
    for x in range(n):
        if sea[y][x] == 9:
            now_y, now_x = y, x
            sea[y][x] = 0  # 상어가 있던 지점을 0으로 설정

shark_size = 2
ate_fish = 0
total_time = 0

# 시뮬레이션 반복
while True:
    visited = bfs()
    result = fishing(visited)

    if result:
        now_y, now_x, move_time = result
        total_time += move_time
        sea[now_y][now_x] = 0  # 먹은 자리를 물고기를 치워준다
        ate_fish += 1

        if ate_fish == shark_size:  # 자신의 크기만큼 물고기를 먹으면 상어 크기 증가
            shark_size += 1
            ate_fish = 0
    else:
        print(total_time)
        break

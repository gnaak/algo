import sys
input = sys.stdin.readline
from collections import deque
inf = float('inf')

def bfs():
    max_distance = 0
    while sharks:
        y, x, depth = sharks.popleft()
        max_distance = max(max_distance, depth)  # 현재까지 가장 큰 거리 갱신
        for i in range(8):
            ny, nx = y +dy[i], x + dx[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] > depth +1 and board[ny][nx] == 0 :
                visited[ny][nx] = depth+1
                sharks.append((ny,nx,depth+1))
    return max_distance

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
sharks = deque()
visited = [[inf]*m for _ in range(n)]
dx, dy = [1,0,-1,0,1,1,-1,-1], [0,1,0,-1,1,-1,1,-1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            sharks.append((i,j,0))
            visited[i][j] = 0

print(bfs())
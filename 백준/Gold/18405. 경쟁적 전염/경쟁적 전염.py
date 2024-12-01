import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    for y in range(n):
        for x in range(n):
            if board[y][x] != 0:
                queue.append((y, x, board[y][x], 0)) 
    
    queue = deque(sorted(queue, key=lambda x: x[2]))
    
    while queue:
        y, x, virus, cur_time = queue.popleft()
        
        if cur_time == s:
            break
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                board[ny][nx] = virus
                queue.append((ny, nx, virus, cur_time + 1))

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, X, Y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

bfs()

print(board[X-1][Y-1])

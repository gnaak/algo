from collections import deque

def bfs():
    queue = deque()
    # Add all initial virus positions to the queue
    for y in range(n):
        for x in range(n):
            if board[y][x] != 0:
                queue.append((y, x, board[y][x], 0))  # (y, x, virus_type, time)
    
    # Sort the queue by virus type to ensure correct order of propagation
    queue = deque(sorted(queue, key=lambda x: x[2]))
    
    while queue:
        y, x, virus, time = queue.popleft()
        
        if time == s:  # Stop if we have reached the target time
            break
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                board[ny][nx] = virus
                queue.append((ny, nx, virus, time + 1))

# Input reading
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, X, Y = map(int, input().split())

# Directions for BFS
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# Perform BFS to spread the virus
bfs()

# Output the result at the given position
print(board[X-1][Y-1])

# 알고스팟

# 알고스팟 운영진들이 미로에 갇혓다.
# 미로는 n*m이며, 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 이동이 가능하지만, 부수지 않으면 이동이 안된다.
# 현재 1,1에 있는 운영진이 n,m으로 이동하려면 벽을 최소 몇개 부수어야 하는지 구하시오


import sys
input = sys.stdin.readline
import heapq
inf = int(1e9)

def dijk(y,x):
    distance = [[inf]*m for _ in range(n)]
    distance[y][x] = 0
    queue = []
    heapq.heappush(queue,(0,y,x))

    while queue:
        dist, cy, cx = heapq.heappop(queue)
        if distance[cy][cx] < dist:
            continue
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<m:
                cost = int(board[ny][nx]) + dist
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(queue,(cost,ny,nx))

    return distance


m, n = map(int,input().split())
board = [list(map(str,input().strip()))for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
a = dijk(0,0)
print(a[n-1][m-1])
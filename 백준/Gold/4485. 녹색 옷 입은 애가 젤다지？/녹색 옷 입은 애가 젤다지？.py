# 젤다의 전설에서 단위는 루피이다!
# 잃는 금액을 최소로 하여 동굴을 탈출
# 인데 어차피 다 -니까 다익스트라?

import sys
input = sys.stdin.readline
import heapq
inf = 1e9

def dijk(y,x):
    queue = []
    cost = [[inf] * (n+1) for _ in range(n+1)]
    cost[y][x] = board[y][x]
    heapq.heappush(queue,(cost[y][x], y, x))

    while queue:
        rob, y, x = heapq.heappop(queue)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n and cost[ny][nx] > rob +board[ny][nx]:
                cost[ny][nx] = rob +board[ny][nx]
                heapq.heappush(queue,(cost[ny][nx],ny,nx))

    return cost

tc = 1
while True:
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    if n == 0 :
        break
    
    print(f'Problem {tc}: {dijk(0,0)[n-1][n-1]}')

    tc += 1
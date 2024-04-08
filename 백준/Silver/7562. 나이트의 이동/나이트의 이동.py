import sys
input = sys.stdin.readline
from collections import deque
tc = int(input())
for _ in range(tc):
    queue = deque()

    def bfs():
        global cnt
        while queue:
            a, b = queue.popleft()
            if a == ga and b ==gb:
                return board[a][b]
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] ==0:
                    queue.append((nx,ny))
                    board[nx][ny] = board[a][b] +1

    n = int(input()) # n*n 체스판
    a,b = map(int,input().split()) # 현재 나이트가 존재하는 칸
    queue.append((a,b))
    ga, gb = map(int,input().split()) # 나이트가 이동하려고 하는 칸
    board = [[0]*(n) for _ in range(n)] # n*n 격자판
    board[a][b] = 1
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    cnt = 0

    print(bfs()-1)

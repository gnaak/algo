import sys
input = sys.stdin.readline
from collections import deque

while True:
    def island():
        while queue:
            y, x = queue.popleft()
            for i in range(8):
                nx = x +dx[i]
                ny = y +dy[i]
                if 0<=nx<w and 0<=ny<h and maps[ny][nx] == 1:
                    queue.append((ny,nx))
                    maps[ny][nx] = 0

    w, h = map(int, input().split())  # 너비 w, 높이 h
    if w == 0 and h == 0:
        break
    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))

    # 상하좌우 대각선 이동
    dx = [1,0,-1,0,1,-1,1,-1]
    dy = [0,1,0,-1,1,1,-1,-1]

    cnt = 0
    queue = deque()
    for y in range(h):
        for x in range(w):
            if maps[y][x] == 1 :  # 땅이면,
                cnt +=1
                queue.append((y,x))
                maps[y][x] = 0
                island()


    print(cnt)
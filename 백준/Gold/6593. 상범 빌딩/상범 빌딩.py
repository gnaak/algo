# 상범 빌딩

import sys
input = sys.stdin.readline
from collections import deque

def exit(start, end, count):
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    queue = deque([(start, count)])
    gf, gy, gx = end

    while queue :
        current, count = queue.popleft()
        f, y, x = current
        if f == gf and y == gy and x == gx:
            return f'Escaped in {count} minute(s).'


        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<r and 0<=nx<c and visited[f][ny][nx] == 0 and building[f][ny][nx] != '#':
                visited[f][ny][nx] = visited[f][y][x]+1
                queue.append(((f,ny,nx), count+1))
        if f + 1 < l and visited[f+1][y][x] == 0 and building[f+1][y][x] != '#':
            visited[f+1][y][x] = visited[f][y][x]+1
            queue.append(((f+1,y,x), count+1))

        if f - 1 >= 0 and visited[f - 1][y][x] == 0 and building[f - 1][y][x] != '#':
            visited[f - 1][y][x] = visited[f][y][x]+1
            queue.append(((f - 1, y, x), count + 1))

    return 'Trapped!'

while 1:
    l, r, c = map(int, input().split())
    # 상범 빌딩의 층 수, r, c는 한 층의 행과 열의 개수
    if l == 0 and r == 0 and c == 0:
        break
    else:
        building = []
        for i in range(l):
            building.append([list(map(str,input().strip())) for _ in range(r)])
            a = input()

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        start = ()
        end = ()
        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if building[i][j][k] == 'S':
                        start = (i,j,k)
                    elif building[i][j][k] == 'E':
                        end = (i,j,k)

        print(exit(start, end, 0)
              )


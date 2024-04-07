'''
백준 골드 5
적록색약
'''

import sys
from collections import deque
queue = deque()

def dfs(x,y,a):
    while queue:
        x, y, a = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 >nx or nx >=n or 0 > ny or ny >=n :
                continue
            if visited[nx][ny] == 0 and pic[nx][ny] == a :
                visited[nx][ny] = 1
                queue.append((nx,ny,a))

def dfs2(x,y,a):
    while queue:
        x, y, a = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 >nx or nx >=n or 0 > ny or ny >=n :
                continue
            if visited2[nx][ny] == 0:
                if (a =='R' or a == 'G') and (pic[nx][ny] == 'R' or pic[nx][ny] == 'G'):
                    visited2[nx][ny] = 1
                    queue.append((nx,ny,pic[nx][ny]))
                elif pic[nx][ny] == a:
                    visited2[nx][ny] = 1
                    queue.append((nx,ny,a))

n = int(input()) # 크기가 n*n인 그리드
pic = []
for _ in range(n):
    pic.append(list(map(str,input())))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]

cnt_o = 0
cnt_x = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            a = pic[i][j]
            queue.append((i,j,a))
            cnt_x +=1
            dfs(i,j,a)

for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            visited2[i][j] = 1
            a = pic[i][j]
            queue.append((i,j,a))
            cnt_o +=1
            dfs2(i,j,a)

print(cnt_x, end=" ")
print(cnt_o)
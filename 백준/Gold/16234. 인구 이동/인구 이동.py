# n * n 크기의 땅
# r행 c열에는 a[r][c]명이 살고 있다

# 두 나라의 인구 차이가 L 이상 R 이하라면, 국경선을 하루동안 연다
# 국경선이 열렸다면, 인구 이동을 시작한다
# 인접한 칸막을 이용해 이동할 수 있다면, 연합이 된다
# 연합의 인구수는 평균값이 된다
# 모든 국경선을 닫는다

# 며칠 동안 인구 이동이 발생하나요
import sys
input = sys.stdin.readline
from collections import deque

def imigrate(rows,cols,popu):
    for i in range(len(rows)):
        pop[rows[i]][cols[i]] = popu
    return pop
def search(row,col):
    union_cnt = 1
    queue = deque()
    queue.append([row,col])
    rows = [row]
    cols = [col]
    tot_pop = pop[row][col]
    visited[row][col] = 1
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            ny = row + dy[i]
            nx = col + dx[i]
            if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0:
                if abs(pop[ny][nx]-pop[row][col]) <= r and abs(pop[ny][nx]-pop[row][col])>= l:
                    queue.append([ny,nx])
                    visited[ny][nx] = 1
                    union_cnt += 1
                    tot_pop += pop[ny][nx]
                    rows.append(ny)
                    cols.append(nx)
    if union_cnt > 1:
        imigrate(rows,cols,tot_pop//union_cnt)
        return 1
    else:
        return 0

n, l, r = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
pop = []
for i in range(n):
    pop.append(list(map(int,input().split())))

move = 1
days = 0
while move: # 움직일 수 있으면 계속 움직임
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                if search(i,j):
                    ans += 1
    if ans == 0:
        move = 0
    else:
        days += 1

print(days)
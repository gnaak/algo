# 미세먼지 안녕!

# r*c인 집의 크기
# 공기청정기는 항상 1번열에 설치되어 있다
# a[r][c]는 미세먼지의 양

# 1초당

# 1. 미세먼지
# 미세먼지는 4방향으로 확산된다. 공기청정기가 있거나, 칸이 없으면 확산되지 않는다
# 확산되는 양은 a[r][c]/5이다. 소수점은 버린다.
# a[r][c]에 남은 미세먼지의 양은 a[r][c] - a[r][c]/5 * 확산된 방향의 개수

# 2. 공기청정기
# 공기청정기에서는 바람이 나오고 위쪽 공기청정기는 반시계, 아래쪽 공기청정기는 시계방향으로 순환한다.
# 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기로 들어간 미세먼지는 정화된다.

import sys
input = sys.stdin.readline

def spread():

    while dirt:
        y, x, value = dirt.pop()
        spread_cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<r and 0<=nx<c and room[ny][nx] != -1 : # 칸이 존재하고, 공기청정기가 아닌 경우에 확산
                room[ny][nx] += (value // 5) # 1에 의해서 영향받은 2의 값이 아니라, 기존의 2의 값을 활용
                spread_cnt += 1
        room[y][x] -= (value // 5) * spread_cnt

def clean():
    # 반시계 방향으로 도는 공기청정기
    y = cleaner[0][0]
    x = 1
    cnt_idx = 0
    tmp = 0

    while True:
        ny = y + dy[cnt_idx]
        nx = x + dx[cnt_idx]
        if ny == r or nx == c or nx == -1 or ny ==- 1:
            cnt_idx = (cnt_idx -1) % 4
            continue
        if y == cleaner[0][0] and x == 0:
            break
        room[y][x], tmp = tmp, room[y][x]
        y, x = ny, nx

    # 시계방향으로 도는 공기청정기
    y = cleaner[1][0]
    x = 1
    cnt_idx = 0
    tmp = 0
    while True:
        ny = y + dy[cnt_idx]
        nx = x + dx[cnt_idx]
        if ny == r or nx == c or nx == -1 or ny == - 1:
            cnt_idx = (cnt_idx + 1) % 4
            continue
        if y == cleaner[1][0] and x == 0:
            break

        room[y][x], tmp = tmp, room[y][x]
        y, x = ny, nx





r, c, t = map(int,input().split()) # 세로 r, 가로 c, 시간 t
room = [list(map(int,input().split())) for _ in range(r)] # -1은 공기청정기 2개가 위아래로 붙어있다.
current = 0
cleaner = [] # 공기 청정기 담을 배열 공기청정기 위치는 변하지 않음
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while current < t: # t초간
    dirt = [] # 미세먼지 담을 배열
    for i in range(r):
        for j in range(c):
            if room[i][j] != -1 and room[i][j] != 0 :
                dirt.append((i, j, room[i][j])) # r, c, value값 넣어주기
            elif room[i][j] == -1 and len(cleaner) < 2: # 맨 처음에만 공기청정기 2개 넣어줌
                cleaner.append((i,j)) # 위 아래로 있기 때문에 cleaner[0]이 무조건 위에 있음
    # 미세먼지 확산
    spread()
    # 공기청정기 청소
    clean()
    current += 1
ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] != -1 :
            ans += room[i][j]


print(ans)

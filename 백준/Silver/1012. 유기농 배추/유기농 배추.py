'''
백준 실버 2
유기농 배추
'''

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    m, n, k = map(int,input().split()) # 가로, 세로, 배추위치
    garden = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split()) # (가로, 세로)
        garden[b][a] = 1


    cnt = 0 #  배추지렁이의 마리 수
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = []
    for x in range(m):
        for y in range(n):
            if garden[y][x] == 1 : # 배추가 있으면
                cnt +=1
                garden[y][x] = 0
                queue = [(y,x)]
                while queue:
                    ay, ax = queue.pop(0)
                    for i in range(4):
                        nx = ax + dx[i]
                        ny = ay + dy[i]
                        if 0<=nx<m and 0<=ny<n and garden[ny][nx] == 1:
                            queue.append((ny,nx))
                            garden[ny][nx] = 0 # 근처 배추도 배추지렁이가 잡아먹음
    print(cnt)
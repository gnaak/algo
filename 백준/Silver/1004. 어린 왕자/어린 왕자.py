# 어린왕자

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int,input().split()) # 출발점 (x1,y1), 도착점 (x2,y2)
    n = int(input()) # 행성의 개수 n
    ans = 0
    for _ in range(n):
        cx, cy, cr = map(int,input().split()) # 행성의 중점 (cx, cy), 반지름 r
        dist1 = ((cx-x1)**2 + (cy-y1)**2)
        dist2 = ((cx-x2)**2 + (cy-y2)**2) 
        if (dist1 < cr ** 2 and dist2 > cr ** 2) or (dist1 > cr ** 2 and dist2 < cr ** 2):
            ans += 1
    print(ans)
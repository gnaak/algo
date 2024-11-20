# Fly me to the Alpha Centauri

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    x, y = map(int,input().split())
    dist = y - x
    n = 0
    while 1:
        if dist <= n*(n+1):
            break
        n += 1

    if dist <= n**2:
        print(n*2-1)
    else:
        print(n*2)
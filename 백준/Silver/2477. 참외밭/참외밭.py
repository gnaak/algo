import sys
input = sys.stdin.readline

k = int(input())
width = [0,0]
height = [0,0]
arr = [list(map(int,input().split())) for _ in range(6)]

mx_w, mx_h = 0, 0
for i in range(6) :
    d, n = arr[i]
    if (d == 1 or d == 2) and n > mx_w:
        mx_w = n
        width = [i,n]
    elif (d == 3 or d ==4) and n > mx_h:
        mx_h = n
        height = [i,n]

big_box = width[1] * height[1]
small_box = abs(arr[(width[0]+1)%6][1] - arr[(width[0]-1)%6][1]) * abs(arr[(height[0]+1)%6][1] - arr[(height[0]-1)%6][1])
print((big_box-small_box)*k)
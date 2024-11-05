# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


for i in range(1,n):
    for j in range(i+1):
        if j == 0 :
            arr[i][j] += arr[i-1][j]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[-1]))

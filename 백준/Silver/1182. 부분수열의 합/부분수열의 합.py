# 부분 수열의 합

import sys
input = sys.stdin.readline

def total(start, sum):
    global ans
    if sum == s and start > 0:
        ans += 1

    for i in range(start,n):
        total(i+1, sum+arr[i])

n, s = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
total(0,0)
print(ans)
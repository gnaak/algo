# 구간 합 구하기 4
# 수 n개가 주어졌을 때, i부터 j번째 수까지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def sum():
    n, m = map(int,input().split())
    arr = list(map(int,input().split())) # 배열
    dp = [0]*n
    dp[0] = arr[0]
    for i in range(1,n):
        dp[i] = dp[i-1] + arr[i]
    
    for i in range(m):
        start, end = map(int,input().split())
        if start == 1 :
            print(dp[end-1])
        else:
            print(dp[end-1]-dp[start-2])

sum()
'''
백준 실버 2
부분수열의 합
'''

import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 정수의 갯수 n, 정수 m
arr = list(map(int,input().split()))
cnt = 0
ans = []

def total(start):
    global cnt
    if sum(ans) == m and len(ans)>0:
        cnt+=1

    for i in range(start,n):
        ans.append(arr[i])
        total(i+1)
        ans.pop()

total(0)
print(cnt)
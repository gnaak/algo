'''
백준 골드 4
부분합
'''

import sys

n, s = map(int,input().split()) # n길이의 수열, 목표 합 s
nums = list(map(int,input().split()))
ans = 0
start = end = 0
cnt = sys.maxsize

while True:
    if ans >= s:
        cnt = min(cnt, end-start)
        ans -= nums[start]
        start +=1

    elif end == n:
        break

    else:
        ans+=nums[end]
        end +=1

if cnt == sys.maxsize:
    print(0)
else:
    print(cnt)
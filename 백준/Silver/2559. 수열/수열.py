'''
백준 실버 3
수열
'''

import sys
sys.stdin.readline

n, k = map(int,input().split())
temp = list(map(int,input().split()))
f = 0
for i in range(k):
    f += temp[i]
maxt = f
for i in range(k,n):
    f+=temp[i]
    f-=temp[i-k]
    maxt = max(maxt, f)
print(maxt)
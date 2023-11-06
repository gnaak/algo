import sys

N, M = list(map(int ,sys.stdin.readline().split()))

A = [[] for i in range(N)]
for t in range(M):
    i,j,k = list(map(int, sys.stdin.readline().split()))
    for p in range(i-1,j):
        A[p] = k
for i in A:
    if i:
        print(i , end=' ')
    else:
        print(0 , end =' ')
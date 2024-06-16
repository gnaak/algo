import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
cards = list(map(int,input().split()))
target = {}
for card in cards:
    if card in target:
        target[card] += 1
    else:
        target[card] = 1

m = int(input())
findout = list(map(int,input().split()))

for find in findout:
    if find in target:
        print(target[find], end =' ')
    else:
        print(0, end=' ')

        
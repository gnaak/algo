import sys
input = sys.stdin.readline

n = int(input())
have = set(map(int,input().split()))
m = int(input())
for card in list(map(int,input().split())):
    if card in have:
        print(1, end =' ')
    else:
        print(0, end= ' ')

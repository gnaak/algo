import sys
input = sys.stdin.readline

n = int(input())
cow = {}
cnt = 0
for _ in range(n):
    num, place = map(int,input().split())
    if num in cow and cow[num] != place:
        cnt +=1 
    cow[num] = place

print(cnt)
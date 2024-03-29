'''
백준 실버 5
좌표 정렬하기2
'''
import sys
n = int(sys.stdin.readline()) # 점의 개수
place = []
for i in range(n):
    x,y = map(int,input().split())
    place.append([x,y])
place.sort(key=lambda x : (x[1],x[0]))

for i in place:
    print(i[0], i[1])


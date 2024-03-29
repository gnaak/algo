'''
백준 실버 5
좌표 정렬하기
'''

n = int(input()) # 점의 개수
place = []
graph = [[] for _ in range(n)]
for i in range(n):
    x,y = map(int,input().split())
    place.append((x,y))
place.sort(key=lambda x : (x[0],x[1]))
for i in place:
    print(i[0], i[1])

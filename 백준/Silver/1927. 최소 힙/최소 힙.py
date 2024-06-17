import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())  # 연산의 개수
min_heap = []

for _ in range(n):
    a = int(input().strip())
    if a == 0:
        if min_heap:
            print(heapq.heappop(min_heap))  # 최소값을 힙에서 추출
        else:
            print(0)
    else:
        heapq.heappush(min_heap, a)  # 힙에 값을 추가

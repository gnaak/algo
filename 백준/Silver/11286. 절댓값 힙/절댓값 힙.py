# 절댓값 힙

import sys
input = sys.stdin.readline
import heapq


n = int(input())
abs_heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap,(abs(a),a))



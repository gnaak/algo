import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())  # Number of operations
heap = []

for _ in range(n):
    a = int(input().strip())
    if a == 0:
        if heap:
            print(-heapq.heappop(heap))  # Extract the maximum value from the heap
        else:
            print(0)
    else:
        heapq.heappush(heap, -a)  # Add the value to the heap (invert it for max-heap behavior)

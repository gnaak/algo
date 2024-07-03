import heapq
import sys

input = sys.stdin.read
data = input().strip().split("\n")

# 입력은 t개의 테스트 데이터로 구성
tc = int(data[0])

index = 1

for _ in range(tc):
    k = int(data[index])
    
    max_heap = []
    min_heap = []
    count = {}
    
    for i in range(1, k + 1):
        operation, number = data[index + i].split()
        number = int(number)
        
        if operation == 'I':
            heapq.heappush(max_heap, -number)
            heapq.heappush(min_heap, number)
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        elif operation == 'D':
            if number == 1 and max_heap:
                while max_heap and count[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    count[max_val] -= 1
            elif number == -1 and min_heap:
                while min_heap and count[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    count[min_val] -= 1
    
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    
    if max_heap and min_heap:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        print(max_val, min_val)
    else:
        print("EMPTY")
    
    index += k + 1

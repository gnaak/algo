import sys
input = sys.stdin.readline
from collections import deque

queue = deque([])
n = int(input())
result = []

for _ in range(n):
    command_lst = list(map(str, input().split()))
    command = command_lst[0]
    if command == 'push':
        queue.append(int(command_lst[1]))
    elif command == 'pop':
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif command == 'size':
        result.append(len(queue))
    elif command == 'empty':
        result.append(0 if queue else 1)
    elif command == 'front':
        result.append(queue[0] if queue else -1)
    else:  
        result.append(queue[-1] if queue else -1)

# 결과 한 번에 출력
print('\n'.join(map(str,result)))

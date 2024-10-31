# 큐 2

import sys
input = sys.stdin.readline
from collections import deque
queue = deque([])
n = int(input())
for _ in range(n):
    command_lst = list(map(str,input().split()))
    command = command_lst[0]
    if command == 'push':
        queue.append(int(command_lst[1]))
    elif command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
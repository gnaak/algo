import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    a = input().strip()
    if a[0:4] == 'push': #push X: 정수 X를 큐에 넣는 연산이다.
        queue.append(int(a[5:]))
        # print(a[5:])
    elif a == 'pop': # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
        if len(queue) > 0 :
            b = queue.popleft()
            print(b)
        else: # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
    elif a == 'size': # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    elif a == 'empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(queue) > 0 :
            print(0)
        else:
            print(1)
    elif a == 'front': # front: 큐의 가장 앞에 있는 정수를 출력한다.
        if len(queue) > 0 :
            print(queue[0])
        else: # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
    else:
        if len(queue) > 0: # back: 큐의 가장 뒤에 있는 정수를 출력한다.
            print(queue[-1])
        else:  # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
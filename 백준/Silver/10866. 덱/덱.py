# 덱을 구현한 다음, 입력으로 주어지는 명령 처리

import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 명령의 수
queue = []
for _ in range(n):
    prompt = input().strip()

    if 'push_front' in prompt:
        ans = []
        how, num = prompt.split()
        ans.append(num)
        ans += queue
        queue = ans

    elif 'push_back' in prompt:
        how, num = prompt.split()
        queue.append(num)

    elif prompt == 'pop_front':
        if len(queue) > 0 :
            a = queue.pop(0)
            print(a)
        else:
            print(-1)

    elif prompt == 'pop_back':
        if len(queue) > 0:
            a = queue.pop()
            print(a)
        else:
            print(-1)

    elif prompt == 'size':
        print(len(queue))

    elif prompt == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)

    elif prompt == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    elif prompt == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
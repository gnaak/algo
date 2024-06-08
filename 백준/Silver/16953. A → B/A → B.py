import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([(start, 1)]) # 연산 횟수 +1을 찾아야 하기 때문에 1로 시작 
    while queue:
        x, cnt = queue.popleft()
        if x > b: # *2, 숫자 뒤에 1 더해줄 수만 있기 때문에 이미 숫자가 커졌으면 무시
            continue
        if x == b: # 타겟 숫자가 나왔으면 연산 횟수 return 
            return cnt
        queue.append((x*2, cnt+1)) # *2하고 연산 +1
        queue.append((int(str(x)+str(1)), cnt+1)) # 뒤에 1 붙여준 후 연산 +1

    return -1

a, b = map(int,input().split())
print(bfs(a))
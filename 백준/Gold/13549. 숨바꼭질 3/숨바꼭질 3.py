import sys
input = sys.stdin.readline
from collections import deque

def bfs(now, target):
    if now == 0 :
        queue.append(1)
    else:
        queue.append(now)
    while queue:
        start = queue.popleft()
        if start == target:
            return time[target]
        for next in (start-1, start+1, 2*start):
            if 0<= next < 100001 and time[next] == 0:
                if next == 2*start:
                    time[next] = time[start]
                    queue.appendleft(next)
                else:
                    time[next] = time[start] + 1
                    queue.append(next)
# 1. 수빈이가 걷는다면 1초 후에 X-1, 혹은 X+1로 갈 수 있다.
# 2. 순간이동을 하는 경우에 0초 후에 2*X 위치로 갈 수 있다.
n, k = map(int,input().split()) # n: 수빈이의 현재 위치, k: 동생의 현재 위치
limit = 100001
time = [0]*limit # 동생의 위치는 최대 100000
queue = deque()

if n ==0 :
    if k == 0 :
        print(0)
    else:
        print(bfs(n,k)+1) # 0으로 시작하면 무조건 1로 넘어가야하기 때문에 1초 소요
else:
    print(bfs(n,k))
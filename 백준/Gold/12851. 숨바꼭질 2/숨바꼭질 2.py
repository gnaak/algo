import sys
input = sys.stdin.readline
from collections import deque
INF = sys.maxsize

def bfs(now, target):
    queue.append(now)
    while queue:
        start = queue.popleft()
        if start == target:
            return time[target]
        for next in (start-1, start+1, 2*start):
            if 0<= next < 100001:
                if time[next][0] >= time[start][0] + 1 : # 더 줄일 수 있는 방법 중에서
                    if time[next][0] == time[start][0]+ 1 : # 만약에 동일한 방법이 있으면
                        time[next][1] += 1 # 방법의 개수 += 1
                    else: # 지금 값이 최소라면,
                        time[next][0] = time[start][0] + 1
                        time[next][1] = 1 # 1가지 방법이 있다고 표시
                    queue.append(next)

# 1. 수빈이가 걷는다면 1초 후에 X-1, 혹은 X+1로 갈 수 있다.
# 2. 순간이동을 하는 경우에 1초 후에 2*X 위치로 갈 수 있다.
n, k = map(int,input().split()) # n: 수빈이의 현재 위치, k: 동생의 현재 위치
limit = 100001
# 하나는 걸리는 시간 기록용, 하나는 방법의 수 기록용
time = [[INF,0] for _ in range(limit)] # 동생의 위치는 최대 100000
time[n][0] = 0
queue = deque()

if n == k :
    print(0)
    print(1)
else:
    a, b = bfs(n, k)
    print(a)
    print(b)
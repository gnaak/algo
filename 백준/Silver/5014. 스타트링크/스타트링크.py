# 스타트링크

import sys
input = sys.stdin.readline
from collections import deque

def elevator():
    visited = [-1]*(F+1)
    queue = deque([(S,0)])
    visited[S] = 0

    while queue:
        current, btn = queue.popleft()
        if current == G:
            return btn
        up_nxt, down_nxt = current+U, current-D
        if up_nxt <= F and visited[up_nxt] == -1:
            queue.append((up_nxt,btn+1))
            visited[up_nxt] = btn + 1
        if down_nxt >= 1 and visited[down_nxt] == -1:
            queue.append((down_nxt, btn+1))
            visited[down_nxt] = btn+1
    return visited[G]
F, S, G, U, D = map(int,input().split())
ans = elevator()
print(ans if ans != -1 else 'use the stairs')
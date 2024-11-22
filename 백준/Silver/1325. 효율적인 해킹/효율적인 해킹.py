# 효율적인 해킹

import sys
input = sys.stdin.readline
from collections import deque

def main(num):
    visited = [0]*(n+1)
    queue = deque([num])
    visited[num] = 1
    cnt = 1
    while queue:
        cur_num = queue.popleft()
        for nxt_num in net[cur_num]:
            if visited[nxt_num] == 0 :
                queue.append(nxt_num)
                visited[nxt_num] = 1
                cnt += 1
    return cnt

n, m = map(int,input().split())
net = [[] for _ in range(n+1)]
for _ in range(m):
    child, parent = map(int,input().split())
    net[parent].append(child)
ans = 0
ans_lst = []
for i in range(1,n+1):
    count = main(i)
    if ans < count:
        ans_lst = [i]
        ans = count
    elif ans == count:
        ans_lst.append(i)

print(*ans_lst)
# 회장 뽑기

import sys
input = sys.stdin.readline
import heapq
inf = 1e9

def vote(cand):
    dist = [inf]*(n+1)
    queue = []
    heapq.heappush(queue,(0,cand))
    dist[0], dist[cand] = 0, 0
    while queue:
        score, candid = heapq.heappop(queue)
        for friend in cands[candid]:
            if dist[friend] > score +1:
                dist[friend] = score +1
                heapq.heappush(queue,(score+1, friend))

    return cand, max(dist)
n = int(input())
cands = [[]*(n+1) for _ in range(n+1)]

while 1 :
    a, b = map(int,input().split())
    if a == -1 and b == -1 :
        break

    cands[a].append(b)
    cands[b].append(a)

cand_score = inf
cand = []

for i in range(1,len(cands)):
    name, score = vote(i)
    if cand_score > score:
        cand_score = score
        cand = [name]
    elif cand_score == score:
        cand.append(name)

print(cand_score, len(cand))
print(*cand)
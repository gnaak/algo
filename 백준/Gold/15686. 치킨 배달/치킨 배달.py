# 치킨배달

# 크기가 n*n인 도시
# 도시는 빈칸, 치킨집, 집 중 하나
# 치킨 거리는 집에서부터 가장 가까운 치킨 집의 치킨 거리
# 도시의 치킨 거리는 모든 치킨 거리의 합

import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global min_ans

    if cnt == m :
        ans = 0
        for i in home:
            dist = 9999
            for j in range(len(store)):
                if visited[j]:
                    store_dist = abs(i[0]-store[j][0]) + abs(i[1]-store[j][1])
                    dist = min(dist, store_dist)
            ans += dist
        min_ans = min(ans, min_ans)

    else:
        for i in range(idx, len(store)):
            if visited[i] == 0 :
                visited[i] = 1
                dfs(i+1, cnt + 1)
                visited[i] = 0

n, m = map(int,input().split())
home = []
store = []
for i in range(n):
    rows = list(map(int,input().split()))
    for j in range(n):
        if rows[j] == 1 :
            home.append((i, j))
        elif rows[j] == 2 :
            store.append((i, j))
min_ans = 9999
visited = [0 for _ in range(len(store))]

dfs(0,0)
print(min_ans)
import sys
input = sys.stdin.readline

def dfs(now, idx):
    for node in arr[idx]: # 나보다 큰 친구들을 돌면서
        if visited[now][node] == 0 : # 아직 확인을 안한 친구면,
            visited[now][node]= 1 # 나보다 크다고 표시를 해주고
            visited[node][now]= 1 # 반대로 그 친구한테는 내가 더 작은걸 아는 것을 표시
            dfs(now,node) # 이제 나보다 더 친구보다 큰 친구를 찾으러 출발

n, m = map(int,input().split()) # 학생의 수, 비교한 횟수
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b) # 나보다 큰 아이들을 넣어준다

visited = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    visited[i][i] = 1
    dfs(i,i)

cnt = 0
for i in range(1,n+1):
    if sum(visited[i]) == n :
        cnt += 1

print(cnt)
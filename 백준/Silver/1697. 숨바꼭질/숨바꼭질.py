def bfs(n, k):
    q = [n]
    visited[n] = 1
    while q:
        i = q.pop(0)
        if i == k:
            return visited[k]
        for j in [i-1, i+1, i*2]:
            if 0<= j < 100001 and visited[j] == 0:
                visited[j] = visited[i]+1
                q.append(j)

n, k = map(int,input().split())
visited = [0] * 100001
print(bfs(n,k)-1)

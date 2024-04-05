import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):

    def bfs(currnet):
        global cnt
        visited[currnet] = 1
        for i in range(n+1):
            if visited[i] == 0 and trv[currnet][i] == 1:
                bfs(i)
                cnt+=1

    #  n : 국가의 수, m : 비행기의 종류
    n, m = map(int,input().split())
    trv = [[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int,input().split())
        trv[a][b] = 1
        trv[b][a] = 1

    visited = [0]*(n+1)
    global cnt
    cnt = 0 # 비행기 개수
    # 여행 시작
    bfs(1)

    print(cnt)

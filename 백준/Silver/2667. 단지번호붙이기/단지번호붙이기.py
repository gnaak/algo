n = int(input())
maps = [list(map(int,input())) for _ in range(n)]
cnt_ls = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            cnt = 1
            q = []
            q.append((i,j))
            maps[i][j] = 0
            while q:
                k, l = q.pop(0)
                for di, dj in [[1,0],[0,1],[0,-1],[-1,0]]:
                    ni, nj = k+di, l+dj
                    if 0<=ni<n and 0<=nj<n and maps[ni][nj]==1:
                        cnt += 1
                        q.append((ni,nj))
                        maps[ni][nj] = 0
            if cnt:
                cnt_ls.append(cnt)
cnt_ls.sort()
print(len(cnt_ls))
for i in range(len(cnt_ls)):
    print(cnt_ls[i])
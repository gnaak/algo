n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결되어 있는 컴퓨터의 수
com = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)

infected = [0]*(n+1)
queue = [1]
while queue:
    vir = queue.pop(0)
    infected[vir] = 1
    for nxt in com[vir]:
        if infected[nxt] == 0:
            queue.append(nxt)

print(sum(infected)-1)
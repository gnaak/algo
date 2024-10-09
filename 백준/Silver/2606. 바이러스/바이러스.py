import sys
input = sys.stdin.readline
n = int(input()) # 컴퓨터의 숫자


network =[[] for _ in range(n+1)]
m = int(input()) # 컴퓨터들이 연결되어 있는 숫자
for _ in range(m):
    s, e = map(int,input().split())
    network[s].append(e)
    network[e].append(s)
queue = [1]
infected = [0] * (n+1)
infected[1] = 1
while queue:
    current = queue.pop(0)
    infected[current] = 1

    for nxt_computer in network[current]:
        if infected[nxt_computer] == 0 :
            queue.append(nxt_computer)

print(sum(infected)-1)
import sys
input = sys.stdin.readline
INF = sys.maxsize

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if buses[i][j] > buses[i][k] + buses[k][j]:
                    buses[i][j] = buses[i][k] + buses[k][j]
    return buses

n = int(input()) # n개의 도시
m = int(input()) # m 개의 버스

buses = [[INF]*n for _ in range(n)] # 버스 노선
for _ in range(m):
    a, b, c = map(int,input().split()) # 출발 도시, 도착 도시, 가격
    if buses[a-1][b-1] > c : # 초기 값은 c
        buses[a - 1][b - 1] = c  # 초기 값은 c

for i in range(n):
    buses[i][i] = 0 # 출발 지점과 도착 지점이 같을 수는 없다

cost = floyd()

for i in range(n):
    for j in range(n):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')

    print()
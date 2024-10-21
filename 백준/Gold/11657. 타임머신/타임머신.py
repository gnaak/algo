import sys
input = sys.stdin.readline
inf = 1e9

def bellman_ford():
    distance = [inf] * (n + 1)
    distance[1] = 0

    # n-1번 반복하며 모든 간선 확인
    for i in range(n):
        for current in range(1, n + 1):
            for nxt_stop, val in bus[current]:
                if distance[current] != inf and distance[nxt_stop] > distance[current] + val:
                    distance[nxt_stop] = distance[current] + val
                    # n번째 반복에서 값이 갱신되면 음수 사이클 존재
                    if i == n - 1:
                        return True, []

    return False, distance

n, m = map(int, input().split())  # 도시 수, 버스 수
bus = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, time = map(int, input().split())
    bus[start].append((end, time))

has_cycle, distances = bellman_ford()

if has_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distances[i] == inf:
            print(-1)  # 경로가 없는 경우
        else:
            print(distances[i])

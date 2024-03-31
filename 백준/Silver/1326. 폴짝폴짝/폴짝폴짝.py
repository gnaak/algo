import sys
from collections import deque


def bfs():
    queue = deque([a - 1]) # a번째 다리부터 탐색
    visited = [-1] * 100000
    visited[a - 1] = 0 # a 번째 다리는 시작점으로 0으러 초기화

    # 건너야 하는 다리를 모두 탐색
    while queue:
        target = queue.popleft() # 현재 건너는 다리

        # 반복문을 통해 현재 다리에서 앞으로 건넌다.
        for i in range(target, n, m[target]):
            # 탐색하지 않은 다리라면
            if visited[i] == -1:
                queue.append(i) # 건너야 하는 다리의 추가
                visited[i] = visited[target] + 1 # 점프 수 카운트

                # 현재 다리가 b번 다리라면 현재 다리까지 점프한 수를 출력
                if i == b - 1:
                    return visited[i]

        # 반복문을 통해 현재 다리에서 뒤로 간다.
        for i in range(target, -1, -m[target]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[target] + 1
                if i == b - 1:
                    return visited[i]

    # b번 다리를 가지 못했다면 -1 출력
    return -1


n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
print(bfs())
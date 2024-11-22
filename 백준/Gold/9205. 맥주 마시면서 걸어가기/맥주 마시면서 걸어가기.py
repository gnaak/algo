import sys
from collections import deque

input = sys.stdin.readline


def can_reach():
    queue = deque([house])

    while queue:
        x, y = queue.popleft()

        # 목적지에 도달 가능한지 확인
        if abs(x - desti[0]) + abs(y - desti[1]) <= 1000:
            return "happy"

        # 방문하지 않은 편의점 탐색
        for i in range(n):
            if not visited_convi[i]:
                convi_x, convi_y = convi[i]
                if abs(x - convi_x) + abs(y - convi_y) <= 1000:
                    visited_convi[i] = True
                    queue.append((convi_x, convi_y))

    return "sad"


t = int(input())
for _ in range(t):
    n = int(input())  # 편의점 수
    house = tuple(map(int, input().split()))  # 집 좌표
    convi = [tuple(map(int, input().split())) for _ in range(n)]  # 편의점 좌표
    desti = tuple(map(int, input().split()))  # 목적지 좌표

    # 방문 확인 리스트 초기화
    visited_convi = [False] * n

    # 결과 출력
    print(can_reach())

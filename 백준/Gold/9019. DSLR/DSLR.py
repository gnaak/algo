import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append((a, ""))  # 시작 상태와 명령어 경로
    visited[a] = True   # 시작 상태 방문 처리

    while q:
        current, path = q.popleft()
        if current == b:  # 목표 숫자 도달 시 경로 반환
            return path

        # D 명령
        d = (current * 2) % 10000
        if not visited[d]:
            visited[d] = True
            q.append((d, path + "D"))

        # S 명령
        s = current - 1 if current != 0 else 9999
        if not visited[s]:
            visited[s] = True
            q.append((s, path + "S"))

        # L 명령
        l = (current % 1000) * 10 + current // 1000
        if not visited[l]:
            visited[l] = True
            q.append((l, path + "L"))

        # R 명령
        r = (current % 10) * 1000 + current // 10
        if not visited[r]:
            visited[r] = True
            q.append((r, path + "R"))

t = int(input())  # 테스트 케이스 수 입력
for _ in range(t):
    a, b = map(int, input().split())  # a와 b 입력 받기
    visited = [False] * 10000  # 방문 배열 초기화
    print(bfs(a, b))  # 결과 출력

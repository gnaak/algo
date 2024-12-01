import sys
from collections import deque

input = sys.stdin.readline


def bfs(target):
    # (화면의 이모티콘 개수, 클립보드 이모티콘 개수)
    visited = set()
    queue = deque([(1, 0, 0)])  # (현재 화면 이모티콘, 클립보드 이모티콘, 시간)
    visited.add((1, 0))

    while queue:
        screen, clipboard, time = queue.popleft()

        # 목표 이모티콘 개수 도달 시 반환
        if screen == target:
            return time

        # 1. 화면의 이모티콘을 클립보드에 복사
        if (screen, screen) not in visited:
            visited.add((screen, screen))
            queue.append((screen, screen, time + 1))

        # 2. 클립보드 이모티콘을 화면에 붙여넣기
        if clipboard > 0 and screen + clipboard <= target and (screen + clipboard, clipboard) not in visited:
            visited.add((screen + clipboard, clipboard))
            queue.append((screen + clipboard, clipboard, time + 1))

        # 3. 화면의 이모티콘 하나 삭제
        if screen > 0 and (screen - 1, clipboard) not in visited:
            visited.add((screen - 1, clipboard))
            queue.append((screen - 1, clipboard, time + 1))


# 입력 및 출력
n = int(input())
print(bfs(n))

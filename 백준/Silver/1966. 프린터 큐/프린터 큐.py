import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())  # 문서의 개수와 타겟 인덱스
    priorities = deque(map(int, input().split()))
    indices = deque(range(n))  # 문서의 인덱스를 저장하는 큐

    ans = 0
    while priorities:
        if priorities[0] == max(priorities):  # 가장 높은 우선순위가 맨 앞일 때
            ans += 1
            priorities.popleft()
            printed_index = indices.popleft()
            if printed_index == m:  # 타겟 문서가 인쇄된 경우
                break
        else:
            priorities.rotate(-1)
            indices.rotate(-1)  # 우선순위와 인덱스 둘 다 회전

    print(ans)

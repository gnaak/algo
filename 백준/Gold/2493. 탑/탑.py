import sys

input = sys.stdin.readline

n = int(input())  # 탑의 개수
top = list(map(int, input().split()))

ans = [0] * n  # 결과를 저장할 리스트
stack = []  # 스택 초기화

# 왼쪽으로 탐색
for i in range(n):
    # 현재 탑보다 낮은 탑은 스택에서 제거
    while stack and top[stack[-1]] < top[i]:
        stack.pop()

    # 스택이 비어 있지 않다면, 현재 탑보다 높은 탑의 인덱스를 ans에 추가
    if stack:
        ans[i] = stack[-1] + 1  # 1-based index
    else:
        ans[i] = 0  # 없다면 0으로 설정

    # 현재 탑의 인덱스를 스택에 추가
    stack.append(i)

print(*ans)

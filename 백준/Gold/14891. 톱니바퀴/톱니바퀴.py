import sys
from collections import deque

input = sys.stdin.readline

# 바퀴 회전 함수
def twist(number, direction):
    wheel = wheels[number]
    if direction == 1:  # 시계 방향
        a = wheel.pop()
        wheel.appendleft(a)
    else:  # 반시계 방향
        a = wheel.popleft()
        wheel.append(a)

# 회전할 바퀴들 체크 함수
def check(num, dir):
    moved[num] = dir  # 회전 방향 저장
    left, right = num - 1, num + 1

    # 왼쪽 바퀴 검사
    while left >= 0:
        if wheels[left][2] != wheels[left + 1][6]:  # 톱니가 맞닿는 부분이 다르면
            moved[left] = -moved[left + 1]  # 반대 방향으로 회전
        else:
            break  # 같은 톱니면 회전하지 않음
        left -= 1

    # 오른쪽 바퀴 검사
    while right < 4:
        if wheels[right][6] != wheels[right - 1][2]:  # 톱니가 맞닿는 부분이 다르면
            moved[right] = -moved[right - 1]  # 반대 방향으로 회전
        else:
            break  # 같은 톱니면 회전하지 않음
        right += 1

    # 회전 적용
    for i in range(4):
        if moved[i] != 0:
            twist(i, moved[i])

uno = deque(map(int, input().strip()))
dos = deque(map(int, input().strip()))
thr = deque(map(int, input().strip()))
qua = deque(map(int, input().strip()))
wheels = [uno, dos, thr, qua]
k = int(input())
cmds = [list(map(int, input().split())) for _ in range(k)]

for cmd in cmds:
    moved = [0, 0, 0, 0]  # 바퀴별 회전 상태 초기화
    num, dir = cmd
    check(num - 1, dir)

# 결과 계산
ans = 0
if uno[0] == 1:
    ans += 1
if dos[0] == 1:
    ans += 2
if thr[0] == 1:
    ans += 4
if qua[0] == 1:
    ans += 8

print(ans)

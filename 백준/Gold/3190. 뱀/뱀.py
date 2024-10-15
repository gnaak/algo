import sys
from collections import deque

input = sys.stdin.readline


# 방향 전환 함수
def turn(direction, turn_dir):
    if turn_dir == 'L':
        return (direction - 1) % 4  # 왼쪽 회전 (반시계)
    else:
        return (direction + 1) % 4  # 오른쪽 회전 (시계 방향)


# 게임 진행 함수
def check():
    direction = 0  # 처음에는 오른쪽을 보고 있음 (0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위)
    time = 0
    queue = deque([(0, 0)])  # 뱀의 몸통을 큐로 관리
    board[0][0] = 2  # 뱀이 있는 곳을 2로 표시 (1: 사과, 2: 뱀)

    move_direction = 0  # 현재 방향 변환 명령의 인덱스

    while True:
        # 다음에 이동할 위치 계산
        head_row, head_col = queue[-1]
        nxt_row, nxt_col = head_row + dy[direction], head_col + dx[direction]

        # 벽이나 자기 자신의 몸과 부딪혔는지 체크
        if not (0 <= nxt_row < n and 0 <= nxt_col < n) or board[nxt_row][nxt_col] == 2:
            return time + 1

        # 사과가 있는지 확인
        if board[nxt_row][nxt_col] == 1:  # 사과가 있으면 머리만 이동 (꼬리 그대로)
            board[nxt_row][nxt_col] = 2
            queue.append((nxt_row, nxt_col))
        else:  # 사과가 없으면 머리 이동하고 꼬리도 이동 (꼬리 칸 비움)
            board[nxt_row][nxt_col] = 2
            queue.append((nxt_row, nxt_col))
            tail_row, tail_col = queue.popleft()
            board[tail_row][tail_col] = 0  # 꼬리 칸을 비움

        time += 1

        # 방향을 바꿔야 하는 시간이 되었는지 확인
        if move_direction < l:
            spend_time, nxt_direction = moves[move_direction]
            if time == int(spend_time):
                direction = turn(direction, nxt_direction)  # 방향 전환
                move_direction += 1


# 입력 처리
n = int(input())  # n*n 격자판
board = [[0] * n for _ in range(n)]
m = int(input())  # 사과의 개수
for _ in range(m):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1  # 사과를 1로 표시

l = int(input())  # 방향 변환 횟수
moves = []
for _ in range(l):
    time, direction = input().split()
    moves.append((time, direction))

# 방향 (0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(check())

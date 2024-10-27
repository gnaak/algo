# 컨베이어 벨트 위의 로봇

# 길이가 n인 컨베이어 벨트 -> 길이가 2n인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다.
# 1  2    3    ... n-1  n
# 2n 2n-1 2n-2 ... n+2  n+1

# 1번 칸은 올리는 위치, n번 칸은 내리는 위치
# 로봇은 올리는 위치에만 올릴 수 있고, 내리는 위치에 도달하면 그 즉시 내린다.

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
belt = deque(map(int,input().split()))

step = 0
robots = deque([0]*n)
while 1 :

    # 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전한다.
    belt.rotate()
    robots.rotate()

    robots[-1] = 0

    # 2. 가장 먼저 벨트가 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면, 이동한다.
    if sum(robots):
        for i in range(n-2,-1,-1):
            # 로봇이 위치하고, 한 칸 이동할 수 있다면 (이동하려는 칸에 내구도가 남아있고, 다른 로봇이 없는 경우에)
            if robots[i] != 0 and belt[i+1] > 0 and robots[i+1] == 0:
                belt[i+1] -= 1
                robots[i+1] = 1
                robots[i] = 0
            robots[-1] = 0 # 마지막 칸에 있는 로봇은 자동으로 내린다.


    # 3. 로봇을 올릴 수 있으면 올리기
    if robots[0] == 0 and belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1

    step +=1

    if belt.count(0) >= k:
        break




print(step)
import sys
input = sys.stdin.readline
from collections import deque

# 3가지 연산
# 1. 첫 번째 원소를 뽑아낸다
# 2. 왼쪽으로 한 칸 이동시킨다
# 3. 오른쪽으로 한 칸 이동 시킨다.

# 타겟을 주어진 순서대로 뽑는데 드는 2번, 3번 연산의 최솟값
n, m = map(int,input().split())
target = list(map(int,input().split())) # 타겟을 주어진 순서대로 뽑아야 함
queue = deque([i for i in range(1,n+1)]) # 크기는 1부터 n까지
cnt = 0 # 연산 횟수

# 뽑아내는 것은 무조건 첫 번째 원소만 가능

i = 0 # target 인덱스 번호
while i < m :
    if target[i] == queue[0]:
        queue.popleft()
        i += 1
    else: # 왼쪽, 오른쪽 이동시켜서 맨 처음으로 보내야 함
        # 왼쪽의 길이와 오른쪽의 길이를 비교?
        a = queue.index(target[i])
        if a < len(queue)/2 : # 현재 queue의 절반보다 작으면(0에 더 가까우면, 2번 연산을 a번 만큼 실행하면 a = 0이됨
            cnt += a
            for _ in range(a):
                b = queue.popleft()
                queue.append(b)
        else:
            k = len(queue) - a  # 반대로 절반보다 크면(끝에 가까우면, 총 길이가 5인데, 인덱스가 4번째면, 끝까지 가게하고 + 1해서 0번 인덱스로
            cnt += k
            for _ in range(k):
                b = queue.pop()
                queue.appendleft(b)

print(cnt)

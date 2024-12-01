import sys
from collections import deque
input = sys.stdin.readline

def pour(from_amount, to_amount, to_capacity):
    # from 물통에서 to 물통으로 옮길 수 있는 최대 물 양 계산
    transfer = min(from_amount, to_capacity - to_amount)
    return from_amount - transfer, to_amount + transfer

def solve():
    A, B, C = map(int, input().split())
    visited = set()
    result = set()
    queue = deque([(0, 0)])  # 초기 상태: (a=0, b=0)

    while queue:
        a, b = queue.popleft()
        c = C - a - b  # 세 번째 물통의 물 양은 총합에서 계산

        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == 0:
            result.add(c)

        # 6가지 물 옮기기 시도
        # a → b
        next_a, next_b = pour(a, b, B)
        queue.append((next_a, next_b))
        # a → c
        next_a, next_c = pour(a, c, C)
        queue.append((next_a, b))
        # b → a
        next_b, next_a = pour(b, a, A)
        queue.append((next_a, next_b))
        # b → c
        next_b, next_c = pour(b, c, C)
        queue.append((a, next_b))
        # c → a
        next_c, next_a = pour(c, a, A)
        queue.append((next_a, b))
        # c → b
        next_c, next_b = pour(c, b, B)
        queue.append((a, next_b))

    print(" ".join(map(str, sorted(result))))

solve()

import sys
input = sys.stdin.readline

# 체스판의 크기는 8 * 8

board = [[] for _ in range(8)]
for i in range(8):
    board[i] = input().strip()

cnt = 0
for i in range(8): # 세로 순회
    for j in range(8): # 가로 순회
        if (i+j)% 2 == 0 and board[i][j] == 'F':
            cnt += 1

print(cnt)
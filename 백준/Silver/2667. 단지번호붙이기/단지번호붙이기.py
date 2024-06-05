'''
백준 실버 1
단지번호붙이기
'''


def bfs(i,j):
    queue = [(i,j)]
    nums = 1
    while queue:
        y, x = queue.pop(0)
        for k in range(4):
            ny = y +dy[k]
            nx = x +dx[k]
            if 0<=nx<n and 0<=ny<n and board[ny][nx] == 1:
                queue.append((ny,nx))
                nums +=1
                board[ny][nx] = 0
    return nums

n = int(input()) # 지도의 가로, 세로 크기
board = [list(map(int,input())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
num_lis = []
for i in range(n): # 세로 순회
    for j in range(n): # 가로 순회
        if board[i][j] == 1:
            board[i][j] = 0
            cnt += 1
            num_lis.append(bfs(i,j))
num_lis.sort()
print(cnt)
for i in range(len(num_lis)):
    print(num_lis[i])
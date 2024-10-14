# 테트로미노
# 5개의 테트로미노

import sys
input = sys.stdin.readline

def check(tetromino):
    global max_numbers

    # 1번 테트로미노 : 세로4칸 or 가로4칸
    ans = 0
    if tetromino == 1 :
        for i in range(n):
            for j in range(m):
                if i+3 < n :
                    ans = max(ans,board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])
                if j+3 < m :
                    ans = max(ans,board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3])

    # 2번 테트로미노 : 정사각형
    elif tetromino == 2 :
        for i in range(n):
            for j in range(m):
                if i+1 < n and j+1 < m:
                    ans = max(ans,board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1])

    # 3번 테트로미노 : ㅡㅡㅡㅣ
    elif tetromino == 3 :
        for i in range(n):
            for j in range(m):
                if i+1<n and j+2<m :
                    ans = max(ans,
                              board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2],
                              board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j],
                              board[i][j+2]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2],
                              board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+2],
                              )
                if i+2 < n and j+1 < m :
                    ans = max(ans,
                              board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j+1],
                              board[i][j+1]+board[i+1][j+1]+board[i+2][j+1]+board[i+2][j],
                              board[i][j]+board[i+1][j]+board[i+2][j]+board[i][j+1],
                              board[i][j]+board[i+1][j+1]+board[i+2][j+1]+board[i][j+1],
                              )

    elif tetromino == 4 :
        for i in range(n):
            for j in range(m):
                if i+1<n and j+2 < m :
                    ans = max(ans,board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+1][j+2], board[i][j+1]+board[i][j+2]+board[i+1][j]+board[i+1][j+1])
                if i+2 < n and j+1 < m:
                    ans = max(ans, board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1], board[i][j+1]+board[i+1][j+1]+board[i+1][j]+board[i+2][j])


    else:
        for i in range(n):
            for j in range(m):
                if i+1 < n and j+2 < m :
                    ans = max(ans,board[i][j+1]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2], board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+1])
                if i+2 < n and j+1 < m :
                    ans = max(ans,board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j], board[i+1][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1])




    max_numbers = max(max_numbers, ans)



n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

max_numbers = 0

for number in range(1,6): # 1번부터 5번까지 테트로미노에 대해서 최대값 찾기
    check(number)

print(max_numbers)
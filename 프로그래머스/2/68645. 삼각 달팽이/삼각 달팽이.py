def solution(n):
    answer = []
    visited = [[0] * n for _ in range(n)]
    tot_snail = sum(i for i in range(1,n+1)) # 달팽이가 채울 마지막 숫자

    visited[0][0] = 1
    y, x = 0, 0
    turn = False
    for i in range(2,tot_snail+1):
        if not turn:
            if y+1<n and visited[y+1][x] == 0:
                y += 1
                visited[y][x] = i
            elif x+1 < n and visited[y][x+1] == 0:
                x += 1
                visited[y][x] = i
            else:
                turn = True

        if turn:
            if y-1 > 0 and x-1 > 0 and visited[y-1][x-1] == 0:
                y -= 1
                x -= 1
                visited[y][x] = i
            else:
                turn = False
                if y+1 < n and visited[y+1][x] == 0 :
                    y += 1
                    visited[y][x] = i


    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0 :
                answer.append(visited[i][j])    
    
    return answer
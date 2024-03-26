def solution(n, computers):
    answer = 0
    visited = [0]*n

    def dfs(current):
        visited[current] = 1
        for i in range(n):
            if visited[i] == 0 and computers[current][i] == 1:
                dfs(i)
                
    for i in range(n):
        if visited[i] == 0:
            answer+=1
            dfs(i)
                
    return answer
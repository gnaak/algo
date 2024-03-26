def solution(numbers, target):
    global answer
    answer = 0
    def dfs(sum, depth):
        global answer
        if depth == len(numbers):
            if sum == target: 
                answer+=1
            return
        

        dfs(sum+numbers[depth], depth+1)
        dfs(sum-numbers[depth], depth+1)
            
    dfs(0,0)
    return answer
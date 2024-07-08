function solution(numbers, target) {
    
    const dfs =(now, depth) => {
        if (depth == numbers.length){
            if (now == target) answer++;
            return
        }
        dfs(now+numbers[depth], depth+1)
        dfs(now-numbers[depth], depth+1)
    }
    
    
    var answer = 0;
    dfs(0,0)

    return answer;
}
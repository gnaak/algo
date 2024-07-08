function solution(t) {
    t.sort()
    let visited = Array(t.length).fill(0)
    let answer = ["ICN"]
    let result = []
    function dfs(start, cnt, answer){
        if (cnt == t.length){
            result.push(answer.slice())
            return 
        }
        for (let i =0; i<t.length; i++){
            if (t[i][0] == start && visited[i] == 0){
                visited[i] = 1
                answer.push(t[i][1])
                dfs(t[i][1], cnt+1,answer)
                answer.pop()
                visited[i] = 0 
                
            }
        }

    }
    dfs("ICN", 0, answer);
    return result[0]
}
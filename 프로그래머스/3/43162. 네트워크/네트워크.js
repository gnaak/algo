function solution(n, computers) {
    const visited = []
    for (let i=0; i<n;i++){
        visited.push(0)
    }
    function dfs(current){
        visited[current] = 1;
        for (let i = 0; i<n; i++){
            if(computers[current][i] == 1 && visited[i] == 0){
                dfs(i)
            }           
        }
    }
    let answer = 0;
    for (let i = 0 ; i<n;i++){
        if (visited[i] == 0){
            dfs(i);
            answer ++
        }
    }
    return answer;
}
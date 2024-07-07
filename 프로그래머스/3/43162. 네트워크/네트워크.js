function solution(n, computers) {
    let visited = Array.from({ length: n }, () => 0);

    function bfs(start) {
        let q = [];
        q.push(start);
        visited[start] = 1;

        while (q.length > 0) {
            let now = q.shift();
            for (let next = 0; next < n; next++) {
                if (computers[now][next] === 1 && visited[next] === 0) {
                    visited[next] = 1;
                    q.push(next);
                }
            }
        }
    }

    let answer = 0;
    for (let i = 0; i < n; i++) {
        if (visited[i] === 0) {
            bfs(i);
            answer++;
        }
    }

    return answer;
}



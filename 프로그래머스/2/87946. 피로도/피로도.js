function solution(k, d) {
  const dfs = (k, cnt) => {
    answer = Math.max(answer, cnt);

    for (let i = 0; i < d.length; i++) {
      if (k >= d[i][0] && visited[i] == 0) {
        visited[i] = 1;
        dfs(k - d[i][1], cnt + 1);
        visited[i] = 0;
      }
    }
  };

  var answer = 0;
  let visited = Array(d.length).fill(0);
  dfs(k, 0);
  return answer;
}

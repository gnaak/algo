function solution(n, wires) {
  function bfs(graph, cnt) {
    q = [];
    visited = Array(n).fill(0);
    q.push(0);
    visited[0] = 1;

    while (q.length) {
      s = q.shift();
      for (next of graph[s]) {
        if (visited[next] == 0) {
          q.push(next);
          visited[next] = 1;
          cnt++;
        }
      }
    }
    return cnt;
  }

  function makeGraph(n, wire) {
    let graph = Array.from({ length: n }, () => []); // 배열을 n개의 빈 배열로 초기화
    for ([s, e] of wire) {
      // 양방향 그래프이므로 양쪽에 다 표시해줌 
      graph[s - 1].push(e - 1);
      graph[e - 1].push(s - 1);
    }
    return graph;
  }

  let answer = n;

  for (let i = 0; i < n; i++) {
    // 1. 전선을 하나씩 자르기
    let wire = [...wires.slice(0, i), ...wires.slice(i + 1)];
    // 2. 자른 배열로 그래프 만들기 
    let graph = makeGraph(n, wire)
    // 3. 만든 그래프로 bfs 돌리기 
    let one = bfs(graph,1)
    answer = Math.min(answer, Math.abs(n - one - one));
  }

  return answer;
}